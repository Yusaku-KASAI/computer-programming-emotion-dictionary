import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)

from my_library.load_input_data import load_input_data
from my_library.load_dictionary_data import load_dictionary_data
from my_library.classify_dictionary_data import classify_dictionary_data
from my_library.predict_polarity import predict_polarity
from my_library.write_file import write_file

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
sentences = load_input_data(os.path.join(data_dir, 'data.txt'))

dictionary1 = load_dictionary_data(os.path.join(data_dir, 'dictionary1.txt'))
dictionary2 = load_dictionary_data(os.path.join(data_dir, 'dictionary2.txt'))

positive_words, negative_words = classify_dictionary_data(dictionary1, dictionary2)
for positive_word in positive_words:
    write_file(os.path.join(data_dir, 'sample.txt'), positive_word)

for sentence in sentences:
    emotion = predict_polarity(sentence, positive_words, negative_words)
    result = str(emotion)
    if emotion > 0:
        result += " positive"
    if emotion < 0:
        result += " negative"
    if emotion == 0:
        result += " neutral"
    write_file(os.path.join(data_dir, 'result.txt'), result)
