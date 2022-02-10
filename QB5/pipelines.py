# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from unicodedata import name
from itemadapter import ItemAdapter
import pymysql

def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "wp445203",
        charset = "utf8",
        use_unicode = False
    )
    return conn

def insertInfo(item):
    dbObject = dbHandle()
    cursor = dbObject.cursor()
    cursor.execute("USE Tinfo")
    sql = "INSERT INTO infos(name,url) VALUES(%s,%s)"
    try:
        cursor.execute(sql,(item['name'],item['url']))
        cursor.connection.commit()
    except BaseException as e:
        print("错误在这里>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<错误在这里")
        dbObject.rollback()
    pass
    

class Qb5Pipeline:
    def process_item(self, item, spider):
        insertInfo(item)
        return item
