import os
import math
#from gensim.models import FastText # Alternative: sister

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
                text += line.strip("\n") + " "

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


def encode_splits(splits, encoder):
    """Encode the list of parts of the subtitles/text
    
    args: splits (list of parts of the subtitles/text), encoder (string,
    name of the encoder to be used for encoding the splits)
    
    return: splits_encoded (list of parts of the subtitles/text, encoded 
    with word2vec)"""


def encode_labels(labels):
    """Encode the list of labels
    
    args: labels (list of the labels of the subtitle splits)
    
    return: labels_encoded (list of the labels of the subtitle splits,
    encoded as a list of integers)"""
    
    label_dict = {"action": 0, "adventure": 1, "comedy": 2, "drama": 3,
                  "fantasy": 4, "history": 5, "scifi": 6, "sport": 7,
                  "superhero": 8, "western": 9}
    
    genre = labels[0]

    labels_encoded = [label_dict[genre]] * len(labels)

    return labels_encoded


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

    """ x = []
    y = []

    for movie in movie_list:
        text = load_subtitles(movie)
        genre = (str((movie.split("/"))[-2])).lower()
        splits, labels = split_label_subtitles(text, genre, n_splits)

        x += encode_splits(splits, encoder)
        y += encode_labels(labels)

    return x, y """


# FOR TEST PURPOSES ONLY

#path_bttf = "C:/Users/Tim.O/Documents/Studium/4. Semester/Deep Learning for NLP/ABSCHLUSSPROJEKT/Movie collection/SCIFI/Back To The Future (1985).txt"
#path_indy3 = "C:/Users/Tim.O/Documents/Studium/4. Semester/Deep Learning for NLP/ABSCHLUSSPROJEKT/Movie collection/ADVENTURE/Indiana Jones and the Last Crusade (1989).txt"
#path_shawsahnk = "C:/Users/Tim.O/Documents/Studium/4. Semester/Deep Learning for NLP/ABSCHLUSSPROJEKT/Movie collection/DRAMA/The Shawshank Redemption (1994).txt"

#movie_list = [path_bttf, path_indy3, path_shawsahnk]

genres = ["action", "adventure", "comedy", "drama", "fantasy", "history", "scifi", "sport", "superhero", "western"]
movie_list = create_movie_list(genres)
print(movie_list)

create_dataset(movie_list, 100)

#print("Splits:")
#print(x)
#print("Labels:")
#print(y)

#text = load_subtitles(path_bttf)
#print(text)

#splits, labels = split_label_subtitles(text, "scifi", 100)
#print(splits)
#print()
#print(labels)
#print()
#labels_encoded = encode_labels(labels)
#print(labels_encoded)