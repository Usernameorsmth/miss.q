class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        # We will return a string
        return self.word + ' (' + self.meaning + ')'

flash = []
print("welcome to flashcard application")

# The following loop will be repeated until
# user stops to add the flashcards
while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = input("enter 0 , if you want to add another flashcard otherwise enter 1 : ")

    if(option == '1'):  # Changed to compare with string '1' as input returns a string
        break

# printing all the flashcards
print("\nYour flashcards")
for i in flash:
    print(">", i)