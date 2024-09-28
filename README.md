# Personalized-News-Aggregator
A news aggregator that scrapes articles from multiple sources, categorizes them, and provides access via a REST API and a simple front-end interface.

# Personalized News Aggregator

## Overview
This project is a personalized news aggregator that scrapes articles from multiple sources, categorizes them using NLP, and provides access via a REST API. It supports basic keyword searches and filters by category or date range.

### Features
- Scrapes articles from multiple news sources
- Categorizes articles into topics (politics, technology, sports, etc.)
- Provides a REST API to retrieve articles and search them
- Serves data in JSON format

## Technologies Used
- Python
- Django
- BeautifulSoup, Requests
- NLP Libraries: NLTK, spaCy
- CSV for storing data
- REST API for serving data

## Setup Instructions
1. Clone the repository.
   git clone https://github.com/SrikarSaini/Personalized-News-Aggregator.git
   cd Personalized-News-Aggregator
2. Set Up a Virtual Environment.
3. Install Dependencies
4. Run the Scraper
5. Set Up the API
6. Access and Test the API
7. Testing the API using Postman/Newman/Insomnia

## Use Postman or your browser to interact with the API. You can test the following endpoints
- GET /articles: Retrieves all articles
- GET /articles/{id}: Retrieves a specific article by its ID
- GET /search?keywords={query}: Searches articles by a specific keyword

## Google Drive Video Link 
- https://drive.google.com/file/d/1_vmNFfobvaG0radE7AvGeiZ8iF4uoVJW/view?usp=sharing

