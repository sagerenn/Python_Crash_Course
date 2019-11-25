import requests
import json
import time
import os 

os.chdir(os.path.dirname(__file__))

limit_response = requests.get('https://api.github.com/rate_limit')
limit_dict = limit_response.json()

if limit_dict['resources']['search']['remaining'] == 0:
    print(f"Please wait \
        {limit_dict['resources']['search']['reset'] - int(time.time())} \
        seconds until the limit reset!")
    exit(1)

print(limit_dict['resources']['search']['remaining'])

# make an api all and store the response
url = 'https://api.github.com/search/repositories?q=language:go&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# print(f"Total repositories: {response_dict['total_count']}")
# print(len(response_dict['items']))
# print(json.dumps(response_dict['items'][0], indent=4))
# # Process results
# print(f"Keys per items: {len(response_dict['items'][0])}")
# print(response_dict.keys())

urls, stars, names, labels = [], [], [], []

# print("\nSelected information about each repository: ")
for repo_dict in response_dict['items']:
    # print(f"\nName: {repo_dict['name']}")
    # print(f"Owner: {repo_dict['owner']['login']}")
    # print(f"Stars: {repo_dict['stargazers_count']}")
    # print(f"Repository: {repo_dict['html_url']}")
    # print(f"Description: {repo_dict['description']}")
    urls.append(repo_dict['html_url'])
    stars.append(repo_dict['stargazers_count'])
    names.append(f"<a href='{repo_dict['html_url']}' >{repo_dict['name']}</a>")
    labels.append(f"{repo_dict['owner']['login']} <br /> \
        {repo_dict['description']}")

from plotly.graph_objs import Bar
from plotly import offline

data = [{
    'type': 'bar',
    'y': stars,
    'x': names,
    'text': urls,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25, 25, 25)',
        },
    'opacity': 0.6,
    },
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {
        'size': 28,
    },
    'xaxis': {
        'title': 'Repository',
        'titlefont': {
            'size': 24,
        },
        'tickfont':{
            'size': 14,
        },
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {
            'size': 24,
        },
        'tickfont':{
            'size': 14,
        },
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='test.html')

