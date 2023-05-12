from random import shuffle

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View

from app.models import *
from .forms import RegistrationForm, AuthenticationForm, UploadForm, UserEditForm

# from app.crawler import parsed_data

logged = False
user_info = {}


class ProductView(View):
    def get(self, request):
        # for i in parsed_data:
        #     product = Products(manufacturer=i['manufacturer'],
        #                        name=i['name'],
        #                        price=(i['price'].replace(' ', '')),
        #                        characteristics=i['description'],
        #                        image=i['image'],
        #                        category=Categories.objects.get(id=1),
        #                        url=i['url_to_product'])
        #     product.save()

        products = Products.objects.all()
        products_list = list(products)
        shuffle(products_list)
        active = [''] * 4
        active[0] = 'active'
        return render(request, 'Home/Home.html', {'products': products_list,
                                                  'active': active,
                                                  'logged': logged,
                                                  'user_info': user_info})


class UserDetailView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'Home/user_detail.html', {'user': user,
                                                         'logged': logged})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Products.objects.get(id=pk)
        return render(request, 'Home/Product_detail.html', {'product': product,
                                                            'logged': logged,
                                                            'user_info': user_info})


class CategoryView(View):
    def get(self, request, cat):
        categories = Categories.objects.get(category=cat)
        products = Products.objects.filter(category=categories.id)
        active = [''] * 4
        active[categories.id] = 'active'

        return render(request, 'Home/Home.html', {'products': products,
                                                  'active': active,
                                                  'logged': logged,
                                                  'user_info': user_info})


def admin_user(request):
    user = User.objects.all()
    categories = Categories.objects.all()
    product = Products.objects.all()
    return render(request, 'Super/SuperUser.html', {'user': user,
                                                    'category': categories,
                                                    'product': product})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'Authorization/Register.html', {'form': form})


def registration_success(request):
    return render(request, 'Authorization/Register_success.html')


def login_success(request):
    return render(request, 'Authorization/Login_success.html')


def logout(request):
    global logged
    logged = False
    return render(request, 'Authorization/Logout.html')


def login_view(request):
    # form = LoggingForm(request.POST)
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                global logged, user_info
                # user_info = user
                user_info = User.objects.get(username=username)
                print(user_info.password)
                logged = True
                if user_info.is_staff:
                    return redirect('admin_user')
                return redirect('login_success')
            else:
                form.add_error(None, 'Invalid username or password')
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'Authorization/Login.html', {'form': form})


def upload_files(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'you are added the "' + form.cleaned_data['name'] + '" product'
            return render(request, 'Super/Upload_files.html', {'status': status})
    else:
        form = UploadForm()
    return render(request, 'Super/Upload_files.html', {'form': form})


def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get('password'):
                user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect(f'/user_details/{user_id}')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'Home/user_update.html', {'form': form,
                                                     'user': user})


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/login/')


def search_results(request):
    query = request.GET.get('q')
    if query:
        items = Products.objects.filter(Q(name__icontains=query) | Q(characteristics__icontains=query))
    else:
        items = Products.objects.all()
    return render(request, 'Home/search_results.html', {'items': items,
                                                        'logged': logged,
                                                        'user_info': user_info})
