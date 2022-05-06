SalePriceScrape the William Sonoma Data Specialist price scraper!

The purpose of this script is to pull the pricing information using the BeautifulSoup library for analysis, testing, and further manipulation.

Here is the desired result:

![WilliamSonomaScraper](https://user-images.githubusercontent.com/5562920/167085824-577697c7-9e9f-45e4-94e8-87f61c75c934.png)

The text is isolated. From here, it can be sent in an email, placed into an excel spreadsheet, or currated in any fashion.

Here is the pricing information with all of the HTML information:

![WilliamSonomaScraper2](https://user-images.githubusercontent.com/5562920/167086231-5516ac26-41af-455c-a180-e9ea129b4a01.png)


To-Do:

- Allow the variable URL to pull a list of URLs from a txt file, spreadsheet, or database.
  - Iterate through each line of the URL_LIST.txt file and pull all pricing information of desired urls
- Spreadsheet integration with openpyxl library
