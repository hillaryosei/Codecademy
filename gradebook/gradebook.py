last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#create subjects list
subjects = ["physics", "calculus", "poetry", "history"]

#create grades list
grades = [98, 94, 85, 88]

#create gradebook list by adding subjects and grades list together
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
#print(gradebook)

#add computer science subject and grade to gradebook
gradebook.append(["computer science", 100])
#print(gradebook)

#add visual arts subject and grade to gradebook
gradebook.append(["visual arts", 93])
#print(gradebook)

#change gradebook to include extra 5 points to visual arts grade
gradebook[5][1] = 98
#print(gradebook)

#change poetry class grade
gradebook[2].remove(85)
#print(gradebook)

#change poetry class grade to pass
gradebook[2].append("Pass")
#print(gradebook)

#merge last_semster_gradebook and gradebook lists together
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
