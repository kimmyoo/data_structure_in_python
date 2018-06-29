import os
file_path = os.path.join("text_files", "novel.txt")

#freq is a dictionary to hold each word
# and its frequency (key: value) pairs
freq = {}
max_len = 0
longest_word = ''
with open(file_path)as f_object:
    # read() file as a string; split the string into pieces in a list
    for piece in f_object.read().lower().split():
        word = ''.join(c for c in piece if c.isalpha())
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
        if word: # not empty string
            # dict.get(key, [default]), if key exists, get() returns 
            # the value associated with that key; if key doesn't exist
            # default value is assigned
            freq[word] = 1 + freq.get(word, 0)
    max_word = ''
    max_count = 0
    # loop through the dictionary and find the longest word
    for (w, c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c
    print (max_word, max_count)
    print (longest_word, ":", max_len)
    print (freq)
