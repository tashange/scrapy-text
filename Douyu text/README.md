# Douyu
该项目基于scrapy框架
主要修改了settings.py items.py pipelines.py douyu.py文件
安装：
1.直接用集成包进行安装：百度搜索Miniconda，选择对应版本进行安装；一路next
安装完成后cmd窗口用：conda list 命令检验是否成功安装。
2.若安装不成功，可能是路径没有配置正确。
3.使用命令：conda install -c conda-forge scrapy 安装scrapy框架
使用scrapy：
1.新建项目
命令：scrapy startproject ITcast(项目名)
注：settings.py 配置文件(用于开启管道)  items.py需要爬取的字段 
pipelines.py管道文件 spiders文件夹下存放的是爬虫脚本
2.新建爬虫
命令：scrapy genspider itcast (文件名) “http://www.itcast.cn”(爬取的范围)
注：只要在该项目文件下创建就可以，文件会自动创建在spiders文件夹下
3.执行爬虫的命令：
Scrapy crawl itcast(爬虫名，对应爬虫代码中的name参数)
4.使用媒体管道需要有PIL组件的支持，使用Miniconda安装没有该组件，需要手动安装
安装pillow命令：pip install pillow