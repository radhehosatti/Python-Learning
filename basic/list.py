numbers = list(range(1, 21))

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even numbers:", even)
print("Odd numbers:", odd)
