import random
#part a
#task 1

print("""Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius""")

choose = input("Choose conversion (1-4): ") 

temp = float(input("Enter temperature: "))

if choose == "1" :
    fahrenheit =  temp * 9 / 5 + 32
    print("Temperature in Fahrenheit: ", fahrenheit)

elif choose == "2":
    celsius = (temp-32)*5/9
    print("Temperature in Celsius: ", celsius)
elif choose == "3":
    kelvin = temp +273.15
    print("Temperature in kelvin :", kelvin)
elif choose == "4":
    celsius = temp-273.15
    print("Temperature in Celsius: ", celsius)
else :
    print("non value we have")

#task2

numbers = input("Enter numbers separated by spaces:").split()

numbers = [int(x) for x in numbers]

print("Original list:",numbers)

numberssum =sum(numbers)
print("Sum:",numberssum)

numberslen =len(numbers)

avrgenumbers = numberssum / numberslen

print("Average:",avrgenumbers)

maxnum = max(numbers)

minnumber = min(numbers)

print("Max::",maxnum, ", Min:", minnumber)

withoutduplication = list(set(numbers))

print("Without duplicates:", withoutduplication)

sortnumber = sorted(numbers)

print ("Sorted (asc):" , sortnumber)

evennumbers =[x for x in numbers if x % 2 == 0]
oddnumbers = [x for x in numbers if x % 2 != 0]


print("Odd numbers:", evennumbers)
print("Odd numbers:", oddnumbers)

#task 3

text = input("Enter text:")

totalchar = len(text)

print("Total characters (with spaces):",totalchar)

totalcharWithoutspace = len(text.replace(" ",""))

print("Total characters (without spaces):", totalcharWithoutspace)

words = len(text.split())

print("Total words: " , words)

eachchar= {}

for x in text :
    if x != " ":
        if x in eachchar :
            eachchar [x]+=1
        else :
            eachchar [x] = 1

print("Character frequency: " , eachchar)

maxchar = max(eachchar.values())

mostcommon = [char  for char , count in eachchar.items() if count == maxchar ]

print("Most common character:",", ".join(mostcommon),f"(appears {maxchar} times)")

revchar = (text[::-1])

if revchar == text:
    print("Is palindrome: Yes")
else:
    print("Is palindrome: No")

print("Reversed: ",revchar)


