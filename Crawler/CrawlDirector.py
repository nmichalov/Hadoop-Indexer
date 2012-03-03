#!/usr/bin/env python

import sys
import Pyro4
import os
import cPickle
from DistCrawler import Crawler 

class Director:
    
    def __init__(self):
        self.target_urls = []
        self.visited_urls = []

    def add_new(self, url_list):
        for url in url_list:
            if url not in self.visited_urls:
                self.target_urls.append(url)
        
    def new_urls(self):
        return self.target_urls

    def update_record(self):
        self.visited_urls.append(self.target_urls)
        self.target_urls = []

def main():
    urls = []
    url_file = open('URLlist', 'r')
    for line in url_file:
        urls.append(line.strip())
    url_file.close()
    director.add_new(urls)
    target_urls = director.new_urls()
    crawler = Crawler()
    for link in target_urls:
        crawler.crawl(link)

if __name__ == "__main__":
    director = Director()
    main()

