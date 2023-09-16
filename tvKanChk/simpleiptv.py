import http.client
from urllib.request import Request, urlopen
from urllib.error import URLError
import m3u8
import requests

from ipytv import playlist


class RequestsClient():
    def download(self, uri, timeout=None, headers={}, verify_ssl=True):
        o = requests.get(uri, timeout=timeout, headers=headers)
        return o.text, o.url


# url = "https://iptv-org.github.io/iptv/categories/classic.m3u"
#url = "https://gitlab.com/ambagasdowa/notes/-/raw/master/src/Development/iptv.m3u"
url = "https://github.com/ambagasdowa/m3u/raw/main/mylist.m3u8"
# url =
pl = playlist.loadu(url)
print(pl.length())
attributes = pl.get_attributes()
for k, v in attributes.items():
    print(f'"{k}": "{v}"')

for channel in pl:
    print(f'channel \"{channel.name}\": {channel.url}')
    try:
        response = urlopen(Request(channel.url))
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        print('everything is fine')
    # m3u8 lib
        playlist = m3u8.load(channel.url, http_client=RequestsClient())
        print(playlist.dumps())


#host = "http://190.171.101.36/HBO/tracks-v4a2/mono.m3u8"
#host = "https://github.com/ambagasdowa/m3u/raw/main/mylist.m3u8"
#host = "https://gitlab.com/ambagasdowa/notes/-/raw/master/src/Development/iptv.m3u"
#someurl = url = host
#port = 8080


# playlist = m3u8.load(host, http_client=RequestsClient())
# print(playlist.dumps())
