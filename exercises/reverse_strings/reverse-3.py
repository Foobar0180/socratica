# Using recursion to reverse a string by creating a custom recursive method
def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]

print(reverse_string("Hello world"))
