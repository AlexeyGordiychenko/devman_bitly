import os
import requests
from urllib.parse import urlparse
import argparse


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'long_url': url}
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                             headers=headers,
                             json=params)
    response.raise_for_status()
    return response.json().get('link')


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    bitlink = '{uri.netloc}{uri.path}'.format(uri=urlparse(url))
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
        headers=headers)
    response.raise_for_status()
    return response.json().get('total_clicks')


def is_bitlink(url, token):
    bitlink = '{uri.netloc}{uri.path}'.format(uri=urlparse(url))
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}',
                            headers=headers)

    return response.ok


def main(url):
    token = os.environ['BITLY_TOKEN']
    if is_bitlink(url, token):

        try:
            bitlink = count_clicks(token, url)
            print('Clicks', bitlink)
        except requests.exceptions.HTTPError:
            print('Couldn\'t count clicks for the link')

    else:

        try:
            bitlink = shorten_link(token, url)
            print('Bitlink', bitlink)
        except requests.exceptions.HTTPError:
            print('Couldn\'t create a bitlink')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Shorten the given URL or count clicks if the given URL is a short URL')
    parser.add_argument('link', help='link')
    args = parser.parse_args()
    main(args.link)
