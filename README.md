# Movie Assistant
## Summary
Need help choosing what movie to watch next? This movie assistant can help! 

Choose a genre you are interested in, and out of a dataset of movies, the chosen genre is filtered and enumerated. 
You can then choose the index of the movie you would like to view!

## Explanation
The movie assistant works by first reading in a `.json` file containing data of over 250 movies extracted from IMDB. 
The data is a list of dictionaries, where each dictionary contains a movie and its information including name, genre, and plot.

The data is used to extract the unique genres available. This is then presented to the user where the user is asked what genre they are interested in. 

The movies of that genre are then filtered out and enumerated such that the user can then select the index of the movie they would like to view the full details of.

`Error handling` is used to make sure the user puts in a valid input for the genre they are interested in and for the index of the movie they would like to view.

