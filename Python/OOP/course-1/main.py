# class IceCream:
    
#     def __init__(self):
#         self.scoops = 3

#     def eat(self):
#         print("Yum!")


# ice_cream = IceCream()
# print(ice_cream.scoops)
# ice_cream.eat()


# class IceCream:

#     def __init__(self):
#         self.scoops = 3

#     def eat(self, scoops):
#         if self.scoops < scoops:
#             print('Sorry this is amount is missing!')
#         else:
#             self.scoops -= scoops

#     def add(self, scoops):
#         self.scoops += scoops

# ice_cream = IceCream()
# print(ice_cream.scoops)
# ice_cream.eat(4)
# print(ice_cream.scoops)
# ice_cream.add(3)
# print(ice_cream.scoops)

# the first step of learning is over #

# class Light:

#     def __init__(self):
#         self.on = False
    
#     def toggle(self):
#         self.on = not self.on
#         print(self.on)
    
#     def is_on(self):
#         if self.on == False:
#             print('light is off!')
#         else:
#             print('light is on!')


# light = Light()
# light.toggle()
# light.is_on()

# the second step of learning is over #

# class Light:

#     on = False

# a = Light()
# b = Light()

# a.on = True

# print(a.on)
# print(b.on)

# Light.on = True 

# print(a.on)
# print(b.on)

# Light.on = False 

# print(b.on)
# print(a.on)

# the third stage of learning is over #

# class IceCream:

#     max_scoops = 3

#     def __init__(self):
#         self.scoops = self.max_scoops

#     def eat(self, scoops):
#         if self.scoops < scoops:
#             print('Sorry this is amount is missing!')
#         else:
#             self.scoops -= scoops

#     def add(self, scoops):
#         self.scoops += scoops

#         if self.scoops > self.max_scoops:
#             self.scoops = 0
#             print('Too many scoops! dropped ice cream.')


# class IceCreamTruck:

#     min_sold = 0

#     def __init__(self):

#         self.sold = self.min_sold

#     def order(self, scoops):
#         ice_cream = IceCream()
#         self.add(ice_cream, scoops)
#         return ice_cream


#     def add(self, ice_cream, scoops):
        
#         ice_cream.add(scoops)
#         self.sold += scoops


# truck = IceCreamTruck()
# icecream = truck.order(3)
# icecream.eat(2)
# truck.add(icecream, 1)
# print(truck.sold)

# the fourth stage of learning is over #

# class Light:

#     def __init__(self, sync=None):
#         self.on = False
#         self.sync = sync
    
#     def toggle(self):
#         self.on = not self.on
        
#         if self.sync is not None:
#             self.sync.toggle()

#         print(self.on)
    
#     def is_on(self):
#         if self.on == False:
#             print('light is off!')
#         else:
#             print('light is on!')

# light1 = Light()
# light2 = Light(sync=light1)
# light2.toggle()

# light1.is_on()
# light2.is_on()

# the fiveth stage of learning is over #

# class IceCream:

#     max_scoops = 3

#     def __init__(self):
#         super().__init__()
#         self.scoops = self.max_scoops

#     def eat(self, scoops):
#         if self.scoops < scoops:
#             print('Sorry this is amount is missing!')
#         else:
#             self.scoops -= scoops

#     def add(self, scoops):
#         self.scoops += scoops

#         if self.scoops > self.max_scoops:
#             print('Too many scoops! dropped ice cream.')
#             self.scoops = 0



# class IceCreamTruck:

#     def __init__(self):
#         super().__init__()
#         self.sold = 0
 
#     def order(self, scoops):
#         ice_cream = IceCream()
#         self.add(ice_cream, scoops)
#         return ice_cream


#     def add(self, ice_cream, scoops):
        
#         ice_cream.add(scoops)
#         self.sold += scoops 

# class DeluxeIceCreamTruck(IceCreamTruck):

#     def order(self, scoops):
#         ice_cream = super().order(scoops)
#         ice_cream.add(1)
#         return ice_cream
    
# truck = DeluxeIceCreamTruck()
# ice_cream  = truck.order(2)
# print(ice_cream.scoops)
# data = truck.sold
# print(data)

# the sixth stage of learning is over #
