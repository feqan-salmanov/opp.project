import random,os

class Esger():
    def __init__(self):
        self.hayattami = True
        self.can = random.randint(10,40)
        self.vurus = random.randint(40,50)
        self.qalxan = random.randint(10,30)
    def vur(self,player):
        damage = self.vurus - player.qalxan
        player.can -= damage
        if player.hayattami <= 0:
            player.hayattami = False

class Player():
    def __init__(self):
        self.hayattami = True
        self.can = 600
        self.vurus = 60
        self.qalxan =40
    def vur(self,esger):
        damage = self.vurus - esger.qalxan
        esger.can -= damage
        if esger.can <= 0:
            esger.hayattami = False
            esgerler.remove(esger)
esgerler = list()
for i in range(10):
    esgerler.append(Esger())
player = Player()
while True:
    os.system("cls") #mac ucun "clear"
    print("Player ----->>>>> Can: {} ------->>>>> Vurus: {} ------->>>>> Qalxan:{}".format(player.can,player.vurus,player.qalxan))
    if player.hayattami == False :
        print("GAE OVER !!... :(")
        quit()
    if not esgerler:
        print("Tebrikler .... :)")
    for i in esgerler:
        print("{}.Esger ----->>>>> Can: {} ------->>>>> Vurus: {} ------->>>>> Qalxan:{}".format(esgerler.index(i),i.can,i.vurus,i.qalxan))
    secim =int(input("Esger secin :"))
    esger = esgerler[secim]
    player.vur(esger)
    if esgerler:
        saldiran = esgerler[random.randint(0,len(esgerler)-1)]
        saldiran.vur(player)
