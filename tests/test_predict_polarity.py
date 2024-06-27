import pytest
import os
import sys

# プロジェクトのルートパスを設定
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)

# 自作ライブラリのインポート
import src.my_library.predict_polarity as predict_polarity
import src.my_library.classify_dictionary_data as classify_dictionary_data

classify_dictionary_data.classify_dictionary_data(dictionary1,dictionary2)
def test_predict_positive():
    # ポジティブな入力に対する予測結果をテスト
    assert predict_polarity.predict_polarity("猫と一緒に過ごす時間が一番の癒し。",positive_words,negative_words)>0
    

def test_predict_negative():
    assert predict_polarity.predict_polarity("猫と一緒に過ごす時間が一番の癒し。",positive_words,negative_words)<0

def test_predict_neutral():
    # 中立的な入力に対する予測結果をテスト
    assert predict_polarity.predict_polarity("猫と一緒に過ごす時間が一番の癒し。",positive_words,negative_words)==0
