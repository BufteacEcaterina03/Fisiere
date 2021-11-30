with open ('c:/Users/User/Desktop/fisier.txt', 'r') as f:
    j=f.read()
with open ('fisier2.txt', 'w') as f:   
    for i in range (0,len(j)):
        if str(j[i])=='u' or str(j[i])=='e' or str(j[i])=='a' or str([i])=='i' or str(j[i])=='o' or str(j[i])=='O' or str(j[i])=='E' or str(j[i])=='I' or j[i]=='U' or j[i]=='A':
             f.write((j[i]))
        

