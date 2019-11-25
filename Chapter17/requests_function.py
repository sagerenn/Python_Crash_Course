import requests

def github_api():
    """request the github api"""
    url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
    r = requests.get(url)
    return r
