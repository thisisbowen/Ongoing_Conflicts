from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.request import urlopen
import pandas as pd
import requests
import lxml
import csv
import re

my_url ='https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts'
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")

with open('event_sourcing.csv', 'w', encoding='UTF-8', newline='') as fd:
    writer = csv.writer(fd)
    writer.writerow(["Start of conflict", "Conflict", "Continent",
                  "Country", "Cumulative fatalities",
                  "Fatalities in 2017", "Fatalities in 2018"])

    containers = page_soup.find("table",{"id":"conflicts10000"}).tbody.findAll("tr")[1:]
    for container in containers:
        fish = container.findAll("td")
        row = []
        for fish_soup in fish:
            row.append(re.sub("[\(\[].*?[\)\]]", "",fish_soup.text.split('\n')[0].replace('–','-').replace('\xa0','',1).replace('\xa0','&').strip()))
        writer.writerow(row)

    containers = page_soup.find("table",{"id":"conflicts1000"}).tbody.findAll("tr")[1:]
    for container in containers:
        fish = container.findAll("td")
        row = []
        for fish_soup in fish:
            row.append(re.sub("[\(\[].*?[\)\]]", "",fish_soup.text.split('\n')[0].replace('–','-').replace('\xa0','',1).replace('\xa0','&').strip()))
        writer.writerow(row)

    containers = page_soup.find("table",{"id":"conflicts100"}).tbody.findAll("tr")[1:]
    for container in containers:
        fish = container.findAll("td")
        row = []
        for fish_soup in fish:
            row.append(re.sub("[\(\[].*?[\)\]]", "",fish_soup.text.split('\n')[0].replace('–','-').replace('\xa0','',1).replace('\xa0','&').strip()))
        writer.writerow(row)
        
    containers = page_soup.find("table",{"id":"conflicts1"}).tbody.findAll("tr")[1:]
    for container in containers:
        fish = container.findAll("td")
        row = []
        for fish_soup in fish:
            row.append(re.sub("[\(\[].*?[\)\]]", "",fish_soup.text.split('\n')[0].replace('–','-').replace('\xa0','',1).replace('\xa0','&').strip()))
        writer.writerow(row)