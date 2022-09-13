# Problem Set 4B
# Name: Autumn Artist
# Collaborators: Daniel Ajayi
# Time Spent: 2:00
# Late Days Used: 0

import string
import random
import json

### HELPER CODE ###
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
    for i in range(len(input_text)):
        letter = input_text[i]
        if i == len(input_text)-1:
            word += input_text[-1]
            word_list.append(word)
        elif letter == " ":
            word_list.append(word)
            word = "" 
        elif (letter == " ") == False:
            word += letter
    return word_list

def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            self.message_text (string, determined by input text)
        '''
        self.message_text = input_text

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by. -95<shift<95

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        
        #get number assigned to each character
        index = ord(char)
        #index + shift is less than or equal to the max (126)
        if (index + shift) <= 126 and (index + shift) >= 32:
            index += shift
        elif index + shift > 126:
            #change the shift by findin how far from max 
            shift = (shift + index) % 126
            #add new shift to 31, to account for jump from 126 to 32
            index = 31+shift
        else:
            #Case: index+shift <32
            num = index-32
            num2 = (-1*shift) - num
            index = 127- num2
        #convert new index back to the character and return
        word = chr(index)
        return word
        
    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to self.message_text.
        For each character in self.message_text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt self.message_text
                        len(pad) == len(self.message_text)
                        elements of pad are in the range (-95, 95)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        text = Message(self.message_text)
        word = Message.get_message_text(text)
        #index to count the elements in the list (pad)
        index = 0
        #new string for the new ciphered text
        ciphertext = ""
        #individually shift each character of the string
        for i in word:
            letter = text.shift_char(i, pad[index])
            #add shifted letter to new word
            ciphertext += letter
            index += 1
        return ciphertext

class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad!=None then len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        A PlaintextMessage object inherits from Message. It has three attributes:
            self.message_text (string, determined by input_text)
            self.pad (list of integers, determined by pad
                or generated from self.generate_pad() if pad==None)
            self.encrypted_message_text (string, input_text encrypted using self.pad)
        '''
        self.message_text = input_text
        # if the pad isn't there then pad = None
        if pad == None:
            self.pad = self.generate_pad()
        else:
            self.pad = pad
        #Using the apply_pad to make an encrypted message with self.pad given
        word = Message(self.message_text)
        self.encrypted_message_text = word.apply_pad(self.pad)
        

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt self.message_text.

        The pad should be generated by making a new list and for each character
            in self.message_text chosing a random number in the range [0, 95) and
            adding that number to the list.
        Hint: random.randint(a,b) returns a random integer N such that a<=N<=b

        Returns: (list of integers) the new one time pad
        '''
        #pad must equal len of message_text
        word_length = len(self.message_text)
        pad = []
        for i in range(word_length):
            #for each letter in the message_text - assigned random int
            #Excluded 95, so do (0,94)
            num = random.randint(0, 94)
            pad.append(num)
            
        return pad

    def get_pad(self):
        '''
        Used to safely access self.pad outside of the class

        Returns: a COPY of self.pad
        '''
        #copy of pad and return copy
        pad_copy = self.pad.copy()
        return pad_copy

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text

    def change_pad(self, new_pad):
        '''
        Changes self.pad of the PlaintextMessage, and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        Returns: nothing
        '''
        #Update pad
        self.pad = new_pad
        word = Message(self.message_text)
        #Update encrypted text
        self.encrypted_message_text = word.apply_pad(self.pad)


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
                            on the given file WORDLIST_FILENAME)
        '''
        self.message_text = input_text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self, pad):
        '''
        Decrypts self.message_text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        Returns: the plaintext message
        '''
        
        #Encrypted text
        text = Message(self.message_text)
        word = text.get_message_text()
        plaintext = ""
        for i in range(len(pad)):
            #Reverts to regular by doing the shift with the negative number
            plaintext += text.shift_char(word[i], pad[i]*-1)    
        return plaintext

    def decrypt_message_try_pads(self, pads):
        '''
        Finds the pad in pads which when used to decrypt self.message_text results
        in a plaintext with the most valid English words. In the event of ties return
        the first pad that results in the maximum number of valid English words.

        pads (list of lists of ints): A list of pads which might have been used
            to encrypt self.message_text

        Returns: (list of ints, string) a tuple of the best pad and the decrypted plaintext
        '''
        #list to keep count of english words in each list
        en_words = []
        #going through each list in the list
        for i in pads:
            #string for the decrypted message using the pad
            text = self.decrypt_message(i)
            #changes the string to a list of words
            word_list = prep_data(text)
            num_words = 0
            #checks each word in the list to see if its english 
            #if english --> adds 1
            for i in word_list:
                if is_word(self.valid_words, i):
                    num_words += 1
            #adds number of english words to the a list
            en_words.append(num_words)
        #finds index of highest list
        max_index = en_words.index(max(en_words))
        #uses that most accurate(most english words) to decrypt the message
        #assigns it to guess
        guess = self.decrypt_message(pads[max_index])
        #tuple with the best pad and the decryption from said pad
        best_guess = (pads[max_index], guess)
        return best_guess


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    Bob_story = get_story_string()
    secret_story = EncryptedMessage(Bob_story)
    Bob_pad = get_story_pads()
    story = secret_story.decrypt_message_try_pads(Bob_pad)
    return story[1]


if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    