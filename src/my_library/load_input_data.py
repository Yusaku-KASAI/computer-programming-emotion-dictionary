from my_library.read_file import read_file
def load_input_data(path):
    data = read_file(path)
    # 読み込んだデータを改行ごとに区切り配列に変換
    lines = data.split('\n')
    # 結果を返却
    return lines
