# Web Scraping Projects

A collection of Python web scraping projects built using `requests`, `BeautifulSoup`, and `Selenium`. Includes both practice projects (using sites built specifically for learning scraping) and real-world projects (scraping live, public data sources).

## 🌍 Real-World Projects

These scrape live, real websites with genuine public data.

### Wikipedia GDP Scraper — `GDPs.py`
Scrapes the "List of countries by GDP (nominal)" table from Wikipedia and exports country-wise GDP data to `gdp_by_country.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Parsing complex HTML tables, filtering header/junk rows, cleaning footnote markers from text
- **Source:** en.wikipedia.org (live data)

### News Scraper — `news_scraper.py`
Scrapes top story titles and points from [Hacker News](https://news.ycombinator.com), saved to `stories.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Pairing separate elements with `zip()`
- **Source:** news.ycombinator.com (live data)

## 🧪 Practice Projects

Built on sites specifically designed for scraping practice, used to learn core concepts before tackling real sites.

### Books Scraper — `books_scraper.py`
Scrapes book titles and prices from books.toscrape.com across multiple pages, saved to `book.csv`.
- **Concepts:** Pagination, CSV export, encoding handling

### Quotes Scraper — `quotes_scraper.py`
Extracts quotes and authors from quotes.toscrape.com across 10 pages, saved to `quotes.csv`.
- **Concepts:** Pagination, CSV export

### Movies Scraper (AJAX) — `movies_scraper.py`
Scrapes Oscar-winning movie data from an AJAX-loaded table on scrapethissite.com.
- **Tools:** `Selenium`
- **Concepts:** Handling AJAX-loaded content, explicit waits

### Jobs Scraper — `jobs_scraper.py`
Extracts job listings (title, company, location) from realpython.github.io/fake-jobs, saved to `jobs.csv`.
- **Concepts:** Error handling, data cleaning, CSV quoting for fields with commas/newlines

### Price Tracker — `price_tracker.py`
Logs book prices from books.toscrape.com with a timestamp on every run, appending to `price_history.csv`.
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
python3 GDPs.py
```

## Tech Stack

- Python 3
- `requests` — fetching static pages
- `BeautifulSoup` — parsing HTML
- `Selenium` — scraping JavaScript-rendered and AJAX-loaded sites
- `webdriver-manager` — automatic ChromeDriver management
