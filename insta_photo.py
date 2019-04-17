import requests
import os
from pprint import pprint


def fetch_image(filename, url):
	path = os.path.join(os.getcwd(), 'image')
	try:
		os.makedirs('image')
	except FileExistsError:
		pass
	response = requests.get(url)
	with open(os.path.join(path,filename), 'wb') as file:
		file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/"
    launches = requests.get(url).json()
    launches.reverse()
    for launch in launches:
        if not len(launch['links']['flickr_images']) == 0:
            image_urls = launch['links']['flickr_images']
            break
    for image_number, image_url in enumerate(image_urls):
        fetch_image(f'spacex{image_number}.jpg', image_url)


def get_file_extension(url):
    return os.path.splitext(url.split('/')[-1])[1]


def fetch_hubble_image_by_id(id, prefix=''):
    hubble_url = 'http://hubblesite.org/api/v3/image/'
    response = requests.get(f'{hubble_url}{id}').json()
    hubble_images_urls = [param['file_url'] for param in response['image_files']]
    extension = get_file_extension(hubble_images_urls[0])
    fetch_image(f'hubble{prefix}{extension}', hubble_images_urls[-1])


def fetch_hubble_collection(collection):
    hubble_collections_url = 'http://hubblesite.org/api/v3/images/'
    response = requests.get(f'{hubble_collections_url}{collection}').json()
    collection_images_id = [image['id'] for image in response]
    for prefix, image_id in enumerate(collection_images_id):
        fetch_hubble_image_by_id(image_id, f'_{collection}_{prefix}')


if __name__ == '__main__':
    collection = 'holiday_cards'
    fetch_hubble_collection(collection)
