import requests
import os


def fetch_image(filename, url):
	path = os.path.join(os.getcwd(), 'image')
	os.makedirs('image', exist_ok=True)
	response = requests.get(url)
	if response.ok:
		with open(os.path.join(path,filename), 'wb') as file:
			file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/"
    launches = requests.get(url).json()
    launches.reverse()
    for launch in launches:
        if launch['links']['flickr_images']:
            image_urls = launch['links']['flickr_images']
            break
    for image_number, image_url in enumerate(image_urls):
        print(f'fetching spacex{image_number}.jpg ...')
        fetch_image(f'spacex{image_number}.jpg', image_url)
        print('done')


if __name__ == '__main__':
    fetch_spacex_last_launch()
