import numpy as np 
import math 

class polygon: 
    def __init__(self):
        self.n=0 
        self.layer=0 
        self.ordinates=[]
    def display(self):
        print("Vertices: ",self.n)
        print("Layer: ",self.layer)
        print("Co-ordinate: ",self.ordinates)

file=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 4/Source.txt","r")
file3=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 4/POI.txt","r")
file2=open("Output4.txt",'w')

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
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
  
    return x

def dist(List1,List2): 
    return ((List2[1]-List1[1])**2+(List2[0]-List1[0])**2)

def angle(a,b,c,d):
    
     dotProduct = a*c + b*d
         # for three dimensional simply add dotProduct = a*c + b*d  + e*f 
     modOfVector1 = math.sqrt( a*a + b*b)*math.sqrt(c*c + d*d) 
         # for three dimensional simply add modOfVector = math.sqrt( a*a + b*b + e*e)*math.sqrt(c*c + d*d +f*f) 
     angle = dotProduct/modOfVector1
     #angleInDegree = math.degrees(math.acos(angle))
     return angle
     
## the function I was working on
## this is not working 
# def checkFunction(List1,List2,List3): 
#     dist1=[]
#     dist2=[]
#     List1+=List2
#     for point1 in List1:
#         for point2 in List1: 
#             if(point1!=point2):
#                 dist1.append([dist(point1,point2),round(angle(point1[0],point1[1],point2[0],point2[1]),2)])

#     for point1 in List3: 
#         for point2 in List3: 
#             if(point1!=point2):
#                 dist2.append([dist(point1,point2),round(angle(point1[0],point1[1],point2[0],point2[1]),2)])

#     # gcd=find_gcd(dist1[0][0],dist1[1][0])
#     # for i in range(2,len(dist1)):
#     #     gcd=find_gcd(gcd,dist1[i][0])

#     # gcd1=find_gcd(dist2[0][0],dist2[1][0])
#     # for i in range(2,len(dist2)):
#     #     gcd1=find_gcd(gcd1,dist2[i][0])

#     # for i in range(len(dist1)): 
#     #     dist1[i][0]/=gcd 
#     # for i in range(len(dist2)):
#     #     dist2[i][0]/=gcd1

#     if(dist1==dist2):
#         return True 
#     return False 

## this function has 100% accuracy but 65% purity
def checkFunction(List1,List2): 
    dist1=[]
    dist2=[]
    for point1 in List1:
        for point2 in List1: 
            if(point1!=point2):
                dist1.append(dist(point1,point2))
    for point1 in List2:
        for point2 in List2: 
            if(point1!=point2):
                dist2.append(dist(point1,point2))
    gcd=find_gcd(dist1[0],dist1[1])
    for i in range(2,len(dist1)):
        gcd=find_gcd(gcd,dist1[i])

    gcd1=find_gcd(dist2[0],dist2[1])
    for i in range(2,len(dist2)):
        gcd1=find_gcd(gcd1,dist2[i])

    for i in range(len(dist1)): 
        dist1[i]/=gcd 
    for i in range(len(dist2)):
        dist2[i]/=gcd1

    if(set(dist1)==set(dist2)):
        return True 
    return False 

polygon_create()
content=content3
file2.close()
file2=open("Output4.txt",'w')
polygon_create()

test_object=object_List[-1]
object_List.pop() 
test_object1=object_List[-1]
object_List.pop()


print(test_object.ordinates)
print(test_object1.ordinates)

result_List=[] 
for objects in object_List: 
    if(checkFunction(test_object.ordinates,objects.ordinates) or checkFunction(test_object1.ordinates,objects.ordinates)):
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
file2=open("Output4.txt",'w')
file=open("C:/Users/geetha/OneDrive/Documents/codes visual/Projects/KLA/Data/Milestone_Input/Milestone_Input/Milestone 4/Source.txt",'r').read() 
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