# 1) 200-დან 500-მდე 4-ის და 7-ის საერთო ჯერადები

# for ციკლით
print("Task 1 - for:")
for i in range(200, 501):
    if i % 4 == 0 and i % 7 == 0:
        print(i)

# while ციკლით
print("Task 1 - while:")
i = 200
while i <= 500:
    if i % 4 == 0 and i % 7 == 0:
        print(i)
    i += 1


# 2) 300-დან 1000-მდე 3-ის ან 10-ის ჯერადები

# for ციკლით
print("Task 2 - for:")
for i in range(300, 1001):
    if i % 3 == 0 or i % 10 == 0:
        print(i)

# while ციკლით
print("Task 2 - while:")
i = 300
while i <= 1000:
    if i % 3 == 0 or i % 10 == 0:
        print(i)
    i += 1


# 3) 1-დან 50-მდე Even / Odd
print("Task 3:")
for i in range(1, 51):
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)


# 4) 10 რიცხვის შეყვანა
print("Task 4:")
positive = 0
negative = 0

for i in range(10):
    num = int(input("Enter number: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)


# 5) რიცხვის შემოწმება
print("Task 5:")
num = int(input("Enter number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Good")
elif num % 2 == 0:
    print("Two")
elif num % 3 == 0:
    print("Three")
else:
    print("None")


# 6) FizzBuzz (1-დან 100-მდე)
for i in range(1,101):
    print(i)


print("task: 7")
positive = 0
negative = 0

while True:
    num = int(input("Enter number: "))
    if num > 0:
        positive += 1
    else:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)

# 8) 1-დან n-მდე, მაგრამ 4-ის ჯერადების გამოტოვება
print("Task 8:")
n = int(input("Enter number: "))

for i in range(1, n + 1):
    if i % 4 == 0:
        continue
    print(i)


# 9) 5-ჯერ შეყვანა (Even/Odd)

# for ციკლით
print("Task 9 - for:")
for i in range(5):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# while ციკლით
print("Task 9 - while:")
i = 0
while i < 5:
    num = int(input("Enter number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    i += 1