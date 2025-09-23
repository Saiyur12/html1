class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):


        #We will return a string
        return self.word+' ( '+self.meaning+')'
    
flash = []
print("Welcome to flashcard application")

#The following loop will be rpeated until
#User stops to add the flashcards
while(True):

