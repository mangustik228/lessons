## Лекции про scrapy с разных мест и просто эксперименты.

### Источники: 

1. [ScrapeOps](https://www.youtube.com/@scrapeops)



### AWS 

```bash 
# library for aws 
pip install botocore

scrapy crawl [SPIDER_NAME] -O s3://aws_key:aws_secret@mybucket/path/to/pyscrapeddata.scv:scv

``` 


### MySQL 




### Scrapyd [Другой урок](https://www.youtube.com/watch?v=PZKH5S0C8EI)

```bash 
# scrapy.cfg 
url = http://localhost:6800/ # Надо раскоментировать 

# Установка scrapyd scrapyd-client 
pip install scrapyd scrapyd-client 

# look pipelines_and_sql.test and docs for scrapyd-client
```

### redis 

```bash 
pip install scrapy-redis
# см Документацию https://github.com/rmax/scrapy-redis
```