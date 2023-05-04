# if __name__ ==  "__main__":
import os.path
import time
from os.path import basename
from bs4 import BeautifulSoup, Tag
import requests
from collections import defaultdict

# url = "https://alfa.kz/phones/telefony-i-smartfony/2155-android" #1
# url = "https://alfa.kz/electronics/headphone/sort-cnfrmd_price-desc#products" #2


# url = "https://alfa.kz/phones/telefony-i-smartfony" #1
# url = "https://alfa.kz/electronics/headphone" #2
url = "https://alfa.kz/pc/notebooks" #3

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

products = doc.find_all('div', {'class': 'product-item'})
parsed_data = []
products = products[:5]
for product in products:
    image = ''
    name = product.find('span', {'itemprop': 'name'}).text.strip()
    price = product.find('span', {'class': 'num'}).text.strip()
    url_to_product = product.find('div', {'class': 'title'}).find('a')['href'].strip()

    parsed_data.append({
        'image': image,
        'manufacturer': '',
        'name': name,
        'price': price,
        'description': '',
        'url_to_product': url_to_product,
        'category': 2
    })
# for i in range(len(parsed_data)):
#     for k, v in parsed_data[i].items():
#         print(k, v)

for product in parsed_data:
    request = requests.get(product['url_to_product'])
    bs = BeautifulSoup(request.text, 'html.parser')
    description = bs.find('div', {'class': 'excerpt'}).text.strip()
    image1 = bs.find(class_='item').find('img')['data-src']
    for i in product['name']:
        if i != ' ':
            product['manufacturer'] += i
        else:
            break
    product['image'] = "images/2023/"+basename(image1)
    product['description'] = description
    print(product['image'])

    img_data = requests.get(image1).content
    with open(os.path.join(r"C:\Users\yedyg\PycharmProjects\monyedi\media\images\2023", basename(image1)), 'wb') as handler:
        handler.write(img_data)

    print(product['description'])
    print(product['manufacturer'])
    time.sleep(2)

# products = doc.find_all(class_="num")
# name = doc.find_all(itemprop="name")
#
# for i in range(len(products)):
#     print(products[i].string)
#     name[i] = name[i].string.strip()
#     print(name[i])
#
#     ans = 0
#     for j in range(len(name[i])):
#         name[i] = list(name[i])
#         # print(name[i])
#         if name[i][j] == ' ' and ans == 0:
#             ans+=1
#             continue
#         elif (name[i][j] == '/' or name[i][j] == ' ') and ans <= 4:
#             ans += 1
#             name[i][j] = '_'
#     name[i] = "".join(name[i])
#     name[i] = name[i].split(' ')
#
#     url = "https://alfa.kz/phones/telefony-i-smartfony/" + name[i][0] + "/" + name[i][1]
#     url1 = doc.find('a')
#     # if url in url1:
#     #     url = url1
#     print(url1)
#
#     # print(doc1.prettify())

# import os
# import django
# from app.models import Products
# from bs4 import BeautifulSoup
# import requests
#
# products = Products.objects.all()
# for product in products:
#     url = product.url
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(url)
#
#     # product.price = soup.find('span', {'class': 'num'}).text.strip()
#     # product.save()

