class WordLengthIterator:

    def __init__(self, word_list):
        self.word_list = word_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.word_list):
            word = self.word_list[self.index]
            self.index += 1
            return len(word)
        else:
            raise StopIteration

words = ["This", "is", "a", "class", "iterator"]

class_iter = WordLengthIterator(words)

print(f"\nТип об'єкта (клас): {type(class_iter)}")

print("Результат роботи ітератора-класу:")
for length in class_iter:
    print(length)