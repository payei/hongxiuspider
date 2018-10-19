# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HongxiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	url = scrapy.Field()		#原文url
	origin = scrapy.Field()		#来源，如潇湘、起点等
	cat = scrapy.Field()		#作品类别
	level = scrapy.Field()		#作品等级
	workState = scrapy.Field()  #连载中 or 已完结
	isDeal =scrapy.Field()		#是否签约
	vip = scrapy.Field()		#是否vip
	length = scrapy.Field()		#字数，单位万
	commentCount = scrapy.Field()	#评论数
	pvCount = scrapy.Field()		#点击量
	likeCount = scrapy.Field()		#收藏量
	chapterCount = scrapy.Field()	#章节数
	descript = scrapy.Field()		#简介
	tags = scrapy.Field()			#标签,数组
	updateAt = scrapy.Field()		#更新时间，潇湘：date格式，红袖：多久前

	pass
