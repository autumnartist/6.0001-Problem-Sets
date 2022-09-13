# 6.0001 Fall 2019
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Autumn Artist
# Collaborators: None
# Time Spent: 7:00
# Late Days Used: None

import string
import math

# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other 


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()

### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text
    """
    word = ""
    word_list = []
    #check for short cuts first, replace with spaces
    if "\n" in input_text:
        input_text = input_text.replace("\n", " ")
    if "\r" in input_text:
        input_text = input_text.replace("\r", " ")
    #add letter to empty string
    #if space or at end of word add word to list
    for i in range(len(input_text)):
        letter = input_text[i]
        if letter == " " and len(word) == 0:
            continue
        elif i == len(input_text)-1:
            word += input_text[-1]
            word_list.append(word)
        elif letter == " " :
            word_list.append(word)
            word = "" 
        elif (letter == " ") == False:
            word += letter
    return word_list

def find_bigrams(single_words):
    """
    Args:
        single_words: list of words in the text, in the order they appear in the text
            all words are made of lowercase characters
    Returns:
        list of bigrams from input text list
    """
    bigrams = []
    #adds word at index i and the next to the bigram list
    for i in range(len(single_words)-1):
        words = f'{single_words[i]} {single_words[i+1]}'
        bigrams.append(words)
    return bigrams

### Problem 2: Word Frequency ###
def count_words(word, word_list):
    """
    Args:
        words: word looking for within list
        word_list: list of words, all are made of lowercase characters
    Returns:
        number of times word is repeated within list
    """
    #counts number of items in word_list
    #if the word matches the one we are looking for
    count = 0
    for i in word_list:
        if word == i:
            count += 1
    return count

def get_frequencies(words):
    """
    Args:
        words: list of words (or bigrams), all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string 
        is a word (or bigram) in words and the corresponding int 
        is the frequency of the word (or bigram) in words
    """
    word_freq = {}
    for i in words:
        #if the word isn't in the dictionary already 
        #add the word and number of times it appears
        if i not in word_freq:
            count = count_words(i, words)
            word_freq[i] = count
    return word_freq

### Problem 3: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.
    
    Args:
        dict1: frequency dictionary of words or bigrams for one text
        dict2: frequency dictionary of words or bigrams for another text
    Returns:
        float, a number between 0 and 1, inclusive 
        representing how similar the texts are to each other
        
        The difference in text frequencies = DIFF sums words 
        from these three scenarios: 
        * If a word or bigram occurs in dict1 and dict2 then 
          get the difference in frequencies
        * If a word or bigram occurs only in dict1 then take the 
          frequency from dict1
        * If a word or bigram occurs only in dict2 then take the 
          frequency from dict2
         The total frequencies = ALL is calculated by summing 
         all frequencies in both dict1 and dict2. 
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    #if any dictionary is empty return 0
    if len(dict1) == 0 or len(dict2) == 0:
        return 0
    diff = float(0)
    sim = float(0)
    total = float(0)
    # is is a word in dict1
    for i in dict1:
        #total is sum of all values in both
        total += float(dict1[i])
        if i in dict2:
            #if i is in both
            diff += abs(float(dict1[i]) - float(dict2[i]))
        else:
            #if i is ONLY in dict1
            diff += float(dict1[i])
    for i in dict2:
        total += float(dict2[i])
        if i not in dict1:
            #if i is ONLY in dict2
            diff+= float(dict2[i])
    #similarity score rounded to 2 decimal places
    sim = round(1-(diff/total), 2)
    return sim

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.
    
    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries
    
    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency. 
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2. 
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    high = 0
    all_words = {}
    word_list = []
    #Making a dict of combined dict1 and dict2
    list1 = dict1.keys()
    for i in list1:
        #if the word isn't in the all_words already add it
        if i not in all_words:
            num = dict1[i]
            all_words[i] = num
                
    list2 = dict2.keys()
    for i in list2:
        if i in all_words:
            #if word is already there add the values from dict2 with dict1
            num = dict2[i] + all_words[i]
            all_words[i] = num
        else:
            #if its not in the all_words dict, add it with its own value
            all_words[i] = dict2[i]
    
    #Finding the highest frequency
    for i in all_words:
        if high < all_words[i]:
            high = all_words[i]
    #Finding if there are multiple words with same highest frequency
    for i in all_words:
        if all_words[i] == high:
            word_list.append(i)
    return word_list

### Problem 5: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_word_frequencies from earlier
    """
    #preping data
    words = load_file(text_file)
    words = prep_data(words)
    num = float(len(words))
    #Makes everything dict
    freq = get_frequencies(words)
    #alter dict, so its freq over total words
    for i in freq:
        freq[i] = freq[i]/num
    return freq

def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculatd as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    files = []
    for i in text_files:
        file = prep_data(load_file(i))
        files.append(file) #list of lists 
    
    word_dict = {}
    count = 0
    for i in files: #goes through each of the lsit
        for x in i: #goes through each item in the list we examine
            word = x
            for j in files: #goes through each list 
                if word in j: #if word in specific list, add 1 to count
                    count += 1
            word_dict[word] = math.log10(len(files)/count)
            count = 0
    return word_dict
    

def get_tfidf(text_file, text_files):
    """
        Args:
            text_file: name of file in the form of a string (used to calculate TF)
            text_files: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)

        """
    file_tf = get_tf(text_file)
    file_idf = get_idf(text_files)
    file_list = []
    #create list
    for i in file_tf.keys():
        if i in file_idf and i not in file_list:
            tfidf = file_tf[i]*file_idf[i]
            file_list.append((i, tfidf))
    
    file_list.sort(reverse = True) #sort list in alphabetical
    
    #turn list to dict
    dict1 = {}
    for i in file_list:
        dict1[i[0]] = i[1]
    #sort dict1 in increasing order based on values
    dict1 = dict(sorted(dict1.items(), key=lambda item: item[1]))
    
    #turn dict to list of truples
    file = []
    for i in dict1:
        file.append((i, dict1[i]))
    return file
    

if __name__ == "__main__":
    pass
    ##Uncomment the following lines to test your implementation
    ## Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/" 
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt') 
    world, friend = prep_data(hello_world), prep_data(hello_friend)
    #print(world) ## should print ['hello', 'world', 'hello']
    #print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 1: Find Bigrams
    world_bigrams, friend_bigrams = find_bigrams(world), find_bigrams(friend)
    #print(world_bigrams) ## should print ['hello world', 'world hello']
    #print(friend_bigrams) ## should print ['hello friends']

    ## Tests Problem 2: Get frequency
    world_word_freq, world_bigram_freq = get_frequencies(world), get_frequencies(world_bigrams)
    friend_word_freq, friend_bigram_freq = get_frequencies(friend), get_frequencies(friend_bigrams)
    #print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    #print(world_bigram_freq) ## should print {'hello world': 1, 'world hello': 1}
    #print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}
    #print(friend_bigram_freq) ## should print {'hello friends': 1}

    ## Tests Problem 3: Similarity
    word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
    bigram_similarity = calculate_similarity_score(world_bigram_freq, friend_bigram_freq)
    #print(word_similarity) ## should print 0.4
    #print(bigram_similarity) ## should print 0.0

    ## Tests Problem 4: Most Frequent Word(s)
    freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    most_frequent = get_most_frequent_words(freq1, freq2)
    #print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    text_file = 'tests/student_tests/hello_world.txt'
    text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(text_file)
    idf = get_idf(text_files)
    tf_idf = get_tfidf(text_file, text_files)
    #print(tf) ## should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    #print(idf) ## should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) ## should print [('hello', 0.0), ('world', 0.10034333188799373)]
