# class IceCream:
    
#     def __init__(self):
#         self.scoops = 3

#     def eat(self):
#         print("Yum!")


# ice_cream = IceCream()
# print(ice_cream.scoops)
# ice_cream.eat()


class IceCream:

    def __init__(self):
        self.scoops = 3

    def eat(self, scoops):
        self.scoops -= scoops

ice_cream = IceCream()
print(ice_cream.scoops)
ice_cream.eat(2)
print(ice_cream.scoops)