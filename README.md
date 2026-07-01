# Web Scraping Projects

A collection of Python web scraping projects built using `requests`, `BeautifulSoup`, and `Selenium`. Includes both real-world projects (scraping live, public data sources) and practice projects (using sites built specifically for learning scraping).

## 🌍 Real-World Projects

These scrape live, real websites with genuine public data.

### 1. Times of India News Scraper — `TOI_news.py`
Scrapes live headlines and article links from Times of India and saves to `toi_headlines.csv`.
- **Tools:** `Selenium`
- **Concepts:** JS-rendered site, href-based selectors, filtering empty elements
- **Source:** timesofindia.indiatimes.com (live data)

### 2. GitHub Trending Repos Scraper — `GIT.py`
Scrapes trending repositories (name, language, description) from GitHub Trending and saves to `repos.csv`.
- **Tools:** `Selenium`
- **Concepts:** Dynamic JS site, error handling for missing fields
- **Source:** github.com/trending (live data)

### 3. Wikipedia GDP Scraper — `GDPs.py`
Scrapes the "List of countries by GDP (nominal)" table from Wikipedia and exports to `gdp_by_country.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Parsing complex HTML tables, cleaning footnote markers
- **Source:** en.wikipedia.org (live data)

### 4. Hacker News Scraper — `news_scraper.py`
Scrapes top story titles and points from Hacker News, saved to `stories.csv`.
- **Tools:** `requests`, `BeautifulSoup`
- **Concepts:** Pairing separate elements with `zip()`
- **Source:** news.ycombinator.com (live data)

## 🧪 Practice Projects

Built on sites specifically designed for scraping practice.

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
- **Concepts:** Error handling, data cleaning, CSV quoting

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
python3 TOI_news.py
```

## Tech Stack

- Python 3
- `requests` — fetching static pages
- `BeautifulSoup` — parsing HTML
- `Selenium` — scraping JavaScript-rendered and AJAX-loaded sites
- `webdriver-manager` — automatic ChromeDriver management
