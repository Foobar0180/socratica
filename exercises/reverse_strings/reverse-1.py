# Using loops and joins to concatenate to a temp array
def reverse_string(str):
    
    temp = []
    length = len(str)

    while length > 0:
        # In each iteration, concatenate the value of str[index-1] with temp
        temp += str[length - 1]

        # Decrement the length
        length = length - 1

    res = ''.join(temp)
    return res

print(reverse_string("Hello world"))
