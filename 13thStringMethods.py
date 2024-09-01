# String are immutable
a="Durjoy! !!!! !Durjoy"
print(len(a))
print(a)

print(a.upper()) #upper() methods converts all the character in the string into upperCase

print(a.lower()) #lower() methods converts all the character in the string into lowerCase

print(a.rstrip("!")) #rstrip("!") methods removes all character which is common in the string and the inside this method

print(a.replace("Durjoy","Abir")) #replace("Durjoy","Abir") is replace Durjoy to Abir.

print(a.split(" ")) # split() method make a list deviding where it get the character which given inside the method

blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) #capitalize() convert the first character into upper case.Other than all of us is in lower case

str1="Welcome to the Console"
print(len(str1)) #25
print(len(str1.center(50))) #center(50) print the string in the center among 50 character.

print(a.count("Durjoy")) #count("Durjoy") it counts how many times Durjoy isin the string

str1="Welcome to the Console !!!"
print(str1.endswith("!!!")) #endswith("!!!") is contains boolean type value.If string endswith !!! it prints true else false 

str1="Welcome to the Console !!!"
print(str1.endswith("to",4,10)) #endswith("to",4,10) is contains boolean type value.If inside the string index 4 to 10 string endswith "to" it prints true else false 


str1="He's name is Dan. He is an honest man."
print(str1.find("is")) #find("is") from 0 index when it gets is it print the index no.
print(str1.find("ishh"))#find("ishh") if ishh can't find in the string it prints -1

str1="WelcomeToTheConsole"
print(str1.isalnum()) #if str1 is alphanumaric, it prints true else false
str1="Welcome00"
print(str1.isalnum()) #if str1 is alphanumaric, it prints true else false

str1="hello world"
print(str1.islower()) #if all charecter of str1 is lowercase, it prints true else false

str1="HELLO"
print(str1.isupper()) #if all charecter of str1 is uppercase, it prints true else false

str1="hello world"
print(str1.isprintable()) #if all charecter of str1 is printable, it prints true else false

str1="          "
print(str1.isspace()) #if there is a space in the string ,it prints true else false


str1="Hello World"
print(str1.istitlele()) #if first letter of all words in the string is in uppercase, it prints true else false


str1="Python is interpreted language"
print(str1.title()) #it uppercase first letter of all words in the string

str1="Python is interpreted language"
print(str1.swapcase()) #it uppercase the letter which is in lowercase and lowercase the letter which is in uppercase .

str1="Python is interpreted language"
print(str1.startswith("Python")) #if string startwith "Python",it prints True else false.