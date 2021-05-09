
read1 = "book1.txt"
read2 = "book2.txt"

book1 = open(read1, 'r', encoding='utf-8')
book2 = open(read2, 'r', encoding='utf-8')

bk1=set()
bk2=set()

p = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

for word in book1.read().split():
    for x in word :
        if x in p :
            word=word.replace(x,"")
    if word !=' ':
        bk1.add(word.lower())
        
for word in book2.read().split():
    for x in word :
        if x in p :
            word=word.replace(x,"")
    if word !=' ':
        bk2.add(word.lower())       
        
        
commonwords=bk1.intersection(bk2)
print (commonwords)