#!/bin/python

import requests as r
from bs4 import BeautifulSoup as bs
from pprint import pprint
import argparse
import sys

_URLS = {
        'ssgc': 'https://suigasbill.pk/view-ssgc-bill/',
        'sngpl': 'https://suigasbill.pk/view-sngpl-bill/'
        }

_DATA = { 'ref': None }

def print_tariff():
    pass

def print_types():
    print('\033[4mTYPES OF PAKISTAN SUI GAS BILLS\033[0m')
    for k,v in _URLS.items():
        print('{}: {}'.format(k, v))

def get_bill(type, number):
    _DATA['ref'] = number

    if type not in _URLS.keys(): raise Exception('Unknown bill type.')

    import ipdb; ipdb.set_trace()
    res = r.post(_URLS.get(type), _DATA)
    if res.ok:
        html = bs(res.content, 'html.parser')
        bill = html.find("div", {"class": "thebill"})
    else:
        print('nay!')
        bill = None

    return bill

def bill_to_json(bill):
    bill_json = {}
    
    all_divs = bill.find_all('div')

    if len(all_divs) < 2: raise Exception("No bills found. Please try again!")
    for i in range(1, 20, 3):
        f = all_divs[i].text.strip()[:-1].lower()
        v = all_divs[i+1].text.strip().upper()
        #print(i, f, i+1, v, '--')
        bill_json.update({f:v})
    
    return bill_json

def print_bill(bill):
    #print(bill)
    print('\033[4mCUSTOMER: ', bill.get('name'), '\033[0m')
    del bill['name']
    for k,v in bill.items():
        print('\t', k.upper().strip(),': ', v)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Pakistan Sui Gas Bills and Tariff.')
    parser.add_argument('-t', '--tariff', required=False, action='store_true', help='Show tariff.')
    parser.add_argument('-b', '--bill_types', required=False, action='store_true', help='Show bill types.')
    parser.add_argument('-c', '--check_bill', required=False, dest='bill_type', metavar='T', help='Check bill type.')
    parser.add_argument('-n', '--consumer_number', required=False, dest='bill_no', metavar='N', help='Specify the bill/customer number.')
    a = parser.parse_args()

    print('\n')

    if a.bill_type:
        bill = get_bill(a.bill_type, a.bill_no)
        if not bill: raise Exception('Bill not found.')

        bill_json = bill_to_json(bill)
        print_bill(bill_json)
    elif a.bill_types:
        print_types()
    elif a.tariff:
        raise Exception('Not yet implemented.')


