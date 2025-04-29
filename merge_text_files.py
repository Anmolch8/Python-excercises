
for i in range (1,4):
    with open(f'file{i}.txt','r') as source_files:
        with open('text_merge.txt','a') as target_files:
            target_files.write(source_files.read())
            target_files.write('\n')
source_files.close()
target_files.close()

