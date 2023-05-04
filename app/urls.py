from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductView.as_view()),
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
    path('logout/', logout, name='logout'),
    path('login/', login_view, name='login'),
    path('admin_user/', admin_user, name='admin_user'),
    path('upload_files/', upload_files, name='upload_files'),
    path('user_details/<int:user_id>/', UserDetailView.as_view(), name='user_details'),
    path('user_details/<int:user_id>/user_update/', edit_user, name='user_edit'),
    path('delete_user/<int:user_id>/', delete_user, name='user_delete'),
    path('search_results/', search_results, name='search_results'),

    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<str:cat>/', CategoryView.as_view(), name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


