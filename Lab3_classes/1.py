class String:
    def __init__(self):
        self.my_string = ""
    
    
    def getString(self):
        self.my_string = input("Write string: ")
        
        
    def printString(self):
     print(self.my_string.upper())
     
String = String()
String.getString()
String.printString()