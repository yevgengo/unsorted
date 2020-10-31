#!/usr/local/bin/python
#given a number of coordinates of names,radii and sequences of flowers produce the one that has largest bloom
# given number of vertices, radii and coordinates of points produce the longest graph chain\link from given coordinates
import matplotlib.pyplot as plt
import random
import math

random.seed
class flower:
    def __init__(self):
        self.name=random.choice("abcdefghijklmnopqrstuvwxyz")+str(random.randint(1,100))
        self.xcoord=random.randint(-100,100)
        self.ycoord=random.randint(-100,100)
        self.radius=random.randint(1,100)
    def distance (self,other) -> float:
        return math.sqrt((self.xcoord-other.xcoord)**2+(self.ycoord-other.ycoord)**2)

    def create_circle(self,desirededgecolor='red'):
        self.circle=plt.Circle((self.xcoord,self.ycoord),radius=self.radius,facecolor='none',edgecolor=desirededgecolor)


def buildchains(targetelement,entirelist,currentoutputlist):
    longestlist=[targetelement]
    outputlist=[targetelement]
    nearlist=[]
    if (entirelist==[]):
        return []

    if (entirelist==[targetelement]):
        return []
    
    if (currentoutputlist != [] and targetelement in currentoutputlist ):
        return []

    else:
        for element in entirelist:
            if (targetelement.distance(element)!=0 and ((targetelement.distance(element)<=element.radius) or targetelement.distance(element)<=targetelement.radius)):
                if (element not in nearlist):
                    nearlist=nearlist+[element]

        for nearelement in nearlist:
            if (nearelement not in currentoutputlist and nearelement not in outputlist):
                outputlist=outputlist+[nearelement]
                outputlist=outputlist+buildchains(nearelement,entirelist,outputlist)
                longestlist=list(set(outputlist).union(set(longestlist)))

#            if (len(outputlist)>len(longestlist)):
#                longestlist=outputlist

    return longestlist
        



if __name__=="__main__":
    ourflowerfield=[]
    output=[]
    currentflower=flower()

    for i in range (1,10):
        currentflower=flower()

        ourflowerfield=ourflowerfield+[currentflower]

    fig,ax=plt.subplots(figsize=(15,10))
    ax.axis('scaled')
    plt.xlim(-200,200)
    plt.ylim(-200,200)
    for element in ourflowerfield:
        print(element.name,element.xcoord,element.ycoord,element.radius)
        element.create_circle()
        ax.add_patch(element.circle)
    

    for element in ourflowerfield:
        candidateoutput=[]
        candidateresult=[]

        candidateoutput=buildchains(element,ourflowerfield,[])
        if(len(candidateresult)<len(candidateoutput)):
            candidateresult=candidateoutput
        for secondelement in candidateresult:
            if (secondelement in candidateresult):
                candidateresult=list(set(candidateresult).union(set(candidateoutput)))
            if (secondelement in output):
                output=list(set(candidateresult).union(set(output)))
            else:
                if(len(output)<len(candidateresult)):
                    output=candidateresult


#        print("outputishere with length of ",len(output))


    
    for element in output:
        print (element.name,element.xcoord,element.ycoord,element.radius)
        element.create_circle('green')
        ax.add_patch(element.circle)
#        ax.legend([element.circle],[element.name])

    plt.show()

