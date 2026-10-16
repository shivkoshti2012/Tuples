#tuple and its method
tup = (87,64,33,95,76)
print(tup[0])
print(tup[1:3])
print(len(tup))
tup1 = ()#It is called empty tuple
tup2 = (1,)
tup3 = (1,2,3)
print(type(tup2))
print(type((1)))
#tuples method
print(tup3.index(1))
print(tup1.count(1))
# Ask the user to enter the names of their 3 favorite movies and store them in a list.
movies = []
movies.append(input("Enter 1st Movie: "))
movies.append(input("Enter 2nd movie:"))
movies.append(input("Enter 3rd movie:"))
print(movies)
#Check if a list is a palindrome (reads the same forwards and backwards).
nums = [1,2,3,2,1]
copy_nums = nums.copy()
copy_nums.reverse()
if nums == copy_nums:
    print("Palindrome")
else:
    print("Not a Palindrome")
#Count the number of students with the "A" grade in the following tuple.
grades = ("C","D","A","A","B","B","A")
print("Students with A grade:", grades.count("A"))
#Store the above values in a list and sort them from "A" to "D".
grades = ["C","D","A","A","B","B","A"]
grades.sort()
print(grades)