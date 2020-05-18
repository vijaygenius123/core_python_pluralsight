from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')

story_words_decoded = []
story_words = []

for line in story:
    line_words_decoded = line.decode('utf-8').split()
    line_words = line.split()
    for word in line_words:
        story_words.append(word)
    for word in line_words_decoded:
        story_words_decoded.append(word)
story.close()

print(story_words)
print(story_words_decoded)
