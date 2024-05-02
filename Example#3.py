# Example 3 - Calculating Average

num_of_students = int(input("Enter the number of students: "))

sum = 0

while num_of_students > 0:
    mark = float(input(f"Enter mark ({num_of_students - 1} remaining):"))
    sum += mark
    num_of_students -= 1
    
average = sum/num_of_students

print(f"Your class average is {average}")