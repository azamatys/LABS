class Person():
    def __init__(self):
        self.word = ""
    
    def getString(self):
        self.word = input()

    def printString(self):
        print(self.word.upper())

word = Person()
word.getString()
word.printString()