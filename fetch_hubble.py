import requests
import os
from fetch_spacex import fetch_image
from pprint import pprint
import argparse



def create_parser():
    parser = argparse.ArgumentParser(
        description='Program fetches images from distinct collection of hubblesite.org'
        'also gets collections names')
    parser.add_argument('-c', '--collections', action='store_true')
    parser.add_argument('-i', '--images')
    return parser


def get_file_extension(url):
    return os.path.splitext(url.split('/')[-1])[1]


def fetch_hubble_image_by_id(id, prefix=''):
    hubble_url = 'http://hubblesite.org/api/v3/image/'
    response = requests.get(f'{hubble_url}{id}').json()
    hubble_images_urls = [param['file_url'] for param in response['image_files']]
    extension = get_file_extension(hubble_images_urls[-1])
    try:
        fetch_image(f'hubble{prefix}{extension}', hubble_images_urls[-1])
    except requests.exceptions.HTTPError:
        print('An error occured while fetching image')


def get_collections_list():
    url = 'http://hubblesite.org/api/v3/images/all'
    params = {
        'page': 'all'
    }
    response = requests.get(url, params)
    return list(set([image['collection'] for image in response.json()]))


if __name__ == '__main__':
    parser = create_parser()
    args_namespace = parser.parse_args()
    if args_namespace.collections:
        for collection in get_collections_list():
            print(collection)
    elif args_namespace.images:
        hubble_collections_url = 'http://hubblesite.org/api/v3/images/'
        response = requests.get(
                f'{hubble_collections_url}{args_namespace.images}')
        if response.json():
            collection_images_id = [image['id'] for image in response.json()]
            for prefix, image_id in enumerate(collection_images_id):
                image_name = f'_{args_namespace.images}_{prefix}'
                print(f'fetching {image_name} ...')
                fetch_hubble_image_by_id(image_id, image_name)
                print('done')
        else:
            print('Warning!\nReturned empty response.\n'
                  'Possibly collection with name: '
                  f'{args_namespace.images} doesnt exist')

    else:
        print('You must input args')
