import scrapy


class RestaurantsSpider(scrapy.Spider):
    name = "restaurants"
    allowed_domains = ["concreteplayground.com"]
    start_urls = ["https://concreteplayground.com/sydney/restaurants"]

    def parse(self, response):
        rest_links = response.css("div.info.clearfix > p.name > a::attr(href)").getall()

        for link in rest_links:
            yield response.follow(link, self.parse_restaurants)

        next_page = response.css(
            "div.numbered-pagination.pagination > a.next.page-numbers::attr(href)"
        ).get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_restaurants(self, response):
        name_rest = response.css("h1.title::text").get()

        street_address = (
            response.css("section.article-details.clearfix > div.section-content::text")
            .get()
            .strip()
        )
        street_address = (
            street_address.rstrip(",")
            if street_address.endswith(",")
            else street_address
        )

        suburb = response.css(
            "section.article-details.clearfix > div.section-content > a::text"
        ).get()

        phone_contact = response.css(
            "section.article-details.clearfix > div.section-content > span[itemprop='telephone'] > a::text"
        ).get()

        style = response.css("li.infoitem > ul.subinfo > li > a[rel='tag']::text").get()

        url_rest = response.css(
            "div.buttons-container > section.email.places > a[itemprop='url']::attr(href)"
        ).get()

        date_pub = response.css(
            "div.published > div.info > span.created_at::text"
        ).get()

        yield {
            "name": name_rest,
            "street address": street_address,
            "suburb": suburb,
            "style": style,
            "phone number": phone_contact,
            "website": url_rest,
            "date published": date_pub,
        }
