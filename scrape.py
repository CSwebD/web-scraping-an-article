from bs4 import BeautifulSoup
import requests
import csv

# Define the URL to scrape
url = 'https://developer-roadmaps.netlify.app/python'

# Send an HTTP GET request to the URL
source = requests.get(url).text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(source, 'lxml')

# Open a CSV file for writing
csv_file = open('cms_scrape.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Write the headers to the CSV file
csv_writer.writerow(['headline', 'summary', 'video_link'])

# Extract the headline from the HTML content
headline = soup.find('h2', class_='title-page').text.strip()
print(headline)

# Extract the summary from the HTML content
summary_section = soup.find('section', id='text-course')
summary = summary_section.find('p', class_='paragraph').text.strip()
print(summary)

# Extract the video link from the iframe in the HTML content
try:
    video_iframe = soup.find('iframe')
    video_src = video_iframe['src']

    # Extract the video ID from the video source URL
    if 'youtube.com' in video_src:
        vid_id = video_src.split('/embed/')[1]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    else:
        yt_link = video_src
except Exception as e:
    yt_link = None

print(yt_link)
print()

# Write the extracted data to the CSV file
csv_writer.writerow([headline, summary, yt_link])

# Close the CSV file
csv_file.close()
