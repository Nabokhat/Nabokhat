path=r'C:\Users\user\OneDrive\Рабочий стол\python\lesson9\python.txt'

f=open(path)
text=f.read().lower()
print(text)

import string
punctuations_list=[',','.','-','*','!']
print(punctuations_list)
for i in punctuations_list:
    text=text.replace(i,'')
    text=text.replace('\n',' ')
print(text)


d={}
for i in text.split(' '):
    if len(i)>0:
        if i not in d.keys() :
            d[i]=1
        else:
            d[i]+=1

print(d)


