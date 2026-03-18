#1
for i in range(1, 51):
    print(i)

#2
for i in range(2, 101, 2):
    print(i)

#3
for i in range(1, 101, 2):
    print(i)

#4
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

#5
total = 0

for i in range(1, 101):
    total += i

print(total)

#6
for i in range(50, 0, -1):
    print(i)

#7
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
    print(count)

#8
for i in range(1, 11):
    print(i ** 2)

#9
for i in range(1, 11):
    print(i ** 3)

#10
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

#11
i =1
while i <= 20:
    print(i)
    i = i + 1

#12
n = int(input("Enter a number: "))
 
fact = 1
i = 1
 
while i <= n:
    fact = fact * i
    i = i + 1
 
print("Factorial =", fact)
 
#13
num = int(input("Enter a number: "))
 
rev = 0
 
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
 
print("Reversed number =", rev)

#14
num = int(input("Enter a number: "))
 
count = 0
 
while num > 0:
    num = num // 10
    count = count + 1
 
print("Number of digits =", count)

#15
text = ""
 
while text != "stop":
    text = input("Enter something: ")

#16
i = 1

while i <= 4:
    print("*" * i)
    i += 1

#17
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#18
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

#19
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

#20
num = 1
 
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num = num + 1
    print()

#21
text = input("Enter a string: ")
 
count = 0
 
for ch in text:
    count = count + 1
 
print("Total characters =", count)

#22
text = input("Enter a string: ")
 
count = 0
 
for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1
 
print("Vowels =", count)

#23
text = input("Enter a string: ")
 
count = 0
 
for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count = count + 1
 
print("Consonants =", count)

#24
text = input("Enter a string: ")
 
rev = ""
 
for ch in text:
    rev = ch + rev
 
print("Reversed =", rev)

#25
text = input("Enter a string: ")
 
rev = ""
 
for ch in text:
    rev = ch + rev
 
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
 
#26
text = input("Enter a string: ")
 
print(text[0:5])

#27
text = input("Enter a string: ")
 
print(text[-3:])
 
#28
text = input("Enter a string: ")
 
print(text[::-1])

#29
text = input("Enter a string: ")
 
print(text[::2])

#30
text = input("Enter a string: ")
 
print(text[1:-1])

#31
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

#32
numbers = [10, 20, 30, 40, 50]
max_value = max(numbers)
print(max_value)

#33
numbers = [10, 20, 30, 40, 50]
min_value = min(numbers)
print(min_value)
 
#34
numbers = [10, 20, 30, 40, 50]
total_elements = len(numbers)
print("Total elements:", total_elements)

#35
numbers = [10, 23, 45, 67, 89]
search_value = 23
print(f"{search_value} exists in list: {search_value in numbers}")
search_value = 100
print(f"{search_value} exists in list: {search_value in numbers}")

#36
numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)
numbers.append(60)
print(numbers)
 
#37
numbers = [20, 40, 60, 90]
 
numbers.insert(2, 25)
 
print(numbers)

#38
numbers = [1, 2, 3, 4, 5]
 
numbers.remove(3)
 
print(numbers)

#39
numbers = [1, 2, 3, 4]
 
reversed_list = []
 
for num in numbers:
    reversed_list = [num] + reversed_list
 
print(reversed_list)
 
#40
numbers = [4, 1, 3, 2]
 
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
 
print(numbers)
 