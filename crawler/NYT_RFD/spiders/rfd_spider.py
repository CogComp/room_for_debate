import scrapy
import json
from urllib.parse import urljoin


class Debate(scrapy.Item):
    debate_url = scrapy.Field()
    debate_headline = scrapy.Field()
    debate_date = scrapy.Field()
    debate_introduction = scrapy.Field()
    debate_articles = scrapy.Field()


class RFDSpider(scrapy.Spider):
    name = "NYT_RFD"
    total_page_num = 63

    def start_requests(self):

        urls = ['https://www.nytimes.com/roomfordebate/page/{}'.format(i) for i in range(1, self.total_page_num + 1)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_articles = response.css("ul.nytint-archive-discussions>li>h5>a").xpath('@href').getall()
        all_articles = [url.replace("..", "https://www.nytimes.com/roomfordebate") for url in all_articles if url.startswith("..")]
        for article in all_articles:
            yield scrapy.Request(url=article, callback=self.parse_debate_intro)

    def parse_debate_intro(self, response):

        debate_url = response.request.url
        debate_headline = response.css("div.nytint-discussion-header>h1::text").get()
        debate_date = response.css('p.pubdate::text').get()
        intro_div = response.css("div.nytint-intro")

        if len(intro_div) == 0:
            intro_div = response.css("div.nytint-discussion-content")

        debate_introduction = "".join(intro_div.css("p").xpath('./descendant-or-self::*/text()').extract())

        discussion_links = response.css('ul.nytint-participants').css('a').xpath('@href').extract()
        discussion_links = [urljoin(response.request.url, link) for link in discussion_links if not link.startswith("//")]

        debate_item = Debate()
        debate_item["debate_url"] = debate_url
        debate_item["debate_headline"] = debate_headline
        debate_item["debate_date"] = debate_date
        debate_item["debate_introduction"] = debate_introduction

        for link in discussion_links:
            yield scrapy.Request(url=link, callback=self.parse_debate_article, meta={'item': debate_item})


    def parse_debate_article(self, response):

        item = response.meta['item']

        article = response.css('article.rfd')
        article_url = response.request.url

        headline = self._clean_web_text("".join(article.css('.nytint-post-headline::text').extract()))

        author_desc = article.css('.nytint-post-leadin').xpath('string(.)').extract()[0]
        author_desc_links = article.css('.nytint-post-leadin>a').xpath('@href').extract()
        author_desc_links = [urljoin(article_url, link) for link in author_desc_links]

        publication_date = article.css('.pubdate::text').extract()[0].strip()

        _post = article.css('div.nytint-post')
        post_content = "".join(_post.css('p').xpath('string(.)').extract())
        post_summary = _post.css('.entry>blockquote::text').get()

        item["debate_articles"] = {
            "article_url": article_url,
            "author_description": author_desc,
            "author_description_links": author_desc_links,
            "publication_date": publication_date,
            "headline": headline,
            "summary": post_summary,
            "content": post_content,
        }

        return item

    @staticmethod
    def _clean_web_text(str):
        return str.replace('\xa0', ' ')