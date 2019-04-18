import os
from dotenv import load_dotenv
from instabot import Bot



def get_images_list(path):
    images_list = []
    accepted_extensions = ['.png', '.pdf', '.jpg', '.jpeg']
    for image_name in os.listdir(path):
        if os.path.splitext(image_name)[1].lower() in accepted_extensions:
            images_list.append(image_name)
    return images_list


if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('INSTA_USER')
    password = os.getenv('INSTA_PASSWORD')
    bot = Bot()
    bot.login(username=username, password=password)
    images_list = get_images_list('./image')
    for image in images_list:
        print(f'start loading to instagramm {image}...')
        bot.upload_photo(
            os.path.join('./image', image),
            caption=os.path.splitext(image)[0])
        print('done')


