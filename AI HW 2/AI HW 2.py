
# coding: utf-8

# In[12]:


import signal
import time
import timeit
import copy

def input():
    fin = open("input0.txt", "r")
    fout = open("output.txt", "w")
    files = fin.readlines()
    x = []
    lah_applicant = []
    spla_applicant = []
    applicant = []
    for i, line in enumerate(files):
        x.append(line.rstrip())
    beds = int(x[0].strip())

    la_beds= [beds,beds,beds,beds,beds,beds,beds]

    parking = int(x[1].strip())
    spla_parking = [parking,parking,parking,parking,parking,parking,parking]

    lah_so_far = int(x[2].strip())
    a = 2+ lah_so_far+1
    for i in range (0,lah_so_far):
        lah_applicant.append(x[3+i])
    spla_so_far = int(x[a].strip())
    a += 1
    for i in range (0,spla_so_far):
        spla_applicant.append(x[a+i])

    a += spla_so_far
    no_of_applicant = int(x[a].strip()) 
    a+=1
    
    for i in range (0,no_of_applicant):
        applicant.append(x[a+i])
    k = 0
    appli =[[] for i in range (no_of_applicant)] 
    for i in applicant:
        appli[k].append(i[:5])
        appli[k].append(i[5:6])
        appli[k].append(i[6:9])
        appli[k].append(i[9:10])
        appli[k].append(i[10:11])
        appli[k].append(i[11:12])
        appli[k].append(i[12:13])
        appli[k].append(i[13:20])
        k+=1

    lasp = []
    for i in range (0,no_of_applicant):
        if (appli[i][0] in lah_applicant):
            lasp.append(appli[i][0])

    for i in range (0,no_of_applicant):
        if (appli[i][0] in spla_applicant):
            lasp.append(appli[i][0])

    applicants =[] 
    for i in appli:
        if (i[0] not in lasp):
            applicants.append(i)

    lahsa=[]
    spla = []
    lahsa2 = []
    spla2 = []
    
    for i in range (0, len(applicants)):
        a = int(applicants[i][2])
        if (applicants[i][1]=='F' and a >= 18 and applicants[i][3] == 'N'):
            lahsa.append(applicants[i][0])
        if (applicants[i][4] == 'N' and applicants[i][5] == 'Y' and applicants[i][6] == 'Y'):
            spla.append(applicants[i][0])
    
    for i in range (0, len(applicants)):
        a = int(applicants[i][2])
        if (applicants[i][1]=='F' and a >= 18 and applicants[i][3] == 'N'):
            lahsa2.append(applicants[i])
        if (applicants[i][4] == 'N' and applicants[i][5] == 'Y' and applicants[i][6] == 'Y'):
            spla2.append(applicants[i])
    
    lahsa2.sort(key=count1, reverse= True)
    spla2.sort(key=count1, reverse= True)

    common=[]
    common= list(set(lahsa) & set(spla))
    
    commonpeople=[]
    for i in applicants:
        if (i[0] in common):
            commonpeople.append(i)
    commonpeople.sort(key=count1, reverse= True)
    
    lahsafin = []
    for i in lahsa:
        if (i not in common):
            lahsafin.append(i)

    lahsafinal = []
    for i in applicants:
        if (i[0] in lahsafin):
            lahsafinal.append(i)

    splafin = []
    for i in spla:
        if (i not in common):
            splafin.append(i)

    splafinal = []
    for i in applicants:
        if (i[0] in splafin):
            splafinal.append(i)

    lasfinal = []
    for i in appli:
        if (i[0] in lah_applicant):
            lasfinal.append(i)

    splfinal = []
    for i in appli:
        if (i[0] in spla_applicant):
            splfinal.append(i)

    b = []
    for i in lasfinal:
        a =  str(i[7])
        b = list(a)
        for k,j in enumerate(b):
            la_beds[k]-=int(j)

    for i in splfinal:
        a =  str(i[7])
        b = list(a)
        for k,j in enumerate(b):
            spla_parking[k]-=int(j)
            
    return (commonpeople,splafinal,lahsafinal,la_beds,spla_parking, beds, parking, lahsa2, spla2)
    
def count1(elem):
    return elem[7].count('1')

def terminalState(common):
    if not common:
        return True
    
def terminalState1(spla, lahsa):
    if not lahsa:
        return True
def terminalState2(spla, lahsa):
    if not spla:
        return True
    
def evaluateScore(la_bed, spla_parking,spla_final,lahsa_final, beds, parking, node):
    global efficiencyspla, efficiencylahsa, ans
    efficiencyspla, efficiencylahsa = 0,0
    z = []
    if (len(spla_final)!=0):
        spla_final.sort(key=count1, reverse= True)
        for i in range (len(spla_final)):
            c = []
            a =  str(spla_final[i][7])
            b = list(a)
            for k,j in enumerate(b):
                c.append (spla_parking[k]-int(j))
            if (-1 not in c):
                spla_parking = c
                z.append(spla_final[i])
    
    for i in spla_parking:
        efficiencyspla += (parking - i)
    p = []
    if (len(lahsa_final)!=0):
        lahsa_final.sort(key=count1, reverse= True)
        for i in range (len(lahsa_final)):
            c = []
            a =  str(lahsa_final[i][7])
            b = list(a)
            for k,j in enumerate(b):
                c.append(la_bed[k]-int(j))
            if (-1 not in c):
                la_bed = c
                p.append(lahsa_final[i])
                
    
    for i in la_bed:
        efficiencylahsa += (beds - i)
    
    if (len(z)!=0):
        for i in range (len(z)):
            c = []
            a =  str(z[i][7])
            b = list(a)
            for k,j in enumerate(b):
                spla_parking[k]+=int(j)
                
    if (len(p)!=0):
        for i in range (len(p)):
            c = []
            a =  str(p[i][7])
            b = list(a)
            for k,j in enumerate(b):
                la_bed[k]+=int(j)

    ans.append([node,efficiencyspla, efficiencylahsa])
    return (efficiencyspla,efficiencylahsa)

def maxSpla(common, la_bed, spla_parking, beds, parking, lahsa_final, spla_final, currentDepth, node):
    if terminalState(common):
        return evaluateScore(la_bed, spla_parking,spla_final,lahsa_final, beds, parking, node)
    vs = -float('inf')
    vl = -float('inf')
    for i in common[:]:
        q = [[]]
        q = common.pop(common.index(i)) # storing popped value
        e = q[0]
        if (currentDepth == 0):
            node = e
        c = []
        a =  str(q[7])
        b = list(a)
        for k,j in enumerate(b):
            c.append (spla_parking[k]-int(j))
        if (-1 not in c):
                spla_parking = c
#         else:
#             common.append(q)
#             continue
        s,l = maxLahsa(common, la_bed, spla_parking, beds, parking, lahsa_final, spla_final, currentDepth+1, node)
        if s>vs:
            vs = s
            vl = l
        common.append(q) #adding popped value
        for k,j in enumerate(b):
            spla_parking[k] += int(j)
    return vs,vl
    

def maxLahsa(common, la_bed, spla_parking, beds, parking, lahsa_final, spla_final, currentDepth, node):
    if terminalState(common):
        return evaluateScore(la_bed, spla_parking,spla_final,lahsa_final, beds, parking, node)
    vs = -float('inf')
    vl = -float('inf')
    for i in common[:]:
        q = [[]]
        q= common.pop(common.index(i)) # storing popped value
        flag = 0
        c = []
        a =  str(q[7])
        b = list(a)
        for k,j in enumerate(b):
            c.append (la_bed[k]-int(j))
        if (-1 not in c):
                la_bed = c
#         else:
#             common.append(q)
#             continue
        s,l = maxSpla(common, la_bed, spla_parking, beds, parking, lahsa_final, spla_final, currentDepth+1, node)
        if l>vl:
            vl = l
            vs = s
        common.append(q)
        for k,j in enumerate(b):
            la_bed[k]+=int(j)
    return vs,vl

def count2(elem):
    return elem[0]

def calc(ans):
    for x in ans:
        if (sp == x[1] and la == x[2]):
            return x[0]

def calc1(ans1):
    #ans1.sort(key=count2)
    for x in ans1:
        if (sp2 == x[1] and la2 == x[2]):
            return x[0]
        

def evaluateScore1(la_bed, spla_parking,spla, lahsa, beds, parking, node, agent):
    global efficiencyspla1, efficiencylahsa1, ans1
    efficiencyspla1, efficiencylahsa1 = 0,0
    if (agent == 0):
        z = []
        if (len(spla)!=0):
            spla.sort(key=count1, reverse= True)
            for i in range (len(spla)):
                c = []
                a =  str(spla[i][7])
                b = list(a)
                for k,j in enumerate(b):
                    c.append (spla_parking[k]-int(j))
                if (-1 not in c):
                    spla_parking = c
                    z.append(spla[i])
        for i in spla_parking:
            efficiencyspla1 += (parking - i)
        for i in la_bed:
            efficiencylahsa1+= (beds - i)
        if (len(z)!=0):
            for i in range (len(z)):
                c = []
                a =  str(z[i][7])
                b = list(a)
                for k,j in enumerate(b):
                    spla_parking[k]+=int(j)
                    
    
    elif (agent == 1):
        p = []
        if (len(lahsa)!=0):
            lahsa.sort(key=count1, reverse= True)
            for i in range (len(lahsa)):
                c = []
                a =  str(lahsa[i][7])
                b = list(a)
                for k,j in enumerate(b):
                    c.append(la_bed[k]-int(j))
                if (-1 not in c):
                    la_bed = c
                    p.append(lahsa[i])
                    
        for i in spla_parking:
            efficiencyspla1 += (parking - i)
        for i in la_bed:
            efficiencylahsa1 += (beds - i)
        
        if (len(p)!=0):
            for i in range (len(p)):
                c = []
                a =  str(p[i][7])
                b = list(a)
                for k,j in enumerate(b):
                    la_bed[k]+=int(j)
    
    ans1.append([node,efficiencyspla1, efficiencylahsa1])
    return (efficiencyspla1,efficiencylahsa1)
    
            
    


def maxSpla2(lahsa, spla, la_bed, spla_parking, beds, parking, currentDepth, node):
    vs = -float('inf')
    vl = -float('inf')
    if terminalState1(spla, lahsa):
        return evaluateScore1(la_bed, spla_parking,spla, lahsa, beds, parking, node, 0)
    if not spla:
        s,l = maxLahsa2(lahsa, spla, la_bed, spla_parking, beds, parking, currentDepth+1, node)
        if s>vs:
            vs = s
            vl = l
            
    for i in spla[:]:
        q = [[]]
        q= spla.pop(spla.index(i)) # storing popped value
        e = q[0]
        if (currentDepth == 0):
            node = e
        counter = 0
        if (q in lahsa):
            lahsa.pop(lahsa.index(q))
            counter=1
        
        c = []
        a =  str(q[7])
        b = list(a)
        for k,j in enumerate(b):
            c.append (spla_parking[k]-int(j))
        if (-1 not in c):
                spla_parking = c
#         else:
#             if(counter == 1):
#                 spla.append(q)
#                 lahsa.append(q)
#             else:
#                 spla.append(q)
#             continue
        s,l = maxLahsa2(lahsa, spla, la_bed, spla_parking, beds, parking, currentDepth+1, node)
        if s>vs:
            vs = s
            vl = l
        if (counter == 1):
            spla.append(q)
            lahsa.append(q)
        else:
            spla.append(q)
        counter = 0
        for k,j in enumerate(b):
            spla_parking[k] += int(j)
    return vs,vl


def maxLahsa2(lahsa, spla, la_bed, spla_parking, beds, parking, currentDepth, node):
    vs = -float('inf')
    vl = -float('inf')
    
    if terminalState2(spla,lahsa):
        return evaluateScore1(la_bed, spla_parking, spla, lahsa, beds, parking, node, 1)
    if not lahsa:
        s,l = maxSpla2(lahsa, spla, la_bed, spla_parking, beds, parking, currentDepth+1, node)
        if l>vl:
            vs = s
            vl = l
    for i in lahsa[:]:
        q = [[]]
        q= lahsa.pop(lahsa.index(i)) # storing popped value
        counter = 0
        if (q in spla):
            spla.pop(spla.index(q))
            counter=1
        c = []
        a =  str(q[7])
        b = list(a)
        for k,j in enumerate(b):
            c.append (la_bed[k]-int(j))
        if (-1 not in c):
                la_bed = c
#         else:
#             if(counter == 1):
#                 spla.append(q)
#                 lahsa.append(q)
#             else:
#                 lahsa.append(q)
#             continue
        s,l = maxSpla2(lahsa, spla, la_bed, spla_parking, beds, parking, currentDepth+1, node)
        if l>vl:
            vs = s
            vl = l
        if (counter == 1):
            spla.append(q)
            lahsa.append(q)
        else:
            lahsa.append(q)
        counter = 0
        for k,j in enumerate(b):
            la_bed[k] += int(j)
    return vs,vl

# def handle(signum, frame):
#     global fout,sp2,sp
#     if(sp2>sp):
#         print(chosen1,sp2,la2)
#         fout.truncate(0)
#         fout.write(str(chosen1))
#     exit()

def main():
#     start_time = time.time()
#     signal.signal(signal.SIGALRM, handle)
#     signal.alarm(178)
    global sp,la, sp2,la2
    fout = open("output.txt", "w")
    common, spla_final, lahsa_final, la_bed, spla_parking, beds, parking, lahsa, spla = input()
    temp = common
    sp ,la = maxSpla(common, la_bed, spla_parking, beds, parking, lahsa_final, spla_final, 0, [])
    chosen = calc(ans)
    fout.write(str(chosen))
    print(chosen,sp,la)
    sp2, la2 = maxSpla2(lahsa, spla, la_bed, spla_parking, beds, parking, 0, [])
    chosen1 = calc1(ans1)
    print(chosen1,sp2,la2)
    fout.close()
ans1 = []    
ans = []
main()




    

