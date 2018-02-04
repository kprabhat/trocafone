# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

#from troca.items import TrocaItem

class TrocafoneSpider(scrapy.Spider):
    name = 'trocafone'
    allowed_domains = ['trocafone.com']
    start_urls = ['https://www.trocafone.com/vender']

            
    def parse(self, response):
        categories = Selector(response).xpath('//h3/strong/text()').extract()
        url = Selector(response).xpath('//a[@class = "epurchase-selection-box"]/@href').extract()
        
        
        for links in url:
            yield Request(links, callback = self.parseA)
            
        '''
        for item in zip(categories, url):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Categories' : item[0],
                'url' : item[1]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
        '''
            
    def parseA(self, response):
        model = Selector(response).xpath('//h3/strong/text()').extract()
        url = Selector(response).xpath('//a[@class = "epurchase-selection-box"]/@href').extract()
        
        
        for links in url:
            yield Request(links, callback = self.parseB)
        '''
        for item in zip(model, url):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Model' : item[0],
                'url' : item[1]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
        '''    
            
    def parseB(self, response):
        Model_name = Selector(response).xpath('//h3/strong/text()').extract()
        url = Selector(response).xpath('//a[@class = "epurchase-selection-box select-version-box"]/@href').extract()
        
        
        for links in url:
            yield Request(links, callback = self.parseC)        
        
        '''
        for item in zip(Model_name, url):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Model_Name' : item[0],
                'url' : item[1]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
         '''   
            
    def parseC(self, response):
        Model_Name = Selector(response).xpath('//h2/strong/text()').extract()
        
        pattern = r'"id"\:3\,"price"\:"(\w+)"'
        Prices = Selector(response).xpath('//script[@type = "text/javascript"]').re(pattern) 
        
        url = Selector(response).xpath('//meta[@property = "og:url"]/@content').extract()
        
        
        for item in zip(Prices, url, Model_Name):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Model_Name' : item[2],
                'url' : item[1],
                'Prices' : item[0]
            }
    
            #yield or give the scraped info to scrapy
            yield scraped_info
            
            
