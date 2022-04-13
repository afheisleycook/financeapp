import typing
import os
import ipaddress
import re
import requests
from bs4 import BeautifulSoup
ipvery = re.compile("\d\d\d.\d\d\d.\d\d\d.\d.\d\d\d")
data = requests.get("http://192.168.1.254/cgi-bin/devices.ha")
soup = BeautifulSoup(data.text,"html.parser")
for table in soup:
    with open("data.txt","a") as t:
        t.write(table.text)

