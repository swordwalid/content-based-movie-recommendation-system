# Content-Based Movie Recommendation System

This project is a **Content-Based Movie Recommendation System** built using **Streamlit**. The system suggests movies based on user input and provides corresponding image posters using the **TMDB API**. The recommendation algorithm utilizes a **Bag of Words** model for vectorization and **Cosine Similarity** for measuring the similarity between movie plots.

## Features

- Enter a movie name to get recommendations for similar movies.
- Displays recommended movie titles along with their posters.
- The system uses cosine similarity to compare movie content (plots, genres, etc.).
- Simple, interactive web application using Streamlit.

## How It Works

1. **User Input**: The user enters the name of a movie in the search bar.
2. **Recommendation System**: The system finds similar movies by calculating the cosine similarity between the input movie and others using a precomputed similarity matrix.
3. **Poster Fetching**: The posters of the recommended movies are fetched from the TMDB API and displayed alongside the titles.

## Datasets Used

- **tmdb_5000_movies.csv**: Contains information about movies, such as titles, genres, and movie IDs.
- **tmdb_5000_credits.csv**: Contains additional information related to movie credits, such as the cast and crew.
- These datasets were used to build the movie database, which powers the recommendation system.

## Methodology

1. **Vectorization**: 
   - The **Bag of Words (BoW)** technique was used to convert textual data (movie content) into vectors.
   
2. **Similarity Metric**:
   - **Cosine Similarity** was used to compute the similarity between movie vectors, which helps in finding movies with similar content.
   
3. **Poster Retrieval**:
   - Movie posters are retrieved using **TMDB API** by querying the movie's ID.

## Tech Stack

- **Python**: Core programming language for the application.
- **Streamlit**: Used to create an interactive and responsive web interface.
- **Pandas**: For data manipulation and handling movie data from the CSV files.
- **Scikit-learn**: For vectorizing the movie data using Bag of Words and computing the cosine similarity.
- **Requests**: For making API calls to the TMDB API and retrieving movie posters.

## Installation and Setup

To run the project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/swordwalid/content-based-movie-recommendation-system.git
   cd content-based-movie-recommendation-system
2. Create a virtual environment and activate it
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
4. Download the dataset files (tmdb_5000_movies.csv and tmdb_5000_credits.csv) and place them in the root directory.
5. Run the Streamlit application
   ```bash
   streamlit run app.py