# encoding:utf-8


from scrapy.spiders import CrawlSpider
import scrapy
import re
import logging
from hongxiu.items import HongxiuItem 

class xiaoxiangSpider(scrapy.Spider):
	name = "xiaoxiangSpider"
	#allowed_domains = ['https://www.xiaoxiang.com']

	def start_requests(self):
		start_urls = []
		for i in range(1, 1500):
			url = "http://www.xxsy.net/search?s_wd=&s_type=1&sort=9&pn=%d"%i
			url = scrapy.Request(url)
			start_urls.append(url)
			
			url = "http://www.xxsy.net/search?s_wd=&s_type=2&sort=9&pn=%d"%i
			url = scrapy.Request(url)
			start_urls.append(url)

			url = "http://www.xxsy.net/search?s_wd=&s_type=6&sort=9&pn=%d"%i
			url = scrapy.Request(url)
			start_urls.append(url)
		return start_urls

	def parse(self, response):
		self.logger.info('start xiaoxiang parse, url:%s', response.url)
		list = response.xpath("/html/body/div[3]/div/div/div[1]/div[2]/div[2]/ul/li[*]/div/h4/a/@href").extract()
		for path in list:
			url = response.urljoin(path)
			yield scrapy.Request(url, callback=self.parseDetail)
	
	def parseDetail(self, response):
		self.logger.info('start xiaoxiang detail, url:%s', response.url)
		item = HongxiuItem()
		item['origin'] = 'xiaoxiang'
		item['url'] = response.url
		item['title'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/div[1]/h1/text()").extract_first()
		item['author'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/div[1]/span/a/text()").extract_first()
		item['length'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/p[2]/span[1]/em/text()").extract_first()
		item['likeCount'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/p[2]/span[3]/em/text()").extract_first()
		item['pvCount'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/p[2]/span[2]/em/text()").extract_first()
		item['tags'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/p[3]/a/text()").extract()
		item['descript'] = response.xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[1]/dl/dd/p/text()").extract()
		item['vip'] = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/div[2]/p[2]/text()").extract_first()
		item['updateAt'] = max(response.xpath("/html/body/div[3]/div/div[1]/dl/dd/div[2]/p/span/text()").extract())
		(item['isDeal'], item['workState'], item['cat']) = response.xpath("/html/body/div[3]/div/div[1]/dl/dd/p[1]/span/text()").extract()
		yield item

