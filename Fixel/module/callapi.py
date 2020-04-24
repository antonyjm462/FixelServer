import requests
import convert
import re

URL = 'https://us-central1-fixel-project.cloudfunctions.net/getUser'

def main():
  request_data = requests.get(url=URL).json()
  user = request_data['data'];
  POST_URL = 'https://us-central1-fixel-project.cloudfunctions.net/getData?data={"user":"' + user + '"}'
  userData = requests.get(url=POST_URL).json()
  imgs = userData['data'][0].split(',')
  img_data = str.encode(imgs[1])
  img_type = data[0];
  convert.conv64(img_data,img_type);

if __name__=="main":
  main()
