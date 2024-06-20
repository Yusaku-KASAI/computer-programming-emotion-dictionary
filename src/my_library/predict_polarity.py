from my_library.count_word_in_sentence import count_word_in_sentence
def predict_polarity(sentence, positive_words, negative_words):
    emotion = 0
    emotion += count_word_in_sentence(sentence, positive_words)
    emotion -= count_word_in_sentence(sentence, negative_words)
    return emotion
