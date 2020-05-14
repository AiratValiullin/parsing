import requests
import json
from pprint import pprint

part = 'snippet'
video_id = 'RhMYBfF7-hE'
api_key = 'AIzaSyBSgVhzJi4sKjtcNmCfEK4_xvP41TjPKOg'
url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={api_key}'
json_url = requests.get(url)
data = json.loads(json_url.text)
pprint(data)