class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self,amount):
        self.health -= amount
        
class warrior(Character):
    pass        
        
warrior = warrior(100,50,10)
print(f'Initial health: {warrior.health}')
warrior.take_damage(40)
print(f'Health after damage: {warrior.health}')            
         