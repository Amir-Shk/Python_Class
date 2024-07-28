#get_number

print("enter 5 number :")

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())



#show_the_numbers

a = [n1 , n2 , n3 , n4 , n5]

#ascending
a.sort()
print(a)

#descending
a.sort(reverse = True)
print(a)
