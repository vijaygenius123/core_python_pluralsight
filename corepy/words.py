#!/usr/bin/env python3
import sys
from urllib.request import urlopen


def fetch_words(url):
    """fetch data from given url"""
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    return story_words


def print_words(story_words):
    """print the words"""
    print(story_words)


def main(url):

    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    main(sys.argv[1])  # Argument From Commandline
