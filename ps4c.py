
import random
  
import string
from ps4a import get_permutations

file_name = 'words.txt'
### HELPER CODE ###
def load_words(file_name):

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###



word_list=load_words(file_name)


VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'





class SubMessage(object):
    def __init__(self, text):

        self.text = text 
    
    def get_message_text(self):

        return self.text

    def get_valid_words(self):

        valid_words=[]
        
        for i in self.split():            
            if is_word(word_list, i) == True:
                valid_words.append(i)
        return valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):

        
        UC_dict={}
        LC_dict={}

        for position, value in enumerate(string.ascii_uppercase):
            UC_dict[value]= position+1
        for position, value in enumerate(string.ascii_lowercase):
            LC_dict[value]= position+1

        vowels_permutation_upper=vowels_permutation
        vowels_permutation_lower=vowels_permutation_upper.lower()

        
        shift_dict={}
        
        for key, value in UC_dict.items():            
            if key in VOWELS_UPPER:
                for i, j in enumerate(VOWELS_UPPER):
                    if j == key:
                        shift_dict[key]=vowels_permutation_upper[i]
            else:
                shift_dict[key]=key

        for key, value in LC_dict.items():            
            if key in VOWELS_LOWER:
                for i, j in enumerate(VOWELS_LOWER):
                    if j == key:
                        shift_dict[key]=vowels_permutation_lower[i]
            else:
                shift_dict[key]=key
        return shift_dict


    
    def apply_transpose(self, transpose_dict):

        
        List=list(self)
        
        
        List_clone=List[:]
        
        for position, value in enumerate(List):
            if value in transpose_dict.keys():
                List_clone[position]=transpose_dict[value]

        return ''.join(List_clone)
    
    
    

        




class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text = text


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        List=list(self.text)
        
        result_dictionary={}
    
        for i in get_permutations(VOWELS_UPPER):
            x=build_transpose_dict(List, i)
            y=apply_transpose(List, x)
            test=get_valid_words(y)
            counter=len(test)
            result_dictionary[y]=counter
        
        best_decrypt=max(result_dictionary, key=result_dictionary.get)
        
        if max(result_dictionary.values()) == 0:
            return "Can't find good decryption"
        else:
            return 'The best decoded message is '+ best_decrypt
            
            
a=EncryptedSubMessage("Heppy")
print(a.decrypt_message())

#
##            
#            
#
#if __name__ == '__main__':
#
#    # Example test case
#    message = SubMessage("Hello World!")
#    permutation = "eaiuo"
#    enc_dict = message.build_transpose_dict(permutation)
#    print("Original message:", message.get_message_text(), "Permutation:", permutation)
#    print("Expected encryption:", "Hallu Wurld!")
#    print("Actual encryption:", message.apply_transpose(enc_dict))
#    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
#    print("Decrypted message:", enc_message.decrypt_message())
##
