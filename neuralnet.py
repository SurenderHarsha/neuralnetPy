


class neuralnet(object):

    def __init__(self,layers,nodes,threshold):

        self.neutrons={}
        for j in range(len(nodes)):

            for k in range(nodes[j]):

                layername="layer"+str(j)+str(k)
                #print layername
                self.neutrons[layername]=0

        self.threshold=threshold
        self.connections=[]
        self.layers=layers
        for i in self.neutrons:
            if layers-1==int(i[5]):
                break

            k=int(i[5])
            k=k+1
            for j in range(nodes[k]):
                ln="layer"+str(k)+str(j)
                tup=[i,0,ln]
                if tup not in self.connections:
                    self.connections.append(tup)
        #print self.connections

    def init_weights(self,weights):
        for i in range(len(self.connections)):
            self.connections[i][1]=weights[i]

    def give_inputs_to_network(self, inp):
        for i in range(len(inp)):
                name = "layer" + "0" + str(i)
                self.neutrons[name] += inp[i]

        #print self.connections
    def run_network(self,inputs,greater_than,lesser_than):
        self.give_inputs_to_network(inputs)
        for i in range(len(self.connections)):
            self.neutrons[self.connections[i][2]]+=self.connections[i][1]*self.neutrons[self.connections[i][0]]

        for i in range(len(self.connections)):
            if self.neutrons[self.connections[i][2]]>self.threshold:
                self.neutrons[self.connections[i][2]]=greater_than
            else:
                self.neutrons[self.connections[i][2]]=lesser_than

        return self.neutrons["layer"+str(int(self.layers-1))+"0"]


    def clear_network(self):
        for i in self.neutrons:
            self.neutrons[i]=0





