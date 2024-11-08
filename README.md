# Sydney Restaurants Scraper
 This is a Python project to scrape restaurants in Sydney from [Concrete Playground](https://concreteplayground.com/sydney/restaurants) using Scrapy

## Web Scraping Summary
The script used in this project will crawl through https://concreteplayground.com/sydney/restaurants and get the following details for each restaurant in the Sydney area:
- Name
- Street Address
- Suburb
- Style
- Phone Number
- Website
- Date published to the Concrete Playground website

This data is then exported to a CSV file in the *export* folder. Thereafter the data is parsed using a Jupyter notebook and exported as an Excel file, so the end user can choose which file type they'd prefer for subsequent use and application.

A simple dashboard showing a general overview of the data was also added to the excel file to help end-users have general insight into the data before diving in.

![excel dashboard](./images/sydney-restaurants-dashboard-screenshot.png)

PS: If you'd like to replicate the data exporting process, navigate to the *sydney_restaurants* folder, then using the command `scrapy crawl restaurants -O ../export/sydney-restaurants.csv`, will export the data to the *export* folder of the root directory.
