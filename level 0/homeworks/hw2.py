A=15
B=5
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A**B)
print(A//B)

birth_year=2011
current_year=2026
age=birth_year-current_year
print(age)


number1 = 10
number2 = 20
number3 = 30
number4 = 40
number5 = 50

numbers = number1 + number2 + number3 + number4 + number5
average = numbers / 5
print(average)


# დეკლარაცია ნიშნავს ცვლადის შექმნას (გამოცხადებას)
# Python-ში ცვლადის დეკლარაცია და ინიციალიზება ერთდროულად ხდება

x = 10
# ↑ აქ:
# x — ცვლადის სახელია
# = — მინიჭების ოპერატორია
# 10 — მნიშვნელობა
# ეს არის ინიციალიზება (ცვლადს პირველად მივანიჭეთ მნიშვნელობა)


# ინიციალიზება ნიშნავს, რომ ცვლადს ვაძლევთ საწყის მნიშვნელობას
age = 14
# age ცვლადი ინიციალიზებულია მნიშვნელობით 25


# რეინიციალიზება ნიშნავს უკვე არსებულ ცვლადში ახალი მნიშვნელობის მინიჭებას
age = 20
# ↑ აქ age უკვე არსებობდა, მაგრამ მნიშვნელობა შეიცვალა
# ეს არის რეინიციალიზება


# კიდევ ერთი მაგალითი
number = 5      # ინიციალიზება
number = 15     # რეინიციალიზება

print(number)   # ტერმინალში გამოვა 15


#კონკატენაცია ნიშნავს ორი ან მეტი ტექსტის (string)ის შეერთებას
name="nika"
surname="jalabadze"
full_name=name +" "+ surname
print(full_name)


#debugging ნიშნავს რაიმე შეცდომის შესწორებას