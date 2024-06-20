def count_word_in_sentence(sentence, word_list):
    count = 0
    # listからwordの取り出し
    for word in word_list:
        # sentenceにおけるwordの出現回数分countに加算
        count += sentence.lower().count(word.lower())
    return count
