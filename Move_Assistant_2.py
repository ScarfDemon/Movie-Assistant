# %%
import json
with open("Movie Assistant/movies.json", 'r') as f:
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
    
    while True:
        genre_choice = input('What genre are you interested in? ').lower().capitalize()
        try:
            list(get_unique_genres()).index(genre_choice)
            break
        except ValueError:
            broken = False
            print('{g} is not a genre option. Please try again.'.format(g = genre_choice.capitalize()))
            continue



    return genre_choice

genre_choice = get_user_genre_choice()

def get_movies_in_genre(genre):
    return [movie for movie in movies if movie["genre"] == genre]

movies_in_genre = get_movies_in_genre(genre_choice)

def get_movie_by_index():

    
    movies_in_genre = get_movies_in_genre(genre_choice)

    print(f'Movies in the {genre_choice} genre are: ')
    for index, mov in enumerate(movies_in_genre, start = 1):
        print('{i} : {m}'.format(i = index, m = mov['title']))
    while True:
        selected_movie_index = input("Please insert the index of the movie you would like to select: ")
        try:
            selected_movie_index = int(selected_movie_index)
            selected_movie_index -= 1 #as enumerate set to start at 1
            selected_movie = movies_in_genre[selected_movie_index]
            break
        except ValueError or TypeError:
            broken = False
            print('Index imputted, {s}, must be an integer. Please try again.'.format(s = selected_movie_index))
            continue    
        except IndexError:
            broken = False
            print('Index {s} is out of range. Please try again.'.format(s = selected_movie_index+1))
            continue   

    for key, value in selected_movie.items():
        print("{k}: {v}".format(k = key.capitalize(), v = value))

get_movie_by_index()

    
# %%
