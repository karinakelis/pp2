def Polindrome(string):
     return string == string[::-1]
string = "anna"
ans = Polindrome(string)
if ans:
    print("Yes")
else:
    print("No")
    