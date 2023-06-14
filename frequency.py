from romeo_and_juliet import PLAY

"""Removes the punctuation from the input text and returns a list of words."""
def get_words(text):
    """replace all occurrences of the newline character(`\n`) with a space character"""
    clean_text = text.replace("\n", " ")
    """The join() method takes all items in an iterable and joins them into one string"""
    clean_text = "".join(char if char.isalpha() or char == "'" else " " for char in clean_text)
    """The split() method splits a string into a list."""
    words = clean_text.split()
    return words


"""This function takes a list of words as input
and returns a dictionary that contains the frequency of each word in the list """
def words_frequency(words):
    word_frequency_dict = {}
    for word in words:
        if word in word_frequency_dict:
            word_frequency_dict[word] += 1
        else:
            word_frequency_dict[word] = 1
    return word_frequency_dict



"""This function prints the `n` most frequent words and their frequency
counts in a given dictionary `freq` in descending order"""
def top_n_words(freq, n):
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_freq) < n:
        n = len(sorted_freq)
    for i in range(n):
        print(f"{sorted_freq[i][0]}: {sorted_freq[i][1]}")




def main():
    print("Top 50 most frequent words:")
    list_of_words = get_words(PLAY)
    dict_of_word_frequency = words_frequency(list_of_words)
    top_n_words(dict_of_word_frequency,50)

if __name__ == "__main__":
    main()