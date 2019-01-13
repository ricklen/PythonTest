from player import Player
from enemy import Enemy

rick = Player("Rick")

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(6)
print(random_monster)
