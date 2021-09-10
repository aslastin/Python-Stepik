import re
import requests


def get_urls(url):
    r = requests.get(url)
    return set(re.findall(r'<a [^>]*?href="(.+?)"[^>]*?>', r.text))


ua, ub = input(), input()
for link in get_urls(ua):
    if ub in get_urls(link):
        print('Yes')
        break
else:
    print('No')
