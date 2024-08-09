even_number = []
odd_number = []

def separator(x):
    for i in x :
        if i % 2 == 0 :
            even_number.append(i)
        elif i % 2 != 0 :
            odd_number.append(i)
            

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

separator(a)

print(even_number)
print(odd_number)
