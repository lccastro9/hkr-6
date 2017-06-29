class Point():
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
    def move(self,x,y):
        self.x1=x
        self.y1=y   
    def reset(self):
        self.x=0
        self.y=0   
    def calculate_distance(self,otherPoint):
        a=(otherPoint.x-self.x)**2 + (otherPoint.y-self.y)**2
        distancia = a**0.5
        return distancia
        
D=[]

for i in range((int(raw_input())/2)):
	D.append(Point(*map(int,raw_input().split())).Distancia(Point(*map(int,raw_input().split()))))

for i in D:
    print i
