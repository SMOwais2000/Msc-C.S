import random
l=int(input("Enter the length of motif:"))
file=open("influenza.txt","r")
r=file.read()
print("Sequence:",r)
size=len(r)
print("Size of the sequence:",size)
pos=random.randint(0,len(r)-5)
#pos=1
print("Position:",pos)
motif=r[pos:pos+l]
print("Motif:",motif)
i=pos+1
while(i<=size-1):
    if(motif==r[i:i+1]):
        str1=r[i:i+1]
        print("Match motif",str1)
        file1=open("influenza.txt","a")
        file1.write(str1+" ")
    i+=1
