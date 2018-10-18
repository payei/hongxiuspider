# encoding:utf-8

from scrapy.spiders import CrawlSpider
import scrapy
import re
#from bs4 import BeautifulSoup
from hongxiu.items import HongxiuItem 

class hongxiuSpider(scrapy.Spider):
	name = "hongxiuSpider"
	#allowed_domains = ['https://www.hongxiu.com']

	def start_requests(self):
		start_urls = []
		for i in range(1, 2):
			url = "https://www.hongxiu.com/all?&pageSize=10&gender=2&catId=30020&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=%d"%i
			url = scrapy.Request(url)
			start_urls.append(url)
		return start_urls

	def parse(self, response):
		print "start crawling"
		for one in response.xpath('//html/body/div/div[2]/div[2]/div[2]/div[1]/ul/li'):
			path = one.xpath('div[2]/h3/a/@href').extract_first()
			url = response.urljoin(path)
			yield scrapy.Request(url, callback=self.parseDetail)
	
	def parseDetail(self, response):
		print "start detail"
		item = HongxiuItem()
		item['title'] = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/h1/em/text()").extract_first()
		item['author'] = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/h1/a/text()").extract_first()
		item['url'] = response.url
		item['length'] = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/p[2]/span[1]/text()").extract_first()
		item['likeCount'] = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/p[2]/span[2]/text()").extract_first()
		item['pvCount'] = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/p[2]/span[3]/text()").extract_first()
		item['descript'] = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/p[3]/text()").extract()
		item['chapterCount'] = response.xpath('//*[@id="J-catalogCount"]/text()').extract_first()
		item['level'] = response.xpath("//i[@class='red']/text()").extract_first()
		item['vip'] = response.xpath("//i[@class='org']/text()").extract_first()
		(item['workState'],item['isDeal']) = response.xpath("//i[@class='blue']/text()").extract()
		item['cat'] = [];

		#包括作品等级、是否完结、是否签约、是否vip、类型类别
		ilist = response.xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/p[1]/span/i")
		for one in ilist:
			color = one.xpath("@class").extract_first()
			print color
			if not color:
				item['cat'].append(one.xpath("text()").extract_first())

		yield item

