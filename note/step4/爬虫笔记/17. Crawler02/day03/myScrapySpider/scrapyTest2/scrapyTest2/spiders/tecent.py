# -*- coding: utf-8 -*-
#import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Scrapytest2Item

class TecentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # 种子站点的URL
    start_urls = ['https://hr.tencent.com/position.php?keywords=python&lid=2156&tid=0&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
#        i = {}
#        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
#        #i['name'] = response.xpath('//div[@id="name"]').extract()
#        #i['description'] = response.xpath('//div[@id="description"]').extract()
#        return i
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = Scrapytest2Item()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = "https://hr.tencent.com/"+each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            yield item
