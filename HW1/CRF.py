import pycrfsuite
import re

class CRFChineseWordSegmentation:
    def __init__(self, feature_func=None):
        self.tagger = pycrfsuite.Tagger()
        if feature_func is None:
            self.feature_func = self.basic_features
        else:
            self.feature_func = feature_func

    def train(self, X_train, y_train, model_file):
        trainer = pycrfsuite.Trainer(verbose=False)
        for xseq, yseq in zip(X_train, y_train):
            trainer.append(xseq, yseq)
        trainer.train(model_file)

    def load_model(self, model_file):
        self.tagger.open(model_file)

    def segment(self, text):
        features = [self.feature_func(text, i) for i in range(len(text))]
        tags = self.tagger.tag(features)
        return self.tags_to_segments(text, tags)

    def tags_to_segments(self, text, tags):
        segments = []
        start = 0
        for i, tag in enumerate(tags):
            if tag == 'B' or tag == 'S':
                start = i
            if tag == 'E' or tag == 'S':
                segments.append(text[start:i+1])
        return segments

    def basic_features(self, text, i):
        features = {
            'char': text[i],
            'bias': 1.0,
        }
        return features

def load_dictionary(file):
    dictionary = {}
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[1:]:
        parts = line.strip().split(',')
        word = parts[0]
        dictionary[word] = True
    return dictionary

def prepare_training_data(dictionary):
    X_train = []
    y_train = []
    for word in dictionary:
        X_train.append([{'char': c} for c in word])
        y_train.append([label for label in get_label(word)])
    return X_train, y_train

def get_label(word):
    labels = []
    if len(word) == 1:
        labels.append('S')
    else:
        labels.append('B')
        for i in range(1, len(word) - 1):
            labels.append('M')
        labels.append('E')
    return labels

def feature_func(text, i):
    char = text[i]
    features = {
        'char': char,
        'bias': 1.0,
        'is_first': i == 0,
        'is_last': i == len(text) - 1,
        'prev_char': '' if i == 0 else text[i - 1],
        'next_char': '' if i == len(text) - 1 else text[i + 1],
    }
    return features

# Load the dictionary
dictionary = load_dictionary("cht_dict.csv")

# Prepare the training data
X_train, y_train = prepare_training_data(dictionary)

# Train the CRF model
segmenter = CRFChineseWordSegmentation(feature_func)
segmenter.train(X_train, y_train, "crf_model")

# Load the trained model
segmenter.load_model("crf_model")

# Segment the text
text = "你應該趁年輕力壯時認真打拚，日後才能有美好前程。"
segments = segmenter.segment(text)
print(segments)
