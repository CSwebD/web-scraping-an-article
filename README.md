# Web Scraping Python Course
This project aims to scrape information about a Python course from a website and save it to a CSV file using BeautifulSoup and requests.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project scrapes Python course information including headline, summary, and video link from a specified URL and saves it to a CSV file.

## Features

- **Web Scraping:** Uses BeautifulSoup to scrape data from a webpage.
- **CSV Output:** Saves the scraped data to a CSV file.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/web-scraping-python-course.git
    cd web-scraping-python-course
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the `scrape.py` script to scrape data from the specified URL and save it to a CSV file:

```bash
python scrape.py
