def classify_dictionary_data(dictionary1, dictionary2):
    positive_words = []
    negative_words = []
    # dictionary1
    for item in dictionary1:
        # 最終行の空行を除外
        if len(item) < 2:
            continue
        if item[1] == 'p':
            positive_words.append(item[0])
        if item[1] == 'n':
            negative_words.append(item[0])
    #dictionary2
    for item in dictionary2:
        # 最終行の空行を除外
        if len(item) < 2:
            continue
        if item[0] == "ネガ（経験）" or "ネガ（評価）":
            items=""
            for i in range(1,len(item)):
                items=items+item[i]
            negative_words.append(items)
        elif item[0] == "ポジ（評価）" or "ポジ（経験）":
            items=""
            for i in range(1,len(item)):
                items=items+item[i]
            positive_words.append(items)
    return positive_words, negative_words
