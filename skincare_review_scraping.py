import requests
import time
import csv
import random

from tabulate import tabulate
from bs4 import BeautifulSoup

# Base URL for the product review
url = "https://reviews.femaledaily.com/products/treatment/serum-essence/somethinc/5-niacinamide-moisture-sabi-beet-serum"
response = requests.get(url, verify=False)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

# Base URL for the product reviews, with a placeholder for the page number
base_url = "https://reviews.femaledaily.com/products/treatment/serum-essence/somethinc/5-niacinamide-moisture-sabi-beet-serum?cat=&cat_id=0&age_range=&skin_type=&skin_tone=&skin_undertone=&hair_texture=&hair_type=&order=newest&page="

# initialize the number of pages (you can change the number as you like)
page_number = 11

# List to store the review data
data_reviews = []

# Loop through pages 1 to over
for page in range(1, page_number):
    url = base_url + str(page)  # Construct the URL for the current page
    print(f"Scraping page {page}: {url}")

    # Send GET request to fetch the page content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")  # Parse the HTML content

    # Find all the review cards on the page
    reviews = soup.find_all("div", class_="review-card")

    # Loop through each review and extract necessary information
    for review in reviews:
        # Extract review date
        date = review.find("p", class_="review-date")
        date = date.text.strip() if date else "N/A"  # If no date, use "N/A"

        # Extract rating by counting the number of full stars (icon-ic_big_star_full)
        stars = review.find("span", class_="cardrv-starlist")
        if stars:
            rating = len(stars.find_all("i", class_="icon-ic_big_star_full"))  # Count full stars
        else:
            rating = 0  # If no stars, set rating to 0

        # Extract review text
        text = review.find("p", class_="text-content")
        text = text.find("span").text.strip() if text else "N/A"  # If no text, use "N/A"

        # Append the extracted data as a dictionary to the data_reviews list
        data_reviews.append({
            "Tanggal": date,  # Date of review
            "Rating": rating,  # Rating (number of full stars)
            "Review": text  # Text content of the review
        })

    # Sleep for 20 seconds between requests to avoid overloading the server
    time.sleep(20)

# Randomly select 10 reviews from the list of all reviews
random_reviews = random.sample(data_reviews, 10)  # Pick 10 random reviews
headers = ["No", "Tanggal", "Rating", "Review"]  # Table headers
table_data = [(i+1, review["Tanggal"], review["Rating"], review["Review"]) for i, review in enumerate(random_reviews)]  # Prepare table data

# Print the selected random reviews in a tabular format using tabulate
print("\nScraped Data (10 Random Entries):\n")
print(tabulate(table_data, headers, tablefmt="grid"))

# Save all scraped reviews to a CSV file
with open("reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Tanggal", "Rating", "Review"])  # Prepare CSV writer
    writer.writeheader()  # Write header row to the CSV
    writer.writerows(data_reviews)  # Write all scraped data rows to the CSV

# Final message indicating completion of scraping and saving the data
print("\nScraping completed! Data has been saved to 'reviews.csv'")
