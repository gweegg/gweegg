

#pass value to a function

my_text = input("Type anything you want: ")

def print_test(text):
    print("The output is: " , text)

print_test(my_text)

#ass value to a function 2
def InputAge(age):
    new_age = age + 10
    return new_age

How_old = InputAge(3)
print(How_old) 