import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv(dotenv_path='config/.env')
BEARER_TOKEN = os.getenv('TMDB_BEARER_TOKEN')
BASE_URL = 'https://api.themoviedb.org/3/movie/{}'

HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# File paths
CREDITS_CSV_PATH = 'data/tmdb_5000_credits.csv'
OUTPUT_CSV_PATH = 'data/tmdb_5000_movies_fetched.csv'

def fetch_movie_metadata(movie_ids):
    movies_data = []

    for movie_id in tqdm(movie_ids[:]):
        url = BASE_URL.format(movie_id)

        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()

            data = response.json()
            movies_data.append({
                'movie_id': movie_id,
                'title': data.get('title'),
                'budget': data.get('budget'),
                'revenue': data.get('revenue'),
                'runtime': data.get('runtime'),
                'release_date': data.get('release_date'),
                'genres': [g['name'] for g in data.get('genres', [])],
                'original_language': data.get('original_language'),
                'popularity': data.get('popularity'),
                'vote_average': data.get('vote_average'),
                'vote_count': data.get('vote_count'),
                'status': data.get('status'),
                'production_companies': [p['name'] for p in data.get('production_companies', [])]
            })

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error for movie {movie_id}: {http_err}")
        except Exception as e:
            print(f"Error fetching movie {movie_id}: {e}")

        time.sleep(0.25)

    return pd.DataFrame(movies_data)

def main():
    try:
        credits = pd.read_csv(CREDITS_CSV_PATH)
        movie_ids = credits['movie_id'].unique()

        print(f"Found {len(movie_ids)} unique movie IDs.")
        df_movies = fetch_movie_metadata(movie_ids)

        df_movies.to_csv(OUTPUT_CSV_PATH, index=False)
        print(f"Saved {len(df_movies)} records to {OUTPUT_CSV_PATH}")

    except Exception as e:
        print(f"Failed to fetch movie data: {e}")

if __name__ == '__main__':
    main()
