# Convert school to a list of 4 words, then use a for loop to print the words
# on 4 consecutive lines.

school = "Warren County Community College"
# Your code below:
school_list = school.split()
x = 0
for i in range(len(school_list)):
    print(school_list[x])
    x += 1
