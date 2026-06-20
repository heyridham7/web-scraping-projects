# Web Scraping Projects

A collection of Python web scraping projects built using `requests`, `BeautifulSoup`, and `Selenium`. Each project demonstrates a different scraping scenario — static pages, pagination, AJAX-loaded content, and dynamic JavaScript-rendered sites.

## Projects

### 1. Books Scraper — `books_scraper.py`
Scrapes book titles and prices from [books.toscrape.com](https://books.toscrape.com) across multiple pages and saves the data to `book.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Pagination, CSV export, encoding handling

### 2. Quotes Scraper — `quotes_scraper.py`
Extracts quotes and their authors from [quotes.toscrape.com](https://quotes.toscrape.com) across 10 pages, saved to `quotes.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Pagination, CSV export

### 3. Movies Scraper (AJAX) — `movies_scraper.py`
Scrapes Oscar-winning movie data (title, nominations, awards) from an AJAX-loaded table on [scrapethissite.com](https://www.scrapethissite.com/pages/ajax-javascript/).
- **Tools:** `Selenium`
- **Concepts:** Handling AJAX-loaded content, explicit waits

### 4. Jobs Scraper — `jobs_scraper.py`
Extracts job listings (title, company, location) from [realpython.github.io/fake-jobs](https://realpython.github.io/fake-jobs/), saved to `jobs.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Error handling, data cleaning, CSV quoting for fields with commas/newlines

### 5. News Scraper — `news_scraper.py`
Scrapes top story titles and points from [Hacker News](https://news.ycombinator.com), saved to `stories.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Pairing separate elements with `zip()`

### 6. Price Tracker — `price_tracker.py`
Logs book prices from books.toscrape.com with a timestamp on every run, appending to `price_history.csv` to build a price history over time.
- **Tools:** `requests`, `BeautifulSoup`, `datetime`
- **Concepts:** Append-mode file writing, timestamp logging

## Setup

```bash
git clone https://github.com/heyridham7/web-scraping-projects.git
cd web-scraping-projects
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4 selenium webdriver-manager
```

## Running a script

```bash
python3 books_scraper.py
```

## Tech Stack

- Python 3
- `requests` — fetching static pages
- `BeautifulSoup` — parsing HTML
- `Selenium` — scraping JavaScript-rendered and AJAX-loaded sites
- `webdriver-manager` — automatic ChromeDriver management

## Notes

All scrapers target publicly available practice sites built specifically for learning web scraping (books.toscrape.com, quotes.toscrape.com, scrapethissite.com, realpython.github.io/fake-jobs) or public data (Hacker News).
