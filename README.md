# Sydney Restaurants Scraper
 This is a Python project to scrape restaurants in Sydney from [Concrete Playground](https://concreteplayground.com/sydney/restaurants) website using Scrapy

## Web Scraping Summary
The script used in this project will crawl through https://concreteplayground.com/sydney/restaurants and get the following details for each restaurant in the Sydney area:
- Name
- Street Address
- Suburb
- Style
- Phone Number
- Website
- Date published to the Concrete Playground website

This data is then exported to a CSV file under the *export* folder. Thereafter the data is parsed using a Jupyter notebook and exported as an Excel file, so the end user can choose which file type they'd prefer for subsequent use and application.

PS: If you'd like to replicate the data exporting process, navigate to the *sydney_restaurants* folder and using the command `scrapy crawl restaurants -O ../export/sydney-restaurants.csv`, will export the data to the *export* folder of the root directory.
