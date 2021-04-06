class Animal:
    def __init__(self,age,weight,color):
        self.age=age
        self.weight=weight
        self.color=color

    def __str__(self):
      return self.age

class Felin(Animal):
  def attributs(self,tile_lenght):       
        self.tile_lenght=tile_lenght
        
  def eat(self,kgm):
        self.__weight +=kgm
        print("The animal weights" + str(self.__weight) + "kg after eating.")
        
  def switch_color(self,c):
        self.color=c
        print("La couleur est "+str(self.color) )

class bird(Animal):
  def attributs(self,taille):
        self.taille=taille
        
  def tweet(self):
        print("cuicui")
        
        
  def poid_taille(self):
        print("Le rapport est de "+str(self.taille/self.weight))

