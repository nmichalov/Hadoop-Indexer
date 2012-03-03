#!/usr/bin/env python

import os
import re
import sys
import cPickle


class DataReduce:

    def __init__(self):
        self.unique_urls = []
        self.data_dir = '%s/%s' % (os.getcwd(), 'CrawlData')
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)

    def reduce_data(self, crawl_data):
        if crawl_data.startswith('Content#'):
            crawl_data = crawl_data.split('#')
            print crawl_data[2]
            url_file = re.sub('\/', ' ', crawl_data[1])
            out_file = '%s/%s' % (self.data_dir, url_file)
            content_file = open(out_file, 'a')
            content_file.write(crawl_data[2]+' ')
            content_file.close()
        else:
            if crawl_data not in self.unique_urls:
                self.unique_urls.append(crawl_data)

    def return_urls(self):
            url_file = open('URLlist', 'a')
            for url in self.unique_urls:
                url_file.write(url+'\n')
            url_file.close()

if __name__ == '__main__':
    datareduce = DataReduce()
    for line in sys.stdin:
        line = line.strip()
        datareduce.reduce_data(line)
    datareduce.return_urls()
