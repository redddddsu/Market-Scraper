## About
Whenever my tomestone currency caps, I need to search for the highest-selling resources to dumb my currency. This usually doesn't take that long but it is still a bother, so I decided to build a web scraper that scraps from https://universalis.app/.

This is mainly built with Selenium because it requires selecting the correct data center when scraping.
Note: this only works for **Aether**, if you want to check the prices on other Data Centers you can change line 28 to a different Data Center.
>EC.presence_of_all_elements_located((By.XPATH, '//*[@value="Siren"]'))

## Installation 
[Download](https://github.com/redddddsu/Market-Scraper/releases/tag/v1.0) and unzip the file. 
Run the executable inside the file with chromedriver.exe. The chromedriver allows Selenium to interact with the website properly.
