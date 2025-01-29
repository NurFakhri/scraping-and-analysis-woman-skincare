# Indonesian Skincare Review Analysis 💅💆‍♀️

## Project Overview

This project focuses on scraping and analyzing **skincare product reviews** from the **Female Daily** platform. The primary goal is to analyze customer sentiment, categorize reviews, and provide insights into the most common keywords and customer satisfaction for specific products.

## Data Source

The data is scraped from **Female Daily**, a popular Indonesian beauty and skincare community platform. Specifically, reviews for skincare products such as serums, moisturizers, and other treatments are gathered for analysis.

### Example Product:
- **Product Name:** Somethinc Niacinamide - Moisture Sabi Beet Brigtening Serum

## Project Goals

1. **Scraping Reviews**: To collect review data for skincare products.
2. **Sentiment Analysis**: Classify reviews into categories (e.g., "kecewa" (disappointed), "netral" (neutral), "puas" (satisfied)).
3. **WordCloud Visualization**: Generate WordClouds based on review text to highlight frequently mentioned terms.
4. **Insights Extraction**: Provide insights on customer satisfaction, highlight common issues, and trends across the reviews.

## Technologies Used

- **Web Scraping**: Python, with libraries such as:
  - **BeautifulSoup**: To parse and extract data from HTML pages.
  - **Requests**: To send HTTP requests and retrieve content from the website.
- **Data Analysis**: Python with **Pandas** for data manipulation and **Matplotlib** for visualization.
- **Sentiment Categorization**: Custom logic to categorize reviews based on ratings into "kecewa", "netral", and "puas".
- **WordCloud**: Python `WordCloud` library to create visualizations of frequent terms in reviews.

## Scraping Process

## Scraping Process

1. **Extract Product Reviews**:
   - **Respecting Robots.txt**: Before scraping, the project ensures that it complies with the site's `robots.txt` file, which outlines the website's scraping policies. The scraper checks that scraping the review pages is allowed under the `User-agent: *` section, which prevents violating any site rules.
   - Scraping review details (rating, date, text) from product pages.
   - **Pagination** is handled to scrape multiple pages (up to 20 pages). The pages are numbered at the end of the URL (e.g., `page=1`, `page=2`).
   - **Delay Between Requests**: To avoid overloading the server and to be respectful of the website's resources, a delay of **20 seconds** is introduced between scraping each page. This helps reduce the frequency of requests and makes the scraping process less intrusive.

3. **Data Extraction**:
   - Review date: Extracted upload date`.
   - Rating: Counted based on star icons, from 1 to 5.
   - Review Text: Extracted text review.

4. **Data Storage**: The scraped data is saved in CSV files with columns: `No`, `Tanggal`, `Rating`, `Review`.

## Data Analysis

The analysis consists of the following steps:

1. **Preprocessing**:
   - Removal of stopwords in **Indonesian** to clean the text for analysis.
   - Text normalization by removing punctuation and digits.

2. **Sentiment Classification**:
   - Reviews are categorized based on their ratings:
     - Rating 1-2: "Kecewa" (Disappointed)
     - Rating 3: "Netral" (Neutral)
     - Rating 4-5: "Puas" (Satisfied)

3. **Visualizations**:
   - **Bar Chart**: Showing the distribution of reviews across rating categories (1 to 5).
   - **Pie Chart**: Representing the distribution of sentiment categories ("Kecewa", "Netral", "Puas").
   - **WordCloud**: Displaying the most frequent words for each sentiment category.

## How to Run the Project

### Prerequisites
- Python 3.7+
- Libraries: `beautifulsoup4`, `requests`, `pandas`, `matplotlib`, `nltk`, `wordcloud`

You can install the required libraries by running:

```bash
pip install beautifulsoup4 requests pandas matplotlib nltk wordcloud
```

### Running the Scraping Script

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Indonesian-Skincare-Review-Analysis.git
    cd Indonesian-Skincare-Review-Analysis
    ```

2. Run the script to scrape reviews:
    ```bash
    python scrape_reviews.py
    ```

3. After scraping, run the analysis and generate visualizations:
    ```bash
    python analyze_reviews.py
    ```

## Conclusion

This project aims to provide a better understanding of customer feedback for skincare products, helping brands and consumers alike by offering valuable insights from user reviews.

---

** Author: Muhammad Hadi Nur Fakhri **
