# %%
import json
with open('movies.json', 'r') as f:
    movies = json.load(f)

print(len(movies))

# %%

def get_user_genre_choice():
    def get_unique_genres():
        genres = []
        for i in movies:
            genres.append(i['genre'])
        genres = set(genres)
        return genres
    
    genres = get_unique_genres()
    print('The genre options are: ')
    for i in genres:
        print(i)
    
    genre_choice = input('What genre are you interested in? ')

    return genre_choice
# %%
genre_choice = get_user_genre_choice()
# %%
def get_movies_in_genre(genre):
    return [movie for movie in movies if movie["genre"] == genre]


# %%
def get_movie_by_index():
    print(f'Movies in the {genre_choice} are: ')
    movie_options_with_info = get_movies_in_genre(genre_choice)
    movie_options = dict() #enumerated dict
    for i,j in enumerate(get_movies_in_genre(genre_choice), start = 1):
        movie_options[i] = j['title']
        print(i,':',j['title'])
    
    selected_movie_index = int(input("Please insert the index of the movie you would like to select: "))
    selected_movie = movie_options_with_info[selected_movie_index-1]

    for detail in selected_movie:
        print(detail.capitalize(), ":", selected_movie[str(detail)])

get_movie_by_index()

    
# %%
