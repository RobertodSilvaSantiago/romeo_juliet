# romeo_juliet

This code performs the following tasks:

It imports the PLAY variable from the romeo_and_juliet module. The PLAY variable likely contains the text of the play "Romeo and Juliet".

The get_words function takes a text input and removes punctuation from it. It replaces newline characters (\n) with spaces, removes non-alphabetic characters except for apostrophes ('), and splits the cleaned text into a list of words. The function returns this list of words.

The words_frequency function takes a list of words as input and creates a dictionary that stores the frequency of each word in the list. It iterates over the words, and if a word is already present in the dictionary, it increments its count. If a word is not in the dictionary, it adds it with a count of 1. The function returns the word frequency dictionary.

The top_n_words function takes a word frequency dictionary and a number n as input. It sorts the items in the dictionary based on their values (frequency) in descending order. If the length of the sorted frequency list is less than n, it adjusts n to be equal to the length of the list. It then prints the top n most frequent words and their corresponding frequency counts.

The main function is the entry point of the program. It first prints a message indicating that it will display the top 50 most frequent words. It then calls the get_words function on the PLAY variable to obtain a list of words. Next, it passes the list of words to the words_frequency function to get the word frequency dictionary. Finally, it calls the top_n_words function to print the top 50 most frequent words and their counts.

The if __name__ == "__main__": condition ensures that the main function is only executed when the script is run directly and not imported as a module.

When you run the code, it will output the top 50 most frequent words from the "Romeo and Juliet" play along with their counts.
