# Douyu
1.����Ŀ����scrapy���
�½���Ŀ scrapy startproject ITcast
�½����� scrapy genspider itcast "itcast.cn"
���������Ƿ����������� scrapy check itcast
ִ������ Scrapy crawl itcast(����������Ӧ��������е�name����)
���������������ʽ
# json��ʽ��Ĭ��ΪUnicode����
scrapy crawl itcast -o teachers.json
# json lines��ʽ��Ĭ��ΪUnicode����
scrapy crawl itcast -o teachers.jsonl
# csv ���ű��ʽ������Excel��
scrapy crawl itcast -o teachers.csv
# xml��ʽ
scrapy crawl itcast -o teachers.xml
XPathʹ�ã�
/html/head/title: ѡ��<HTML>�ĵ��� <head> ��ǩ�ڵ� <title> Ԫ��
/html/head/title/text(): ѡ�������ᵽ�� <title> Ԫ�ص�����
//td: ѡ�����е� <td> Ԫ��
//div[@class="mine"]: ѡ�����о��� class="mine" ���Ե� div Ԫ��
scrapy.cfg ����Ŀ�������ļ�
mySpider/ ����Ŀ��Pythonģ�飬������������ô���
mySpider/items.py ����Ŀ��Ŀ���ļ�
mySpider/pipelines.py ����Ŀ�Ĺܵ��ļ�
mySpider/settings.py ����Ŀ�������ļ�
mySpider/spiders/ ���洢�������Ŀ¼
���飺����ITcast��Ŀ�ļ����½�һ��DATA�ļ��������������ɵ����ݣ�����DATA�ļ���ִ��scrapy crawl ITcast����