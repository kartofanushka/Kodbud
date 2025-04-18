def palindrome(string): 
    if (string == string[::-1]) :
        return True
    else: 
        return False 
 
#Enter input string 
string = input ("Enter....: ") 
 
print(palindrome(string)) 