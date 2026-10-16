#accessing tuple
developer = ('Alice', 34, 'Rust Developer')
developer[1]
developer[-1]
developer[4]#will create error
#using the tuple constructor
dev = 'Jessica'
tuple(dev)
#checking values from a tuple
programming_language = ('Python','Java', 'C++')
print('Python' in programming_language)
#unpacking values from a tuples
name,age,job = developer
print(name)
print(age)
print(job)
name,*rest = developer
print(name)
print(rest)
dessert = ('cake','pie','cookies','ice cream')
dessert[1:3]
#Removing element from tuple
del developer[1]#this will create error because tuple is immutable but i have written this to demonstrate this only that tuple is immutable.