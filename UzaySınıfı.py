class Space(object):
    def __init__(self):
        pass
    def gravitationalAcceleration(self):
        pass
class Earth(Space):
    __gravity=9.807
    def __init__(self,mass,height):
        self.mass=mass
        self.height=height
    def gravitationalAcceleration(self):
        print("Yer Çekimi İvmesi:{}".format(self.__gravity))
    def potentialEnergy(self):
        mgh=self.mass*self.__gravity*self.height
        print("Potansiyel Enerji: ",mgh)
class Mercury(Space):
    __gravity=3.7
    def __init__(self,mass,height):
        self.mass=mass
        self.height=height
    def gravitationalAcceleration(self):
        print("Yer Çekimi İvmesi:{}".format(self.__gravity))
    def potentialEnergy(self):
        mgh=self.mass*self.__gravity*self.height
        print("Potansiyel Enerji: ",mgh)
        return 
class Venus(Space):
    __gravity=8.87
    def __init__(self,mass,height):
        self.mass=mass
        self.height=height
    def gravitationalAcceleration(self):
        print("Yer Çekimi İvmesi:{}".format(self.__gravity))
    def potentialEnergy(self):
        mgh=self.mass*self.__gravity*self.height
        print("Potansiyel Enerji: ",mgh)
    
    
    
e1=Earth(10,100) #Mass(kütle),Height(Yükseklik)
m1=Mercury(15, 300) #Mass(kütle),Height(Yükseklik)
v1=Venus(20, 200) #Mass(kütle),Height(Yükseklik)

e1.potentialEnergy()
e1.gravitationalAcceleration()
print("-"*20)
m1.potentialEnergy()
m1.gravitationalAcceleration()
print("-"*20)
v1.potentialEnergy()
v1.gravitationalAcceleration()