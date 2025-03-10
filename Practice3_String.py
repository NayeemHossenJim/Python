# 1. User input name 
a = input()
print(f"Good Morning ,{a}")

# 2. Letter template 
letter = '''Dear Name
You r selected 
Date'''
x = letter.replace("Name",a).replace("Date","24 September")
print(x)

# 3. Find Method 
j = x.find("Jim")
print(j)

# 4. Backslash character 
h = '''Hello \nThere are \tthree cow'''
print(h)