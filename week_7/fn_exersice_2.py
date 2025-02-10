# 2. Write a program that takes a list of words and a minimum length, 
# and returns a new list
# containing only the words longer than the minimum length.

def filter_words(words, min_length):
    # int empty list
    filtered = []

    # loop through the words
    for word in words:
        if(len(word)) > min_length:
           filtered.append(word)
    return filtered

words = ['hello','world','python','programming']

filtered_words = filter_words(words, 6)

print(filtered_words) # ['python', 'programming']
