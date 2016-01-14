#!/usr/bin/python
import requests
import json
import sys

#curl -i "https://api.github.com/repos/CTreffOS/codingchaos-2015/pulls?access_token=829cc1d9b30d0c1c8aca5f4d425c035c4bed17dd"

url = 'https://api.github.com/repos/{}/{}/pulls?access_token=829cc1d9b30d0c1c8aca5f4d425c035c4bed17dd'.format(sys.argv[1],sys.argv[2])
resp = json.loads(requests.get(url).text)

for r in resp:
    print u"{:>5} {:>17}  {:.54}".format(r["number"],r["user"]["login"],r["body"].replace('\n','').replace('\r',''))
