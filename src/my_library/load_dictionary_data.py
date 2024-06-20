from my_library.read_file import read_file
def load_dictionary_data(path):
    data = read_file(path)
    # 読み込んだデータを改行ごとに区切り配列に変換
    lines = data.split('\n')
    # 各行を[単語,極性,説明?]の形に分割
    dictionary = [line.split() for line in lines]
    # 結果を返却
    return dictionary
