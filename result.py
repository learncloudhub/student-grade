name = input("Type Student Name: ")
sub1 = int(input("Myanmar exam mark: "))
sub2 = int(input("English exam mark: "))  
average = (sub1 + sub2) // 2
print(f"Name: {name}")

if sub1 > 40 and sub2 > 40:
    result = "Passed"
else:
    result = "Failed"

print(f"Myanmar, {sub1}, {result}")
print(f"English, {sub2}, {result}")

print(f"Average mark on 2 subjects: {average}")

total = sub1 + sub2
print(f"Total Mark: {total}")

print("Test conflict local")
