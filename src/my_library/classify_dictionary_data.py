def classify_dictionary_data(dictionary1, dictionary2):
    positive_words = []
    negative_words = []
    # dictionary1のみ処理
    for item in dictionary1:
        # 最終行の空行を除外
        if len(item) < 2:
            continue
        if item[1] == 'p':
            positive_words.append(item[0])
        if item[1] == 'n':
            negative_words.append(item[0])
    return positive_words, negative_words
