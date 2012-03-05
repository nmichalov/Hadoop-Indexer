#!/usr/bin/env python

import os
import re
from gensim import corpora, models, similarities

def page_text():
    for page_file in os.listdir('CrawlData'):
        content = open('CrawlData/'+page_file, 'r')
        page_text = content.read()
        content.close()
        yield page_text

class PageCorpus:
    def __iter__(self):
        for page_file in os.listdir('CrawlData'):
            content = open('CrawlData/'+page_file, 'r')
            page_text = content.read()
            content.close()
            yield dictionary.doc2bow(page_text.split())

if __name__ == '__main__':
    dictionary = corpora.Dictionary(line.split() for line in page_text())
    pc = PageCorpus()
    model = models.LdaModel(corpus = pc, id2word=dictionary, num_topics=100)#, chunksize=100, distributed=True)
    lda_corpus = model[pc]
    dictionary.save('PageDictionary.dict')
    corpora.MmCorpus.serialize('PageModel.mm', lda_corpus)
