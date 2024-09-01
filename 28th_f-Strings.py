letter = "Hey my name is{1} and I am from {0}"
country = "Bangladesh"
name="Durjoy"

print(letter.format(country,name),"\n") # In complex program this method can be very difficult.Thats why we use f-String to handle this problem.

print(f"Hey my name is{name} and I am from {country}","\n") #We use formatting String(f-String) to put the right data in right place.

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}","\n")

   #It prints>>>We use f-strings like this: Hey my name is {name} and I am from {country}

price = 49.0999
txt=f"For only {price:.2f} dollars!" 
print(txt) #here it prints >> For only 49.09 dollars!

print(type(f"{2*30}")) #Class>>String
