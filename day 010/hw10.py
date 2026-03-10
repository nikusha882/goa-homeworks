temperature = float(input("შეიყვანე ტემპერატურა: "))

if temperature > 30:
    print("ძალიან ცხელა")
elif temperature > 20:
    print("სასიამოვნო ამინდია")
elif temperature > 10:
    print("ცოტა ცივა")
elif temperature > 0:
    print("ცივა თბილად ჩაიცვი")
else:
    print("გაიყინები")



score = float(input("შეიყვანე შენი ქულა: "))
attendance = float(input("შეიყვანე დასწრება (%): "))

if score > 80 and attendance > 90:
    print("შენ ჩააბარე გამოცდა")
elif score > 50 and attendance > 70:
    print("შენ ჩააბარე გამოცდა")
elif score > 30 or attendance > 50:
    print("შენ ჩააბარე გამოცდა")
else:
    print("ჩაიჭერი!")




# მომხმარებლის შეყვანილი მონაცემები
temp = float(input("შეიყვანე ტემპერატურა: "))
rain = input("წვიმა არის? (yes/no): ") 

# პირობის შემოწმება
if temp > 25 and rain == "no":
    print("შესანიშნავი ამინდია სასეირნოდ!")
elif temp > 25 and rain == "yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!")
elif temp < 10 or rain == "yes":
    print("სჯობს სახლში დარჩე")
else:
    print("სასიამოვნო ამინდია")




age =int(input("შეიყვანე შენი ასაკი "))
is_student =input("ხარ სტუდენტი? (yes/no): ")