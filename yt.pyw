from win10toast_click import ToastNotifier
import urllib.request
import pyperclip
import requests
import urllib
import json
import os

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

ico = os.path.join('msm_stuff', 'yt.ico')
ico = os.path.join(install_dir, ico)

start = int(language[1].split(":")[5])
# import pprint
download_dir = ""
if os.environ['userprofile'].startswith('C:'):
    download_dir = os.path.join(os.environ['userprofile'], "Pictures")
    download_dir = os.path.join(download_dir, "Youtube")
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

data = pyperclip.paste()
if 'v=' not in data:
    clipboard = language[start + 9] + '\n' + language[start + 10]
    toaster = ToastNotifier()
    toaster.show_toast(data, clipboard, icon_path=ico, duration=5)
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
            toaster.show_toast(language[start + 12], os.path.basename(title), icon_path=ico, callback_on_click=view, duration=5)
    return language[start + 11], os.path.basename(title)


def view():
    os.system(f'explorer "{download_dir}"')


output = download(os.path.join(download_dir, title_), 'maxres')
toaster = ToastNotifier()
toaster.show_toast(output[0], output[1], icon_path=ico, callback_on_click=view, duration=5)
