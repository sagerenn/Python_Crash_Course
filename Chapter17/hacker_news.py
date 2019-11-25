import requests
import json
from operator import itemgetter
import os

os.chdir(os.path.dirname(__file__))

top_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080",
}


top_response = requests.get(top_url, proxies=proxies)
if top_response.status_code == 200:
    top_response_list = top_response.json()

submission_dicts, titles, urls, comments = [], [], [], []
for top in top_response_list[:10]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(top) + '.json'
    r = requests.get(url, proxies=proxies)
    data = r.json()
    print(r.status_code)
    submission_dict = {
        'title': data['title'],
        'link': data['url'],
        'comments': data['descendants'],
    }
    titles.append(data['title'])
    urls.append(f"<a href='{data['url']}'>{data['title']}</a>")
    comments.append(data['descendants'])
    submission_dicts.append(submission_dict)

submission_dicts.sort(key=itemgetter('comments'), reverse=True)


# for submission_dict in submission_dicts:
#     for key,values in submission_dict.items():
#         print(f"{key}: {values}")

from plotly.graph_objs import Bar
from plotly import offline

data = {
    'type': 'bar',
    'x': urls,
    'y': comments,
}

my_layout = {
    'title': 'Most active submission'
}

fig = {
    'data': data,
    'layout': my_layout
}

offline.plot(fig, filename='test.html')

