# GemFinder - Jewellery Product Recommendation System

💎 **GemFinder** is a jewellery product recommendation system that allows users to search, filter, and explore jewellery products with images, price, category, and ratings. It features an intuitive, aesthetic interface for easy product discovery.

---

## Overview of the Agent
GemFinder is designed to help users discover jewellery products efficiently. Users can search by keyword, filter by category, price range, and rating, and view detailed product information with images. The system provides a clean, modern, and interactive interface using Streamlit.

---

## Features
- Keyword search in product titles and descriptions
- Filter by category, price range, and minimum rating
- Sort products by rating or price
- Aesthetic product cards with images, rounded corners, and category badges
- Responsive and clean Streamlit interface

---

## Limitations
- Works only with the provided dataset (`jewellery_custom.csv`)
- Images must exist in the `images/` folder
- Dataset is simulated; does not fetch live data from Amazon or other online sources
- Does not include user authentication or personalized recommendations

---

## Tech Stack & APIs Used
- **Python 3.x**  
- **Pandas** – for data manipulation  
- **Streamlit** – for interactive user interface  
- Local CSV dataset (`jewellery_custom.csv`)  
- Images stored locally in `images/` folder  

> No external APIs or machine learning models are used in this version.

---

## Setup & Run Instructions

1. Clone the repository:

```bash
git clone https://github.com/hithagovi/luxurygems
cd luxurygems
