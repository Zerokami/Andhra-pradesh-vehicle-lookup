#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import urllib
import time
import sys

BASE_URL = "https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx" # The link from which the results are scraped.

HEADERS = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'} # The headers required for the request. Without this the target website doesn't give the details.

def clean_input(input_no):
    return(input_no.replace(" ", ""))

def get_data(vehicle_no, table=False):

    reqs = requests.session()
    text_req = reqs.get(BASE_URL,headers=HEADERS).text

    soup = BeautifulSoup(text_req)
    #print(soup.prettify)

    #print(soup.find(attrs={'id': "__VIEWSTATE"}))
    hidden_value = soup.find(attrs={'id':"__VIEWSTATE"}).attrs.get('value')
    #print(hidden_value)

    params = urllib.urlencode({'__VIEWSTATE': hidden_value, 'ctl00$OnlineContent$btnGetData':"Get Data","ctl00$OnlineContent$txtInput": vehicle_no, "ct0":"R"})

    final_html = reqs.post(BASE_URL, headers=HEADERS, data=params).text

    final_soup = BeautifulSoup(final_html)
    #print(final_soup.prettify)

    #print(final_soup.find(attrs={'id':'ctl00_OnlineContent_tdOwner'}).text)
    
    if table == True:
        return(final_soup.find(attrs={'id':'ctl00_OnlineContent_tblData'}))
    else:
        return(final_soup.find(attrs={'id':'ctl00_OnlineContent_tblData'})).text

def add_zeros(length, in_value):
    zeros =  "0"*(length-len(in_value))
    return(zeros+in_value)

def clean_newlines(text):
    text = text.replace("\n"*3, "\n")
    return(text)

if __name__ == "__main__":
    #print(get_data("AP36Q2709"))
    print(get_data(sys.argv[1]))


"""
To do:

Proxy,
Logging,
Add sys.arg(1) or sys.argv(0) or whatever.


"""
