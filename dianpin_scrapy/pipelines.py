# -*- coding: utf-8 -*-

from scrapy.exporters import JsonItemExporter, CsvItemExporter, XmlItemExporter
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class honglingjingjson(object):
    def open_spider(self, spider):
        self.file = open('honglingjing.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class honglingjingcsv(object):
    def open_spider(self, spider):
        self.file = open('honglingjing.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class honglingjingxml(object):
    def open_spider(self, spider):
        self.file = open('honglingjing.xml', 'wb')
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class dianpincityxml(object):
    def open_spider(self, spider):
        self.file = open('dianpincity.xml', 'wb')
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class dianpincitycsv(object):
    def open_spider(self, spider):
        self.file = open('dianpincity.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item