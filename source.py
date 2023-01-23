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

file=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 2/Source.txt","r")
file3=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 2/POI.txt","r")
file2=open("Output2.txt",'w')

object_List=[]
test_object=None 

content=file.read().split('\n')
content3=file3.read().split('\n')

def polygon_create():
    for i in np.arange(len(content)):
        if "boundary" not in content[i]:
            file2.write(content[i])
            file2.write('\n')

        if "boundary" in content[i]:
            file2.write("boundary\n")
            i+=1
            object=polygon()
            while "endel" not in content[i]:
                if "layer" in content[i]: 
                    number=content[i].split('layer ')
                    number=number[1]
                    object.layer=number
                elif "xy" in content[i]: 
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
                        List2.append(int(x[count2]))
                        List2.append(int(x[count2+1]))
                        List.append(List2)
                        count2+=3
                        value-=1
                    object.ordinates=List
                    object_List.append(object)
                i+=1   

polygon_create()
content=content3
file2.close()
file2=open("Output2.txt",'w')
polygon_create()

test_object=object_List[-1]
object_List.pop() 

List2=[]
x,y=test_object.ordinates[0]
for x1,y1 in test_object.ordinates: 
    List2.append([x1-x,y1-y])

test_object.ordinates=List2

result_List=[] 
for objects in object_List: 
    List2=[]
    x,y=objects.ordinates[0]
    for x1,y1 in objects.ordinates: 
        List2.append([x1-x,y1-y])

    if(List2==test_object.ordinates):
        new=[]
        new.append('boundary')
        new.append('\n')
        new.append('layer ')
        new.append(f'{objects.layer}\n')
        new.append('datatype 0\n')
        new.append(f'xy  {objects.n}  ')
        coList=''
        for x,y in objects.ordinates: 
            coList+=f'{x} {y}  '
        coList+='\n'
        new.append(coList)
        new.append('endel\n')
        result_List.append(new)
file2.close()
print(len(result_List))
file2=open("Output2.txt",'w')
file=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 2/Source.txt",'r').read() 
content=file.split('\n')
enter=0
for i in np.arange(len(content)): 
    if("boundary" in content[i]):
        for line in result_List: 
            file2.write(''.join(line))
        break 
    else: 
        file2.write(content[i]) 
        file2.write('\n')

file2.write("endstr\n")
file2.write("endlib\n")