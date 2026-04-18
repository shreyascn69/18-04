#  1. Reverse a String (Logic)

# Write a program to reverse a string without using slicing ([::-1]).

# st = [1,2,3,4,5,6]

# rev = []
# for i in range(len(st)-1, -1, -1):
#     rev.append(st[i])

# print(rev)



# ss = int(input())

# for i in range(2, ss):
#     if ss%i ==0:
#         print(ss, "prime number")
#         break
# else:
#     print(ss, "not a prime number")


#  3. Output Prediction
# def func(a, b=[]):
#     b.append(a)
#     return b

# print(func(1))
# print(func(2))
#  Output:
# [1]
# [1, 2]



#  4. Second Largest Number (Without sort)
# st = [10, 20, 4, 45, 99]

# first = second = -float('inf')

# for i in st:
#     if i > first:
#         second = first
#         first = i
#     elif i > second and i != first:
#         second = i

# print("Second largest:", second)

# 5. Character Frequency
# st = "aabbc"

# freq = {}

# for ch in st:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)
#  Output:
# {'a': 2, 'b': 2, 'c': 1}