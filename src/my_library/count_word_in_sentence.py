def count_word_in_sentence(sentence, word_list):
    count = 0
    for word in word_list:
        count += sentence.lower().count(word.lower())
    return count
