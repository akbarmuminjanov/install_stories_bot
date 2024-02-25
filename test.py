import requests
from pprint import pprint

url = "https://instagram-story-downloader-media-downloader.p.rapidapi.com/story/index"



headers = {
	"X-RapidAPI-Key": "616a59496bmsh7a8885bb1b884e1p1cae66jsnd53897bb39ac",
	"X-RapidAPI-Host": "instagram-story-downloader-media-downloader.p.rapidapi.com"
}



def find_stories(username):
    querystring = {"url":username}
    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    return data['stories']