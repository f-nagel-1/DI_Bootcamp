import random



class Gene:
    def __init__(self):
        self.state = random.randint(0,1)

#it can mutate => has to be attribute
#  
    def flip(self):
        self.state = 0 if self.state == 1 else 1

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for i in range(0,10)]
        print("created 10 genes")


    def mutate(self):
        indexs = list(range(0,len(self.genes)))
        random.shuffle(indexs)
        print("shuffeled indexes", indexs)
        index_sub_selection = indexs[0:random.choice(indexs)]
        print("the shuffled subselection")
        for indx in index_sub_selection:
            if random.randint(0,1):
                self.genes[indx].flip()
                print("i flipped")
            else:
                print("I didnt")
            
chromo = Chromosome()
chromo.mutate()

class DNA:
    def __init__(self):
        self.chromoses = [Chromosome() for i in range(10)]
    
    