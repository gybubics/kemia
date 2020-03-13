#Év;Elem;Vegyjel;Rendszám;Felfedező
#0   1     2        3         4
#Ókor;Arany;Au;79;Ismeretlen

with open("felfedezesek.csv", 'r', encoding='latin2') as f:
    fejlec = f.readline()
    matrix = list()
    for i in f:
        matrix.append( i.strip().split(';') )
        
print (f' 3. feladat: Elemek száma: {len(matrix)} ')

szamlalo = 0
for sor in matrix:
    if sor[0] == 'Ókor':
        szamlalo += 1
print (f' 4. feladat: Felfedezések száma az ókorban: {szamlalo} ')
def betu( x ):
    return 'a' <= x <= 'z' or 'A' <= x <= 'Z'
while True:
    a = input('Kérek egy vegyjelet:')
    if len(a) == 1:
        if betu(a):
            break
    elif len(a) == 2:
        if betu(a[0]) and betu(a[1]):
            break
