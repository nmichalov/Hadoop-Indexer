Hadoop Python Indexer
=====================


**A distributed web crawling and indexing tool written in python and utilizing the Hadoop streaming API.**


This is a work in progress of course, but is intended to provide web crawling and indexing for a search engine written entirely in python,
but using the Hadoop Streaming API for distributed processing.  This package consists of three major components:

*DistCrawler.py* is the actual crawler.  Given a URL (preferably the root page of a site) DistCrawler recursivley searches all the internal page links it finds.
DistCrawler streams back page content, and external links via standard output.

*CrawlDirector.py* manages the list of visited URLs and the target URLs for each crawl batch.  It gathers target URLs from a text file called URLlist,
and saves visited URLs in a serialized list.

*DataReduce.py* Specifies how to save the links and content streamed back from the crawler(s).

*ProcContent.py* uses, a python package for document modeling, to generate a topic model of the webpage content retrieved by the crawler.

