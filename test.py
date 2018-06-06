import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
kitten = response.read()
with open('cat_img.jpg','wb') as f:
	f.write(kitten)