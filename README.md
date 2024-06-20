# computer-programming-emotion-dictionary

## 概要
このプロジェクトは、テキストデータを処理し、感情分析を行うシステムです。以下のモジュールがあります：
- ファイルデータの読み込み([read_file.py](src/my_library/read_file.py))
- 感情を判定するデータの読み込み([load_input_data.py](src/my_library/load_input_data.py))
- 辞書データの読み込み([load_dictionary_data.py](src/my_library/load_dictionary_data.py))
- 辞書データの調整([classify_dictionary_data.py](src/my_library/classify_dictionary_data.py))
- 単語の出現回数の計算([count_word_in_sentence.py](src/my_library/count_word_in_sentence.py))
- 感情の予測([predict_polarity.py](src/my_library/predict_polarity.py))
- ファイルの書き込み([write_file.py](src/my_library/write_file.py))

## ディレクトリ構成
```
my_project/
├── src/
│   ├── main.py
│   └── my_library/
│       ├── read_file.py
│       ├── load_input_data.py
│       ├── load_dictionary_data.py
│       ├── classify_dictionary_data.py
│       ├── count_word_in_sentence.py
│       ├── predict_polarity.py
│       └── write_file.py
├── data/
│   ├── dictionary1.txt
│   ├── dictionary2.txt
│   ├── data.txt
│   └── result.txt
├── logs/ 
├── tests/
│   ├── test_read_file.py
│   ├── test_load_input_data.py
│   ├── test_load_dictionary_data.py
│   ├── test_classify_dictionary_data.py
│   ├── test_count_word_in_sentence.py
│   ├── test_predict_polarity.py
│   └── test_write_file.py
├── requirements.txt
└── README.md
```

## セットアップ

### 依存関係のインストール
以下のコマンドを実行して、必要なPythonパッケージをインストールします：
```sh
pip install -r requirements.txt
```

### データファイルの準備
`data/`ディレクトリに以下のファイルを配置してください：
- `dictionary1.txt`
- `dictionary2.txt`
- `data.txt`

## 使用方法

### main.pyの実行
以下のコマンドを実行して、プロジェクトのメインスクリプトを実行します：
```sh
python3 src/main.py
```

このスクリプトは以下の手順で動作します：
1. 入力データ(`data.txt`)の読み込み
2. 辞書データ(`dictionary1.txt`および`dictionary2.txt`)の読み込み
3. 辞書データ(`dictionary1.txt`および`dictionary2.txt`)の調整
3. 入力データの各文の感情を調整された辞書データから予測
4. 結果を`result.txt`に出力

## テスト
プロジェクトにはユニットテストが含まれています。以下のコマンドを実行してテストを実行できます：
```sh
python -m unittest discover -s tests
```

## ライセンス

## 貢献

## 作者

## 注意
```
この`README.md`は、プロジェクトの基本的な情報を提供し、セットアップや使用方法を明確にするためのものです。また、このプロジェクトは未完成です。必要に応じて、プロジェクトの詳細に合わせて修正してください。
現時点ではPythonの外部ライブラリも使用していないので依存関係のインストールを行う必要がありません。
現時点ではユニットテストは作成されていませんので、テストのコマンドを実行してもテストされません。
```
