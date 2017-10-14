# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address1 = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
address2 = 'http://py4e-data.dr-chuck.net/known_by_Ivan.html'

count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
	html = urllib.request.urlopen(address2, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	number = 0
	for tag in tags:
		number += 1
		if number == position:
			address2 = tag.get('href', None)
			if i == position:
				print(tag.contents[0])
			break







# links = []
# for tag in tags:
# 	links.append(tag.get('href', None))
# url = links[position-1]




# n = 0
# x = 0

# while n < count:
# 	html = urllib.request.urlopen(address1, context=ctx).read()
# 	soup = BeautifulSoup(html, 'html.parser')
# 	tags = soup('a')

# 	for tag in tags:
# 		x += 1
# 		if x == position:
# 			address1 = tag.get('href', None)
# 			print(address1)
# 			break
# 	n += 1







# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# count = int(input("Enter count: "))
# position = int(input("Enter position: "))

# names = []

# while count > 0:
# 	soup = BeautifulSoup(html, 'html.parser')
# 	tags = soup('a')
# 	name = tags[position-1]
# 	names.append(name)
# 	html = tags[position-1]['href']
# 	count -= 1

# print(names[-1])


# for x in range(count):
# 	soup = BeautifulSoup(html, 'html.parser')
# 	tags = soup('a')
	# for tag in tags:
	# 	name = tag[position]
	# 	names.append(name)
	# 	names.append(tag.get('href', None))


# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# count = int(input("Enter count: "))
# position = int(input("Enter position: "))

# names = []
# url = urllib.request.urlopen(names[position - 1], context = ctx).read()

# for x in range(count):
# 	names = []
# 	html = urlib.request.urlopen(url, context=ctx).read()
# 	soup = BeautifulSoup(html, 'html.parser')
# 	tags = soup('a')
# 	for tag in tags:
# 		names.append(tag.get('href', None))