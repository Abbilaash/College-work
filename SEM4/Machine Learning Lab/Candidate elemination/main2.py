import os,sys
import pandas as pd
import numpy as np
df=pd.read_csv("dataset3.csv")
x=np.array(df.iloc[:,0:-1])
y=np.array(df.iloc[:,-1])

def check(gen,spec):
    for i in range(len(gen)):
        if gen[i]=='?' or gen[i]==spec[i]:continue
        return 0
    return 1


def candidate(x,y):
    flag=1
    spec=['0']*len(x[0])
    gen=[['?']*len(x[0])]
    for i in range(len(x)):
        if y[i]=='yes':
            new=[]
            for j in range(len(spec)):
                if spec[j]=='0':
                    spec[j]=x[i][j]
                elif spec[j]!=x[i][j]:
                    spec[j]='?'
            for i in gen:
                if check(i,spec):new.append(i)
            gen=new[:]
            flag=0
        else:
            l=len(gen)
            for _ in range(l):
                now=gen.pop(0)
                f=0
                for j in range(len(spec)):
                    if now[j]!='?' and now[j]!=x[i][j]:
                        gen.append(now)
                        f=1
                        break
                if f:continue
                for j in range(len(spec)):
                    if now[j]!='?':continue
                    pre=now[j]
                    for k in pos[j]:
                        if k==x[i][j]:continue
                        now[j]=k
                        gen.append(now[:])
                    now[j]=pre
    return gen,spec
def all_values(x):
    pos=[set() for _ in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(x[i])):
            pos[j].add(x[i][j])
    return pos
pos=all_values(x)
gen,spec=candidate(x,y)
print("Final Specific Hypothesis: ",spec)
print("Final General Hypothesis: ")
for i in gen:
    print(i)
