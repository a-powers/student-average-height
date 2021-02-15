student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total_heights = 0
for height in student_heights:
    total_heights += height
sum_of_heights = total_heights

total_students = 0
for student in student_heights:
    total_students += 1
count_of_students = total_students

average_height = sum_of_heights//count_of_students

print(f"The average student height is {average_height}.")