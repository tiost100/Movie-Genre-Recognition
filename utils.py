import os
import math

# Get the full path of the directory where the current file is located
dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = dir_path.replace('\\','/')

def load_subtitles(filepath):
    """Load movie subtitle txt-file, and remove blank lines and line breaks

    args: filepath (string, full path of the subtitle file)

    return: text (string of continuous text without blank lines and line 
    breaks)

    note: the file path depends on the storage location of the file on the 
    computer, and can vary from computer to computer
    """

    text = ""

    with open(filepath, "r", encoding="latin-1") as infile:
        for line in infile:
            if line.strip():
                text += line.strip("\n").lower() + " "

    return text


def split_label_subtitles(text, genre, n_splits):
    """Split the given subtitles/text into n_splits parts
    
    args: text (subtitles transformed into continuous text), genre (movie
    genre of the film), n_split (integer, number of splits)
    
    return: splits (list of parts of the subtitles/text), labels (list of
    the labels of the subtitle splits)"""

    splits = []

    words = text.split()
    n_words = len(words)
    split_length = math.ceil(n_words/n_splits)

    for i in range(n_splits):
        text_split = ""

        for j in range(split_length):
            index = j + (i * split_length)

            if index < len(words):
                text_split += words[index] + " "

        splits.append(text_split)

    labels = [genre] * n_splits

    return splits, labels


def create_movie_list(genres):
    """Creates a list of the subtitle filepaths
    
    args: genres (a list of the movie genres)
    
    return: movie_list (list of the subtitle filepaths)"""

    movie_list = []

    for genre in genres:
        genre = genre.upper()

        for film in os.listdir(dir_path + "/" + genre):
            movie_list.append(dir_path + "/" + genre + "/" + film)

    return movie_list


def create_dataset(movie_list, n_splits):
    """Create the dataset, i.e. a .csv-file consisting of one column with
    labels and one column with subtitle splits
    
    args: movie_list (list of the subtitle filepaths), n_splits (integer, 
    number of splits)
    
    return: None"""

    with open(f'{dir_path}/movies.csv', 'w', encoding='utf-8') as outfile:
        for movie in movie_list:
            text = load_subtitles(movie)
            genre = (str((movie.split("/"))[-2])).lower()
            splits, labels = split_label_subtitles(text, genre, n_splits)

            for i in range(len(labels)):
                splits[i] = splits[i].replace(";", ",") 
                outfile.write(labels[i] + ";" + splits[i] + "\n")


# Create the dataset
genres = ["action", "adventure", "comedy", "drama", "fantasy", "history", "scifi", "sport", "superhero", "western"]
movie_list = create_movie_list(genres)

create_dataset(movie_list, 100)
print("Dataset created")


# Create a test file (movie "Showtime")
with open(f'{dir_path}/Test/showtime.csv', 'w', encoding='utf-8') as outfile:
    test_text = load_subtitles(dir_path + "/Test/Showtime (2002).txt")
    test_genre = "action"
    test_splits, test_labels = split_label_subtitles(test_text, test_genre, 100)

    for i in range(len(test_labels)):
        test_splits[i] = test_splits[i].replace(";", ",") 
        outfile.write(test_labels[i] + ";" + test_splits[i] + "\n")

# Create a test file (movie "Equalizer 3")
with open(f'{dir_path}/Test/equalizer.csv', 'w', encoding='utf-8') as outfile:
    test_text = load_subtitles(dir_path + "/Test/The Equalizer 3 (2023).txt")
    test_genre = "action"
    test_splits, test_labels = split_label_subtitles(test_text, test_genre, 100)

    for i in range(len(test_labels)):
        test_splits[i] = test_splits[i].replace(";", ",") 
        outfile.write(test_labels[i] + ";" + test_splits[i] + "\n")

print("Test files created")