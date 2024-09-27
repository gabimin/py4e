name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lista = []
d= {}

for linea in handle:
    if linea == '\n':
        continue
    else:
        words = linea.split()
        if words[0] == 'From':
           num = words[5].split(':')
           lista.append(num[0])


for hour in lista:
    if hour in d:
        d[hour] +=1
    else:
        d[hour] = 1

for k,v in sorted(d.items()):
    print(k,v) 