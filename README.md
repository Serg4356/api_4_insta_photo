# DESCRIPTION
This three scripts provide functioanlity to automate fetching images from hubblesite.org, spacex and uploading them to your instagramm account. Each script locates in its own file.
# HOW TO INSTALL
Python has to be installed on your system. Use pip (or pip3 if there is conflict with Python 2) to install dependences.
```
pip install -r requirements.txt
```
It is recommended to use virtual environment virtualenv/venv to isolate your project.

# QUICKSTART

## Fetch images from spacex last launch. 
```
$python fetch_spacex.py
```

## Fetch image collection from hubblesite.org by name. This script provides simple console interface. In case you dont know wich collection to choose you can run script with -c argument, as can be seen below:
```
$python fetch_hubble.py -c
```
When you choose distinct collection, you want to fetch - run script whith -i argument and collection name after space:

```
$python fetch_hubble -i holiday_cards
```
In case you make a mistake in collection's name - you'll recieve a warning message.

## Load local images to your instagramm account
All images from folder `./image` upload to your instagramm account. Login and password must be stored in .env file in your project folder.

```
$python insta_photo.py
```

# PROJECT GOALS
Project was created for educational purposes. Training course for web-developers - [dvmn.org](https://dvmn.org)
