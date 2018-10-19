# hongxiuspider
红袖添香/潇湘书院作品详细信息抓取（针对特定分类的、基于scrapy）

请先安装scrapy（https://github.com/scrapy/scrapy）

红袖执行语句：scrapy crawl hongxiuSpider
潇湘执行语句：scrapy crawl xiaoxiangSpider

样例url只对部分分类、有限页数进行了数据抓取，可自行修改spiders/hongxiuSpider.py的中的start_requests函数，实现其他分类、更多页数的抓取

抓取结果在pipeline中存储为json格式，每个作品一行，复杂存储需求请自行修改pipeline

代理请根据需求配置

