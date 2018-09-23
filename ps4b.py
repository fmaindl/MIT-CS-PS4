# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
file_name = "words.txt"


def load_words(file_name):

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", (len(wordlist)), "words loaded.")
    return wordlist

#word_list=load_words(file_name)
#text=PlaintextMessage("Hello", 1)
#print(text.get_message_text())
#print(text.get_shift())    
#print(text.get_encryption_dict())        
#print(text.get_message_text_encrypted())  

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'




class Message(object):
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


    def build_shift_dict(self, shift):


        
        assert shift >= 0 and shift < 26, "shift value outside of [0,26[ bound"
        
        UC_dict={}
        LC_dict={}

        for position, value in enumerate(string.ascii_uppercase):
            UC_dict[value]= position+1
        for position, value in enumerate(string.ascii_lowercase):
            LC_dict[value]= position+1


        shift_dict={}
        
        for key, value in UC_dict.items():
            if UC_dict[key] + shift < 27:
                shift_dict[key]=list(UC_dict.keys())[list(UC_dict.values
                          ()).index(value+shift)]
            else:
                shift_dict[key]=list(UC_dict.keys())[list(UC_dict.values
                          ()).index(value+shift-26)]

        for key, value in LC_dict.items():
            if LC_dict[key] + shift < 27:
                shift_dict[key]=list(LC_dict.keys())[list(LC_dict.values
                          ()).index(value+shift)]
            else:
                shift_dict[key]=list(LC_dict.keys())[list(LC_dict.values
                          ()).index(value+shift-26)]
        return shift_dict
    
    
    
    def apply_shift(self, shift):

        assert shift >= 0 and shift < 26, "shift value outside of 0,26 bound"
        
        List=list(self)
        
        
        List_clone=List[:]
        
        for position, value in enumerate(List):
            if value in build_shift_dict(self, shift).keys():
                List_clone[position]=build_shift_dict(self, shift)[value]

        return ''.join(List_clone)
        
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):

        self.text = text 
        self.shift = shift

    def get_shift(self):

        return self.shift

    def get_encryption_dict(self):
        

        encryption_dict=build_shift_dict(self.text, self.shift)
        encryption_dict_copy=encryption_dict.copy()
        return encryption_dict_copy
    
    

    def get_message_text_encrypted(self):
  

        text_encrypted=apply_shift(self.text, self.shift)
        return text_encrypted
        



#
    def change_shift(self, shift):

        assert shift >= 0 and shift < 26, "shift out of bounds"
        
        self.shift = shift

class CiphertextMessage(Message):
    def __init__(self, text):

        self.text = text

    def decrypt_message(self):


        List=list(self.text)
        
        result_dictionary={}
        
        
        for s in range(1, 25):
            Decrypted_message=apply_shift(List, 26-s)  
            test=get_valid_words(Decrypted_message)
            counter=len(test)    
            result_dictionary[(26-s, Decrypted_message)]=counter
            
        best_counter=max(result_dictionary, key=result_dictionary.get)
        
        if max(result_dictionary.values()) == 0:
            return "Oops, can't figure this one out"
        else:
            print(best_counter)
            return best_counter    
        


text=CiphertextMessage(get_story_string()) 
print(text.decrypt_message())   



#if __name__ == '__main__':