数据存储到数据库中
1.出现 ImportError: No module named ‘MySQLdb' 错误：在Windows环境下通过CMD进入命令提示符，输入:pip install PyMySQL
然后在需要的项目中，在
 __init__.py中添加两行：
import pymysql
pymysql.install_as_MySQLdb()
就可以用 import MySQLdb了
2.出现 ImportError: No module named ‘MySQLdb' 错误：在Windows环境下通过CMD进入命令提示符，输入:pip install web.py