#Vjezbe3.
#Zadatak 1.
#a)
a=5.0-4.935 #ocekivani rezlutat 0.065
print(a)#rezlutat je 0,06500000000000039
#Razlog zasto rezlutat nije 0.065 vec 0,06500000000000039 je 
# pogreska u zaokruzivanju. Broj kao sto je 4.935 se u 
# pythonu ne gleda kao decimalni vec kao binarni broj
#. Samo s brojevima oblika 1/2^{n} moze idealno racunati sve ostalo je aproksimacija, aproksimacija kojom se priblizava toj vrijednosti sto je vise moguce.

#b)
b=0.1+0.2+0.3
print(b)
print('ovdje staje 1.zdk')
#rezultat je 0.6000000000000001
#Razlog rezultata jest taj sto, bas kao i u prvom slucaju, Python ne vidi nase desimalne brojeve kao takve vec kao njihovu binarnu
#reprezentaciju koja nije tocno jednaka doticnimk brojevima pa samim tim ni njihov zbroj nece biti.


#Zadatak 2.
br=0
N1=200
N2=2000
N3=20000

while br==0:
    for ele in range(N1):
        ele=1/3
        br=br+ele
    print('Rezlutat zbrajanja 200 iteracija je {}.'.format(br))

    br=0

    for le in range(N2):
        le=1/3
        br=br+le
    print('Rezlutat zbrajanja 2000 iteracija je {}.'.format(br))

    br=0

    for l in range(N3):
        l=1/3
        br=br+le
    print('Rezlutat zbrajanja 20000 iteracija je {}.'.format(br))

    br=5

    for i in range(N1):
        i=1/3
        br=br-i
    print('Rezultat od 200 oduzetih iteracija broju 5 je {}.'.format(br))
   
    br=5

    for j in range(N2):
        j=1/3
        br=br-j

    print('Rezultat od 2000 oduzetih iteracija broju 5 je {}.'.format(br))
    

    br=5

    for k in range(N3):
        k=1/3
        br=br-k
    print('Rezultat od 20000 oduzetih iteracija broju 5 je {}.'.format(br))


#U ovom primjeru je vidljivo kako tocnost rezultata opada brojem iteracija gdje za 200 ponmavljanja rezultat ce biti tocan do 12-este decimale dokle onaj za 20000 ce biti tocan do 8.
# Razlog pogreske je taj sto nas rezultat nije nasatao sumiranjem brojeva koji dolaze u obliku 1/2^{n} vec u obliku broja 1/3 sto iziskuje izracun doticnih uzastopnih radnji kroz aproksimaciju.