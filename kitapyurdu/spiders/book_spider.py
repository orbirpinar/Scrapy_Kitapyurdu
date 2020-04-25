import scrapy

from ..items import KitapyurduItem
class BookSpider(scrapy.Spider):
	name = "books"

	start_urls = ["https://www.kitapyurdu.com/index.php?route=product/category&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC&page=1",

					]
	

	def parse(self,response):
		booksDetailUrl =[link.attrib["href"] for link in response.css("div.cover a")]
		for url in booksDetailUrl:
			url = response.urljoin(url)
			yield scrapy.Request(url=url,callback=self.parse_details)
		next_page = response.xpath('//a[@class="next"]/@href').get()
		
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)

	def parse_details(self,response):
		title = " ".join(response.xpath('//h1[@itemprop="name"]/text()').extract())
		author = response.xpath('//span[@itemprop="name"]/text()').extract_first()
		price = "".join(response.xpath('//div[@class="middle"]/span[@class="text"]//text()').extract())
		booksImageLink = response.xpath('//img[@itemprop="image"]/@src').extract_first()
		publisher = response.css("div.publishers span a span::text").extract_first()
		description = "\n".join(response.css("[id='description_text'] span::text").extract())
		isbn = response.xpath('//span[@itemprop ="isbn"]/text()').extract_first()
		datePublished = response.xpath('//td[@itemprop="datePublished"]/text()').extract_first()
		bookEdition = response.xpath('//span[@itemprop ="bookEdition"]/text()').extract_first()
		numberOfPages = response.xpath('//span[@itemprop = "numberOfPages"]/text()').get()
		authorDetailPage = response.xpath("//span[@itemprop='author']/a[@itemprop='url']/@href").extract_first()

		yield {
		'title':title,
		'author':author,
		'price':price,
		'booksImageLink':booksImageLink,
		'publisher':publisher,
		'description':description,
		'isbn':isbn,
		'datePublished':datePublished,
		'bookEdition':bookEdition,
		'numberOfPages':numberOfPages,
		'authorDetailPage':authorDetailPage

		}
		
		