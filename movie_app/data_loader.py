import pandas as pd

def load_initial_movies(limit=50):
    """
    Loads the first 'limit' movies that have valid TMDB IDs.
    Returns a list of dictionaries ready for Flask.
    """
    # 1. Load the essential files
    # Note: We use 'dtype' to save memory, just like before
    movies = pd.read_csv('../data/movies.csv') # Adjust path to your data folder
    links = pd.read_csv('../data/links.csv', dtype={'tmdbId': 'Int32'})

    # 2. Merge them (We need the TMDB ID to get posters!)
    df = pd.merge(movies, links, on='movieId', how='inner')

    # 3. Clean up: Drop movies without a TMDB ID
    df = df.dropna(subset=['tmdbId'])

    # 4. Take the top N (For now, just the first N rows)
    # Later, your team will sort this by 'Popularity Score'
    df_subset = df.head(limit)

    # 5. Convert to a list of dictionaries for Flask
    # Output format: [{'id': 1, 'title': 'Toy Story', 'tmdb_id': 862}, ...]
    movie_list = []
    for _, row in df_subset.iterrows():
        movie_list.append({
            'id': int(row['movieId']),
            'title': row['title'],
            'tmdb_id': int(row['tmdbId']),
            'poster_url': None # We will fetch this later in app.py
        })
    
    return movie_list

if __name__ == "__main__":
    # Test run
    data = load_initial_movies(5)
    print(f"Loaded {len(data)} movies.")
    print(data[0])