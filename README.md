# Web Scraper for Course Information

A Python-based web scraping tool that extracts course details (headline, summary, video link) from a specified educational platform and saves the results to CSV.

## Contents

```
.
├── scrape.py               # Main scraping script
├── requirements.txt        # Python dependencies
├── LICENSE
├── cms_scrape.csv          # Example output of scraped course data
└── README.md               # This file
```

## Prerequisites

* Python 3.7 or higher
* Install required packages:

  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. **Configure target URL**

   * Open `scrape.py` and set the `BASE_URL` or `TARGET_PAGE` to the page you wish to scrape.

2. **Run the scraper**

   ```bash
   python scrape.py
   ```

   * The script will fetch the page content, parse the HTML, and extract headline, summary, and video link for each course.
   * Results are written to `cms_scrape.csv` in the project root.

3. **Inspect output**

   * Open `cms_scrape.csv` with your favorite spreadsheet application or use pandas/R to analyze the data.

## Script Overview (`scrape.py`)

* Uses `requests` to retrieve HTML content.
* Parses HTML with `BeautifulSoup` (using `lxml` parser).
* Finds course elements by CSS selectors or HTML tags.
* Extracts and cleans text fields.
* Writes structured data to CSV via the `csv` module.

## Contributing

Contributions are welcome! Feel free to file issues or submit pull requests for enhancements, such as:

* Support for pagination or multiple pages.
* Export to other formats (JSON, Excel).
* Integration with scheduling or automation tools.

## License

This project is licensed under the MIT License. See [LICENSE](/LICENSE) for details.
