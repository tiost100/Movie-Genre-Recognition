# “Don't judge a movie by its cover but by its subtitles” - Classifying with Deep Learning Architectures and LLMs


## Table of Contents
1. [General Info](#general-info)
2. [Requirements](#requirements)
3. [Download](#download)
4. [Usage](#usage)
5. [Technologies/Sources](#technologiessources)
6. [Licence](#licence)

## General Info
In this project done in the *Deep Learning for NLP* class at *Heinrich Heine Univerität Düseldorf*, we (Philipp Bauer, Jefferson Fonseca and Tim Ostrolucký) used Deep Learning architectures and fine-tuned the BERT and fastText language models to classify movies based on their English subtitles. In order to do that, we manually created a dataset consisting of 100 movies from 10 different genres for the training of the classifiers; the subtitles were downloaded from the opensubitles.org website, tranformed to human-readable .txt-format and the subtitles of every movie were split into 100 parts of approximately equal length to obtain more data points.

The Deep Learning model can be found in the Jupyter notebook `sentiment_classifier.ipynb`, as in the first step every subtitle split was assigned a sentiment score between -1 and 1 using the VADER sentiment analysis tool. The classifiers based on the BERT and fastText LLMs can be found in the notebook with the corresponding names (`bert/fasttext_classifier.ipynb`). The `utils.py` program is used to generate the movie corpus on which these models are trained, combining the collections of movies from the different genres (in the folders `ACTION/ADVENTURE/COMEDY/...`) into one big dataset. It also creates two test files for the evaluation of the models, stored in the `Test` folder.

For further information, please see the paper.

## Requirements
In order to run the `utils.py` program please make sure you have installed Python Version **3.11.8.** As the other programs are Jupyter notebooks, you do not need to install anything else.

## Download
To be able to run the project on your computer, please clone this GitHub repository by running the following command in your terminal; you have to run the terminal as administrator:
<pre>git clone https://github.com/tiost100/Movie-Genre-Recognition</pre>

## Usage
### utils.py
To run the `utils.py` program please do as followed:
* Open your Command Prompt or Windows Terminal.
* Navigate to the directory into where you have stored this repository using the `cd` command.
* Type `python` followed by the name of the Python file, including the `.py` extension.
* Press Enter to run the Python file.

### bert/fasttext/sentiment_classifier.ipynb
To run the Jupyter notebooks please do as followed: 
* Open Google Colab: https://colab.research.google.com/
* Click *Upload Notebook* in the Open Notebook window and select the desired notebook.
* Change runtime type to ***T4 GPU***.
* It is necessary that you run the code cells in the correct order as the individual program parts build on each other. 

## Technologies/Sources
- codebasics. (2022, October 28). fastText tutorial | Text Classification Using fastText | NLP Tutorial For Beginners - S2 E13 [Video]. YouTube. Retrieved March 21, 2024, from https://www.youtube.com/watch?v=Cq_pbQYO3M8
- Code in Action. (2021, July 26). Mastering Transformers | 5. Fine-Tuning Language models for text Classification [Video]. YouTube. Retrieved February 27, 2024, from https://www.youtube.com/watch?v=rR0vHaEOV_k
- Devlin, J., Chang, M., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv (Cornell University). https://arxiv.org/pdf/1810.04805v2
- Google Colaboratory. (n.d.). Retrieved February 27, 2024, from https://colab.research.google.com/
- Happy Scribe Untertitel-Konverter. (n.d.). Retrieved March 19, 2024, from https://www.happyscribe.com/de/untertitel-tools/untertitel-converter
- Hutto, C. J., & Gilbert, É. (2014). VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1), 216–225. https://doi.org/10.1609/icwsm.v8i1.14550
- Joulin, A., Grave, É., Bojanowski, P., & Mikolov, T. (2016). Bag of tricks for efficient text classification. arXiv (Cornell University). https://arxiv.org/pdf/1607.01759.pdf
- Opensubtitles.org. (n.d.). Retrieved March 19, 2024, from https://www.opensubtitles.org/
- Rothman, D. (2022). Transformers for natural language processing: Build, train, and fine-tune deep neural network architectures for NLP with Python, Hugging Face, and OpenAI’s GPT-3, ChatGPT, and GPT-4. Packt Publishing Ltd.
- Yıldırım, S., & Chenaghlu, M. A. (2021). Mastering transformers: Build state-of-the-art models from scratch with advanced natural language processing techniques. Packt Publishing Ltd.

**Related:**
- Kim, J., Kim, J.-K., & Choi, J. (2021). Sequential Movie Genre Prediction Using Average Transition Probability with Clustering. Applied Sciences, 11(24), 11841. https://doi.org/10.3390/app112411841
- Vishwakarma, D. K., Jindal, M., Mittal, A., & Sharma, A. (2021). Multilevel profiling of situation and dialogue-based deep networks for movie genre classification using movie trailers. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2109.06488

## Licence
We are not aware of any copyright restrictions of the material.
