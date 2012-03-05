Hadoop Python Indexer
=====================


A distributed web crawling and indexing tool written in python and utilizing the Hadoop streaming API.
-------------------------------------------------------------------------------------------------------

This is a work in progress of course, but is intended to provide web crawling and indexing for a search engine written entirely in python,
but using the Hadoop Streaming API for distributed processing.  This package consists of three major components:
*DistCrawler.py* is the actual crawler.  Given a URL (preferably the root page of a site) DistCrawler recursivley searches all the internal page links it finds.
DistCrawler streams back page content, and external links via standard output.

*CrawlDirector.py*
