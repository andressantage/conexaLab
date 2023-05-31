from re import I
n=[0.06849890236663069,
 0.8206475733869476,
 0.13871465842485664,
 0.32380767744145744,
 0.014846454193457195,
 0.5967957430071836,
 0.7176842391562697,
 0.02483996934407761,
 0.17900814126833098,
 0.3650412345195949,
 0.3517822129987791,
 0.24944816935860137,
 0.10169749888997713,
 0.557670637524901,
 0.8686465335094339,
 0.41454013905692766,
 0.7811167324297337,
 0.1579188469810079,
 0.06826989271497096,
 0.39429924247482184,
 0.7907181682586601,
 0.8840039202284332,
 0.9786879116228561,
 0.31214143888577095,
 0.06079983871516747]

suma=0
suma1=0
NFT_suma=[]
posicion=[]
p=-1
for j in range(20):
  l=j

for i in range(len(n)):
  if(n[i]>1):
    print("soy mayor de 1")
    break
  suma=suma1
  if(suma<1):
    suma1=suma+n[i]
    k=i
    if(suma1>1):
      NFT_suma.append(suma)
      p=p+1
      posicion.append(k)
      break

d=1-NFT_suma[p]
o=n[posicion[p]+1]-d

suma=o
suma1=o
for i in range(posicion[p]+1, 10):
  print(i)

'''   if(n[i]>1):
    print("soy mayor de 1")
    break
  suma=suma1
  if(suma<1):
    suma1=suma+n[i]
    k=i
    if(suma1>1):
      NFT_suma.append(suma)
      p=p+1
      posicion.append(k)
      break '''




  
  


print(l)
print(NFT_suma)
print(posicion)
print(p)
print(d)
print(o)
