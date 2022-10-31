class Player:
    name = 'Player'

    def __init__(self):
        self.x = 100

    def wherer(self):
        print(self.x)

player = Player()

player.wherer()

print(Player.name)
print(player.name)

#Player.wherer() # error
Player.wherer(player) # plyaer.where() 과 같다