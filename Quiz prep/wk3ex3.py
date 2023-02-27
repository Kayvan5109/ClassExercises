import requests
import json
# you will get this from your reddit app
auth = requests.auth.HTTPBasicAuth('diabeto270', 'v5HZvnUZ6xTO--7PY4FQce7vZqsnZg'
)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'diabeto270',
        'password': 'Sharp206'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'scraper/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
# print(res.json())

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
# res = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

# get 5 new posts from wallstreetbets
params = {'limit': 5}
res = requests.get("https://oauth.reddit.com/r/wallstreetbets/new", headers=headers, params=params)
print(res.json())



## ALTERNATIVE WAY ##

import requests

def get_comments(subreddit):
    url = f"https://www.reddit.com/r/movies/comments.json"
    headers = {
        "User-Agent": "My Reddit API Client/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        comments = response.json()["data"]["children"]
        return [comment["data"]["body"] for comment in comments]
    else:
        return None

comments = get_comments("movies")

if comments:
    print("Latest comments from r/movies:")
    for comment in comments[:10]:
        print(f"- {comment}")
else:
    print("Failed to retrieve comments.")