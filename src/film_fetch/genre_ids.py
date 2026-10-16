# Hardcoded genres and ids
# NOTE: Could query TMDB for this list as well, hardcoded to prevent unnecessary API calls
GENRES = {
    "Action": 28,
    "Adventure": 12,
    "Animated": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Sci-Fi": 878,
    "Thriller": 53,
    "TV Movie": 10770,
    "War": 10752,
    "Western": 37,
}

# Hardcoded ids and genres (Flips keys and values)
GENRE_IDS = {id: genre for genre, id in GENRES.items()}
