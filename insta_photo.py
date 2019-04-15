import requests
import os


filename = 'hubble.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"


def fetch_image(filename, url):
	path = os.path.join(os.getcwd(), 'image')
	try:
		os.makedirs('image')
	except FileExistsError:
		pass
	response = requests.get(url)
	with open(os.path.join(path,filename), 'wb') as file:
		file.write(response.content)


if __name__ == '__main__':
	fetch_image(filename, url)