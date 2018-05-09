# Douyu
1.该项目基于scrapy框架
新建项目 scrapy startproject ITcast
新建爬虫 scrapy genspider itcast "itcast.cn"
测试爬虫是否能正常运行 scrapy check itcast
执行爬虫 Scrapy crawl itcast(爬虫名，对应爬虫代码中的name参数)
或：以下四种输出方式
# json格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json
# json lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonl
# csv 逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv
# xml格式
scrapy crawl itcast -o teachers.xml
XPath使用：
/html/head/title: 选择<HTML>文档中 <head> 标签内的 <title> 元素
/html/head/title/text(): 选择上面提到的 <title> 元素的文字
//td: 选择所有的 <td> 元素
//div[@class="mine"]: 选择所有具有 class="mine" 属性的 div 元素
scrapy.cfg ：项目的配置文件
mySpider/ ：项目的Python模块，将会从这里引用代码
mySpider/items.py ：项目的目标文件
mySpider/pipelines.py ：项目的管道文件
mySpider/settings.py ：项目的设置文件
mySpider/spiders/ ：存储爬虫代码目录
建议：先在ITcast项目文件夹下建一个DATA文件夹用来保存生成的数据，进入DATA文件下执行scrapy crawl ITcast命令