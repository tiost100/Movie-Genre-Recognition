import math
from gensim.models import word2vec

def load_subtitles(filepath):
    """Load movie subtitle txt-file, and remove blank lines and line breaks

    args: filepath (string, full path of the subtitle file)

    return: text (string of continuous text without blank lines and line 
    breaks)

    note: the file path depends on the storage location of the file on the 
    computer, and can vary from computer to computer
    """

    text = ""

    with open(filepath, "r", encoding="utf-8") as infile:
        for line in infile:
            if line.strip():
                text += line.strip("\n") + " "

    return text


def split_label_subtitles(text, genre, n_splits):
    """Split the given subtitles/text into n_splits parts
    
    args: text (subtitles transformed into continuous text), genre (movie
    genre of the film), n_split (number of splits, integer)
    
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


def encode_splits(splits):
    """"""


def encode_labels(labels):
    """Encode the list of labels
    
    args: labels (list of the labels of the subtitle splits)
    
    return: labels_encoded (list of the labels of the subtitle splits,
    encoded of as a list of integers)"""
    
    label_dict = {"action": 0, "adventure": 1, "comedy": 2, "drama": 3,
                  "fantasy": 4, "history": 5, "scifi": 6, "sport": 7,
                  "superhero": 8, "western": 9}
    
    genre = labels[0]

    labels_encoded = [label_dict[genre]] * len(labels)

    return labels_encoded



path_bttf = "C:/Users/Tim.O/Documents/Studium/4. Semester/Deep Learning for NLP/ABSCHLUSSPROJEKT/Movie collection/SCIFI/Back To The Future (1985).txt"

text = load_subtitles(path_bttf)
#print(text)

splits, labels = split_label_subtitles(text, "scifi", 100)
print(splits)
print()
print(labels)
print()
labels_encoded = encode_labels(labels)
print(labels_encoded)