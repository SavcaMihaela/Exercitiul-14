n= int(input('Numarul de linii:'))
X=[[int(input())for a in range(n)]for b in range(n)]
print(' Matricea:')
for a in range(len(X)):
    print(X[a])
s1=0
for a in range(0, len(X)):
    s1+=X[a][a]
s2=0
for a in range(0, len(X)):
    s2+=X[len(X)-a-1][a]
print('Suma componentelor diagonalei principale{s1}, Suma diagonalei secundare{s2}')
s3=0
for a in X:
    for b in a:
        if X.index(a)<a.index(b):
            s3+=b
print('Suma componentelor aflate mai sus de diagonala principala{s3}')
s4=0
for a in X:
    for b in a:
        if X.index(a)>a.index(b):
            s4+=b
print('Suma componentelor aflate mai jos de diagonala principala{s4}')
s5=0
for a in X:
    for b in a:
        if X.index(a)+a.index(b)<n-1:
            s5+=b
print('Suma componentelor aflate mai sus de diagonala secundara{s5}')
s6=0
for a in X:
    for b in a:
        if X.index(a)+a.index(b)>n-a:
            s6+=b
print('Suma componentelor aflate mai jos de diagonala secundara{s6}')