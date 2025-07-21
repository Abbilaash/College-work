coord = [(1,1),(2,1),(4,3),(5,4),(3,2)]
classes = ['Red','Red','Blue','Blue','Red']
point = ['A','B','C','D','E']
z = []
left_out = [i for i in range(len(coord))]
count = [0]*len(coord)

def distance(a,b):
    return ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
    
while left_out:
    i = left_out.pop(0)
    if count[i]>2:
        continue
    count[i] += 1
    if len(z)==0:
        z.append(i)
    else:
        min_len = 10**8
        min_ind = -1
        for j in range(len(z)):
            if distance(coord[i],coord[j])<min_len:
                min_len = distance(coord[i],coord[j])
                min_ind = j
        if classes[min_ind]!=classes[i]:
            z.append(i)
        else:
            left_out.append(i)

print("Z = {",end="")
for i in z:
    print(point[i],end=" ")
print("}")

# OUTPUT:
# Z = {A C D }
