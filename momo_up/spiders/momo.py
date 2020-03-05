# -*- coding: utf-8 -*-
import scrapy
import random


class MomoSpider(scrapy.Spider):
    name = 'momo'
    allowed_domains = ['maimemo.com']
    start_urls = ['https://www.maimemo.com/share/page?uid=6137470&pid=0971e7ff9993e24afbf3b92f16beecc4&tid=18b100dfb88a8c21eecb869748e1a28d']
    num = 0

    def parse(self, response):
        if response.status == 200:
            self.num += 1
            print('正在刷墨墨访问量,次数：%d' % self.num)
            try:
                yield scrapy.Request(self.start_urls[0], dont_filter=True)
            except:
                yield scrapy.Request(self.start_urls[0], dont_filter=True)
