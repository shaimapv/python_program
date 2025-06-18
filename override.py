class Fruit_basket:
    def __init__(self,owner,fruit_count):
        self.owner=owner
        self.fruit_count=fruit_count
    
    def __str__(self):
        return f"{self.owner} has {self.fruit_count} fruits"
    def __add__(self,other):
        total=self.fruit_count + other.fruit_count
        return f"combined basket of {self.owner} and {other.owner} has {total} fruits."
    def __sub__(self,other):
        difference=self.fruit_count-other.fruit_count
        if difference>0:
            return f"{self.owner}'s basket has {difference} fruit more than {other.owner}"
        elif (difference<0):
            return f"{other.owner}'s basket has {-difference} fruit more than {self.owner}"
        else:
            return f"{self.owner} and {other.owner} has same number of fruits."
        
    
basket1= Fruit_basket("rama",20)
basket2=Fruit_basket("deepa",30)

print(basket1)
print(basket2)

print(basket1+basket2)
print(basket1-basket2)

    
