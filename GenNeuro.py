from neuralnet import *
import random
c=neuralnet(3,[2,2,1],0.5)
c.init_weights([0.7,0.8,0.3,0.4,0.5,0.6])
print c.run_network([1,1],1,0)
inputs=[[0,0],[0,1],[1,0],[1,1]]
outputs=[0,0,0,1]

mutation=1
n_w=6
p_size=100

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
def fitness_function(weights):
    c.init_weights(weights)
    score=0
    for i in range(len(inputs)):
        k=c.run_network(inputs[i],1,0)
        if k==outputs[i]:
            score+=1
    return (float(score)/len(outputs))*100


def gen_population(size,len):
    pop=[]
    for i in range(size):
        r=[]
        for j in range(len):
            k=random.randint(1,9)
            k=float(k)/10
            r.append(k)

        pop.append(r)

    return pop


def create_pairs(pop):
    pai=[]
    selected=[]
    pi=[]
    pop_score=[]
    for i in pop:
        pop_score.append([i,fitness_function(i)])

    p=sorted(pop_score,key=lambda x:x[1])
    l=max(p,key=lambda x:x[1])
    l=l[1]
    p=p[::-1]
    #print p
    pop=[]
    for i in p:
        pop.append(i[0])

    while len(pai)*2<len(pop):
        if len(pi)==2:
            pai.append(pi)
            pi=[]
            continue

        for i in p:
            if len(pi)==2:
                break
            k=random.randint(0,l)
            if k<=i[1]:
                if i[0] not in selected:
                    selected.append(i[0])
                    pi.append(i[0])


    return pai


def crossover(pairs):
    po=[]
    st=len(pairs)*2

    for i in pairs:
        a=i[0]
        b=i[1]
        l=len(a)/2
        t=random.randint(0,len(a)-1)
        x=a[:t]+b[t:]
        y=b[:t]+a[t:]
        x1=b[t:]+a[:t]
        y1=a[t:]+b[:t]
        x2=a[:l]+b[l:]
        y2=b[:l]+a[l:]
        dic=[]


        dic.append([x,fitness_function(x)])
        dic.append([y, fitness_function(y)])
        dic.append([x1, fitness_function(x1)])
        dic.append([y1, fitness_function(y1)])
        dic.append([x2, fitness_function(x2)])
        dic.append([y2, fitness_function(y2)])



        sorted_child = sorted(dic, key=lambda x:x[1])
        flag=0
        sorted_child=sorted_child[::-1]
        for i in sorted_child:
        	if flag>=2:
        		break
        	if i[0] not in po:
        		po.append(i[0])
                flag+=1

    po=Remove(po)
    for i in range(st-len(po)):
        k=gen_population(1,len(pairs[0][0]))[0]
        if k not in po:
            po.append(k)


    return po

def mutations(pop):
    st=len(pop)
    for i in range(len(pop)):
        k=pop[i]
        for j in range(len(k)):
            c=random.randint(0,100)
            if c<=mutation:
                p=random.randint(1,9)
                p=float(p)/10
                k[j]=p

    pop=Remove(pop)
    for i in range(st-len(pop)):
        k=gen_population(1,len(pop[0]))[0]
        if k not in pop:
            pop.append(k)
    return pop


population=gen_population(p_size,n_w)
best_fitness=0
best_weights=[]
while best_fitness<100:

    cr=create_pairs(population)
    cr=crossover(cr)
    cr=mutations(cr)
    avg=0
    for i in cr:
        r=fitness_function(i)
        avg+=r
        if r>best_fitness:
            best_fitness=r
            best_weights=i

    avg=float(avg)/len(cr)
    population=cr
    #print population
    print avg,"AVG"
    print best_weights,"WEIGHTS"
    print best_fitness,"Fitness"






