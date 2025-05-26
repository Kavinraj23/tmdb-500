import pandas as pd
import ast

MOVIES_PATH = 'data/tmdb_5000_movies_fetched.csv'
CREDITS_PATH = 'data/tmdb_5000_credits.csv'
OUTPUT_PATH = 'data/merged_movies_credits.csv'

movies_df = pd.read_csv(MOVIES_PATH)
credits_df = pd.read_csv(CREDITS_PATH)

merged_df = pd.merge(movies_df, credits_df, on='movie_id', how='left')

# extract top 3 actors and director from cast and crew json strings
def extract_top_cast(cast_str):
    try:
        cast_list = ast.literal_eval(cast_str)
        return [actor['name'] for actor in cast_list[:3]]
    except:
        return []

def extract_director(crew_str):
    try:
        crew_list = ast.literal_eval(crew_str)
        for person in crew_list:
            if person['job'] == 'Director':
                return person['name']
        return None
    except:
        return None

merged_df['top_cast'] = merged_df['cast'].apply(extract_top_cast)
merged_df['director'] = merged_df['crew'].apply(extract_director)

merged_df.drop(columns=['cast', 'crew'], inplace=True)

merged_df.to_csv(OUTPUT_PATH, index=False)
print(f"Merged data saved to {OUTPUT_PATH} with {merged_df.shape[0]} rows")
