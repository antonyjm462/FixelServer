import requests
import convert
import re

r = requests.get(url='https://us-central1-fixel-project.cloudfunctions.net/getUser');
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
