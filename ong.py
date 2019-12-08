# File:        ong.py
# Author:      De'Shaunna Scott
# Date:        11/19/15
# Section:     29
# Email:       dscott6@umbc.edu
# Description: This program will contain a class "ong" that will translate words
#              given by the user to ong language

class Ong:
    word = ""

    # Class constructor
    def __init__(self,word):
        self.word = word
    
    # this method determines if a letter in the given word is a vowel or not
    def isVowel(self,letter):
        self.letter = letter
        if(( self.letter == "a") or (self.letter == "e") or (self.letter == "i") or (self.letter == "o") or (self.letter == "u")):
            return True
        else: 
            return False

    # this method translates given word to ong language
    def translateOng(self):
        translated = ""
        word = self.word
        # iterates over the string to determine which letter to add "ong" to
        for letter in word:
            vowel = self.isVowel(letter)
            if vowel  == False:
                translated += (letter + "ong")
            else:
                translated += letter 
        print(translated)

def main():
    word = input("Enter a string to translate: ")
    ong = Ong(word)
    ong.translateOng()
main()
