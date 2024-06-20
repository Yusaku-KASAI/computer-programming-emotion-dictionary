def read_file(path):
    # ファイルを開いて内容を読み込む
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    # 読み込んだデータを返却
    return data
