# hongxiuspider
红袖添香作品详细信息抓取（针对特定分类的、基于scrapy）

请先安装scrapy（https://github.com/scrapy/scrapy）

执行语句：scrapy crawl hongxiuSpider

分类地址如：https://www.hongxiu.com/all?pageNum=1&pageSize=10&gender=2&catId=30020&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0

样例url只抓取了“现代言情”分类下的第一页的作品，可自行修改spiders/hongxiuSpider.py的中的start_requests函数，实现其他分类、更多页数的抓取

代理请根据需求配置

简易存储可使用-o hongxiu.json参数，复杂存储需求请修改pipelines.py
