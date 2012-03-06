#!/usr/bin/env python

"""
Keeps track of crawled, and to be crawled, URLs by means of the URLlist text file,
and the visited_urls serialized file.  When using the hadoop streaming API, CrawlDirector serves
as the crawler map function, delegating URLs to the distributed Crawlers.
"""


import sys
import os
import cPickle
from DistCrawler import Crawler 

class Director:
    
    def __init__(self):
        self.target_urls = []
        if os.path.exists('Visited.pkl'):
           self.visited_urls = cPickle.load('Visited.pkl')
        else:
            self.visited_urls = []

    def add_new(self, url):
        if url not in self.visited_urls:
            self.target_urls.append(url)
        
    def new_urls(self):
        return self.target_urls

    def update_record(self):
        self.visited_urls.append(self.target_urls)
        visited_list = open('Visited.pkl', 'w')
        cPickle.dump(self.visited_urls, visited_list)
        visited_list.close()


def main():
    for line in sys.stdin:
        line = line.strip()
        director.add_new(line)
    target_urls = director.new_urls()
    crawler = Crawler()
    for link in target_urls:
        crawler.crawl(link)

if __name__ == "__main__":
    director = Director()
    main()
    director.update_record()

