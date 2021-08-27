from win10toast_click import ToastNotifier
import urllib.request
import pyperclip
import requests
import urllib
import json
import os

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
# import pprint
if not os.path.exists(f"{os.environ['userprofile']}\\Pictures\\YouTube\\"):
    os.mkdir(f"{os.environ['userprofile']}\\Pictures\\YouTube\\")

data = pyperclip.paste()
if 'v=' not in data:
    clipboard = language[start + 9] + '\n' + language[start + 10]
    toaster = ToastNotifier()
    toaster.show_toast(data, clipboard, icon_path="C:\\Yosh\\msm_stuff\\gal.ico", duration=5)
    exit(0)

VideoID = data.split('v=')[-1]
VideoID = VideoID.split('&')[0]

params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
url = "https://www.youtube.com/oembed"
query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string

with urllib.request.urlopen(url) as response:
    response_text = response.read()
    data = json.loads(response_text.decode())
    # pprint.pprint(data)
    # print(data['title'])
title_ = data['title']

# vid = requests.get(data)
# vid_data = vid.content.split(b'<title>')[1]
# print(vid_data[:80])
# vid_data = vid_data.split(b'</title>')[0]
# print(vid_data[:80])
# title_ = str(vid_data)[2:-1]  # removes b' '
for character in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
    title_ = title_.replace(character, '')  # forbidden characters by windows


# https://i.ytimg.com/vi/ynf7CoXssTE/maxresdefault.jpg
def download(title, res):
    wallpaper = requests.get(f'https://img.youtube.com/vi/{VideoID}/{res}default.jpg')
    i = 1
    if os.path.exists(f'{title}.jpg'):
        while os.path.exists(f'{title}-{i}.jpg'):
            i += 1
        title = f'{title}-{i}'
    with open(f'{title}.jpg', 'wb') as jpg:
        jpg.write(wallpaper.content)
    if wallpaper.content == b'':
        if res == 'maxres':
            download(title, 'sd')
        if res == 'sd':
            download(title, 'hq')
        if res == 'hq':
            download(title, 'mq')
        if res == 'mq':
            toaster = ToastNotifier()
            toaster.show_toast(language[start + 12], title.split('\\')[-1], icon_path="C:\\Yosh\\msm_stuff\\gal.ico", callback_on_click=view, duration=5)
    return language[start + 11], title.split('\\')[-1]


def view():
    os.system(f'explorer "{os.environ["userprofile"]}\\Pictures\\YouTube\\"')


output = download(f"{os.environ['userprofile']}\\Pictures\\YouTube\\{title_}", 'maxres')
toaster = ToastNotifier()
toaster.show_toast(output[0], output[1], icon_path="C:\\Yosh\\msm_stuff\\gal.ico", callback_on_click=view, duration=5)
