import requests
import convert
import re

URL = 'https://us-central1-fixel-project.cloudfunctions.net/getUser';
r = requests.get(url=);
s = r.json();
user = s['data'];
x = 'https://us-central1-fixel-project.cloudfunctions.net/getData?data={"user":"' + user + '"}';

y = requests.get(url=x);

z = y.json();

data = z['data'];

data = data[0];
data = data.split(',');

img_data = data[1];


img_type = data[0];
img_data = str.encode(img_data);


convert.conv64(img_data,img_type);

if __name__=="main":
  main()
