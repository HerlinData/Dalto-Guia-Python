lista = [(3,"a"), (1,"b"),(5,"c"), (2,"d"), (1,"e"), (7,"f"), (4,"g")]
reverso = list(reversed(lista))
print(reverso)

for i in reverso:
    if i[0] == 1:
        print(i) 
             
for i in reverso:
    if i[0] == 2:
        print(i)