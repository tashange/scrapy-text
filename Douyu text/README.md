# Douyu
����Ŀ����scrapy���
��Ҫ�޸���settings.py items.py pipelines.py douyu.py�ļ�
��װ��
1.ֱ���ü��ɰ����а�װ���ٶ�����Miniconda��ѡ���Ӧ�汾���а�װ��һ·next
��װ��ɺ�cmd�����ã�conda list ��������Ƿ�ɹ���װ��
2.����װ���ɹ���������·��û��������ȷ��
3.ʹ�����conda install -c conda-forge scrapy ��װscrapy���
ʹ��scrapy��
1.�½���Ŀ
���scrapy startproject ITcast(��Ŀ��)
ע��settings.py �����ļ�(���ڿ����ܵ�)  items.py��Ҫ��ȡ���ֶ� 
pipelines.py�ܵ��ļ� spiders�ļ����´�ŵ�������ű�
2.�½�����
���scrapy genspider itcast (�ļ���) ��http://www.itcast.cn��(��ȡ�ķ�Χ)
ע��ֻҪ�ڸ���Ŀ�ļ��´����Ϳ��ԣ��ļ����Զ�������spiders�ļ�����
3.ִ����������
Scrapy crawl itcast(����������Ӧ��������е�name����)
4.ʹ��ý��ܵ���Ҫ��PIL�����֧�֣�ʹ��Miniconda��װû�и��������Ҫ�ֶ���װ
��װpillow���pip install pillow