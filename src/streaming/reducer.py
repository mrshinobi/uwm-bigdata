#!/usr/bin/python3
import sys


def parse_line(fields):
    return fields[0], int(fields[1]), int(fields[2])


class Word:
    def __init__(self, word, count, word_len):
        self.word = word
        self.count = count
        self.word_len = word_len


def main():
    word_counters = {}

    for line in sys.stdin:
        fields = line.split(sep=",")

        word, count, word_len = parse_line(fields)

        if word in word_counters:
            existing_word = word_counters[word]
            existing_word.count = existing_word.count + count

            word_counters[word].count += count

        else:
            word_counters[word] = Word(word, count, word_len)

    for keyword, word in sorted(word_counters.items()):
        print(keyword, word.count, sep=",")


if __name__ == "__main__":
    main()
