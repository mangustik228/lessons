from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


class ParsingerLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(lambda x: x.strip())
    price_in = MapCompose(lambda x: int(x.split(" ")[0]))
    url_in = MapCompose(lambda x: "https://parsinger.ru/" + x)
