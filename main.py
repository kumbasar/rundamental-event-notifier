#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

event_class = 'large- small-12 columns thisWeekSession'

def checkEvent(url):
    html = requests.get(url)
    print("Status code: {}".format(html.status_code))
    html.raise_for_status()

    parsed_html = BeautifulSoup(html.text, features="lxml")
    events = parsed_html.find('div', attrs={'class': event_class}).a.get('href')

    return events
    

if __name__ == "__main__":

    event_url = 'https://rundamental.com.tr/etkinlikler'

    events = checkEvent(event_url)

    print("Event: {}".format(events))