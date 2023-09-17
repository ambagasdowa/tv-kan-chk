import http.client
from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlparse

import re
import m3u8
from m3u8 import protocol
from m3u8.parser import save_segment_custom_value

import requests

import ipytv
from ipytv.playlist import M3UPlaylist
from ipytv.channel import IPTVChannel

from ipytv.doctor import M3UDoctor, M3UPlaylistDoctor
from ipytv import playlist


class RequestsClient():
    def download(self, uri, timeout=None, headers={}, verify_ssl=True):
        o = requests.get(uri, timeout=timeout, headers=headers)
        return o.text, o.url


def check_url_struct(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def save_pls(tunner):
    with open('./test/my-fixed-playlist.m3u', 'w', encoding='utf-8') as out_file:
        content = tunner.to_m3u_plus_playlist()
        out_file.write(content)


def pls_channel(result, url, error=""):
    # url = "https://github.com/ambagasdowa/m3u/raw/main/mylist.m3u8"
    print(result)
    if result:
        print(f'Checking the channels in {url} ...')
        pl = ipytv.playlist.loadu(url)
        print(f"Found {pl.length()} channels")

        tunner = ipytv.playlist.M3UPlaylist()
        # plsChannel = ipytv.channel.IPTVChannel()

        for channel in pl:
            if check_url_struct(channel.url):

                tunner.append_channel(channel)
                print(f'channel \"{channel.name}\": {channel.url} Status: OK')

                # plsLoad = m3u8.load(channel.url, http_client=RequestsClient())

                # if you want to write a file from its contenot
                # playlist_dump +=
                # plsLoad.dump(f'./test/"{channel.name}".m3u8')
                # print(plsLoad.dumps())

            # if check_url_struct(channel.url):
            #     try:
            #         response = urlopen(Request(channel.url))
            #     except URLError as e:
            #         if hasattr(e, 'reason'):
            #             print('We failed to reach a server.')
            #             print('Reason: ', e.reason)
            #         elif hasattr(e, 'code'):
            #             print('The server couldn\'t fulfill the request.')
            #             print('Error code: ', e.code)
            #     else:
            #         print('everything is fine')
    else:
        print(f'Source is offline \n Error: "{error}"')

    # print(tunner)
    save_pls(tunner)
    # pllist = m3u8.load(tunner)
    # print(pllist.dumps())

    # if you want to write a file from its content

    # playlist.dump('playlist.m3u8')
