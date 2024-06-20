def write_file(path, data):
    # ファイルにデータを追記する
    with open(path, 'a', encoding='utf-8') as file:
        file.write(data + '\n')  # 改行を追加して新しい行に追記
