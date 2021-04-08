def preprocessing(text):
    preprocessed_words = []
    
    stemmer = PorterStemmer()

    for word in word_tokenize(text.lower()):
        if word not in punctuation_set and word not in english_stopwords:
            preprocessed_words.append(stemmer.stem(word))

    return preprocessed_words