vowels=['a','e','i','o','u']
st='hello everyone'
count_vowels=0

for ch in st:
    if ch in vowels:
        count_vowels+=1

print(f"Total Vowels in the string:{count_vowels}")
