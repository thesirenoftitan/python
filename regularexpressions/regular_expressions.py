with open("The_Raven.txt", "r") as file:
    contents = file.read()
"""
# Identify all the words that start with a ‘t” but do not end with an ‘e’, case should be ignored here.

matches = re.findall("'/t", contents)
count = len(matches)

print(f"The substring "'t" appears {count} times.")
"""

"""
# Change all the exclamations marks (!) to hash symbols (#)

new_contents = contents.replace("!", "#")

with open("The_Raven_New.txt", "w") as file:
    file.write(new_contents)
"""

""" 
# Find the word ‘shrieked’

result = re.search("shrieked", contents)

if result:
    print("yes")
else:
    print("no")
"""
""" 
# Find the word ‘bleak’

result = re.search("bleak", contents)

if result:
    print("yes")
else:
    print("no")
"""
"""
# Count the number of words that contain ‘pp’

matches = re.findall('pp', contents)
count = len(matches)

print(f"The substring 'pp' appears {count} times.")
"""

