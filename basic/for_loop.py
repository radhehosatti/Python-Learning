# Example 1: Print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("--------------------")

# Example 2: Print even numbers from 1 to 20
print("Even numbers from 1 to 20:")
print("even numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("odd numbers:") 
for i in range(1,21):
  if i%2!=0:
     print(i)
print("--------------------") 

# Example 3: Loop through a string
name = "Radhe"
print("Characters in the name:")
for ch in name:
    print(ch)
