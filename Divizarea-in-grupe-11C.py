f=open('c:/Users/User/Downloads/Lista Clasei 11C.txt','r')
Y=list(f)
f.close()
f=open('c:/Users/User/Desktop/Lista_Clasei_11C.txt','w')
f.write(f'Nume\tPrenume\t\tNota\tLimba\n')
k=open('c:/Users/User/Desktop/Grupa nr.1.txt','w')
z=open('c:/Users/User/Desktop/Grupa nr.2.txt','w')
note=[]
for j in range(len(Y)):
    elv= Y[j].split()
    n=int(input(f"Nota elevului {elv[0]}  {elv[1]}:"))
    note.append(n)
    l=str(input(f'Limba straina:'))
    f.write(f'{elv[0]}  {elv[1]}, {str(n)} {l}   \n')
    if str(l).lower()=='limba engleza':
        k.write(f'{elv[0]}\t{elv[1]}\t{str(n)}\n')
    elif str(l).lower()=='limba franceza':
        z.write(f'{elv[0]}\t{elv[1]}\t{str(n)}\n')
k.close()
z.close()
f.write(f'Media celor {len(Y)} studenti este {sum(note)/float(len(Y))}')
f.close()