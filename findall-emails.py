st="Contact us at info@example.com or support@another.net.  Also, see john.doe@domain.org."

split_str=st.split()

emails=[]

for word in split_str:
    if '@' in word:
       emails.append(word)

emails=list(map(lambda a:a[:-1] if a.endswith('.') else a,emails))
print(emails)