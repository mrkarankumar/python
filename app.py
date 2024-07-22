import pickle
import streamlit as st
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to fetch movie poster using The Movie Database API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (4xx or 5xx)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None

# Function to recommend movies based on selected movie
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []

        # Fetch posters in parallel
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(fetch_poster, movies.iloc[i[0]].movie_id) for i in distances[1:6]]
            for future in as_completed(futures):
                poster_url = future.result()
                if poster_url:
                    recommended_movie_posters.append(poster_url)
                    recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters

    except IndexError:
        st.error("Movie not found in the database.")
        return [], []
    except Exception as e:
        st.error(f"Recommendation error: {e}")
        return [], []

# Main Streamlit application
def main():
    st.header('Movie Recommender System')

    # Load data from pickle files
    try:
        movies = pickle.load(open('model/movie_list.pkl', 'rb'))
        similarity = pickle.load(open('model/similarity.pkl', 'rb'))

        movie_list = movies['title'].values
        selected_movie = st.selectbox(
            "Type or select a movie from the dropdown",
            movie_list
        )

        if st.button('Show Recommendation'):
            recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
            for name, poster in zip(recommended_movie_names, recommended_movie_posters):
                st.text(name)
                st.image(poster, width=200)

    except FileNotFoundError:
        st.error("Pickle files not found. Please check your data files.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
