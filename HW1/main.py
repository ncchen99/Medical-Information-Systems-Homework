class ChineseWordSegmentation:
    def __init__(self, dictionary_file):
        self.dictionary = self.load_dictionary(dictionary_file)

    def load_dictionary(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        dictionary = {}
        for line in lines[1:]:
            parts = line.strip().split(',')
            word = parts[0]
            if word not in dictionary:
                dictionary[word] = True
        return dictionary

    def segment(self, text):
        segments = []
        text_length = len(text)
        start = 0
        while start < text_length:
            longest_word = None
            for end in range(start + 1, text_length + 1):
                word = text[start:end]
                if word in self.dictionary:
                    if longest_word is None or len(word) > len(longest_word):
                        longest_word = word
            if longest_word is None:
                segments.append(text[start:start + 1])
                start += 1
            else:
                segments.append(longest_word)
                start += len(longest_word)
        return segments


# Example usage:
segmenter = ChineseWordSegmentation("cht_dict.csv")
text = "明天天氣真好"
segments = segmenter.segment(text)
print(segments)
