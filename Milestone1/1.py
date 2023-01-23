import numpy as np 
class polygon: 
    def __init__(self):
        self.n=0 
        self.layer=0 
        self.ordinates=[]
    def display(self):
        print("Vertices: ",self.n)
        print("Layer: ",self.layer)
        print("Co-ordinate: ",self.ordinates)

file=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 1/Format_Source.txt","r")

file2=open("Output.txt",'w')
object_List=[]
content=file.read().split('\n')

enter=0 
count=0
for i in np.arange(len(content)):
    if "boundary" not in content[i]:
        file2.write(content[i])
        file2.write('\n')

    if "boundary" in content[i]:
        file2.write("boundary\n")
        count+=1 
        i+=1
        if(count>2): 
            break 
        object=polygon()
        while "endel" not in content[i]:
            if "layer" in content[i]: 
                number=content[i].split('layer ')
                number=number[1]
                object.layer=number
            elif "xy" in content[i]: 
                enter=1
                List=content[i].split(' ')
                x=content[i].split('xy')
                x=x[1]
                x=x.split(' ')
                object.n=int(x[2])
                value=object.n
                count2=4
                List=[]
                while(value>0):
                    List2=[]
                    List2.append(x[count2])
                    List2.append(x[count2+1])
                    List.append(List2)
                    count2+=3
                    value-=1
                object.ordinates=List
                object.display()
                object_List.append(object)
            i+=1   

file2.write("endstr\n")
file2.write("endlib\n")

file2.close()
     