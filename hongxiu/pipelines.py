# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import datetime
from scrapy.utils.project import get_project_settings

class HongxiuPipeline(object):
	def __init__(self):
		config = get_project_settings()
		path = config.get('HONGXIU_OUTPUT') + "." + datetime.date.today().strftime('%Y%m%d')
		self.file = codecs.open(path, 'w', encoding='utf-8')
	
	def process_item(self, item, spider):
		lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.file.write(lines)
		return item
	
	def clost_spider(self, spider):
		self.file.close()
