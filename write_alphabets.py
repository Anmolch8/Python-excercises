name=input("Give Name:")
name=name.lower()
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_dict=dict()

for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]]=i+1

for ch in name:
       print(f'{ch} - {alphabet_dict[ch]}\n')

