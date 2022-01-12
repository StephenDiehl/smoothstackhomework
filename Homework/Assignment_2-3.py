names = ["Stephen", "John", "Karinna", "Paul"]

def crowded(names):
    if len(names) > 3:
        print('The room is crowded')
crowded(names)
names.pop()
names.pop()
crowded(names)



#---------------------------------------------------------



names = ["Stephen", "John", "Karinna", "Paul"]

def crowdedv2(names):
    if len(names) > 3:
        print("It's Crowded in here")
    else:
        print("The room is not very crowded in here.")


crowdedv2(names)
names.pop()
names.pop()
crowdedv2(names)


#---------------------------------------------------------


names = ["Stephen", "John", "Karinna", "Paul", "Ian", "Tiffany"]

def crowdedv3(names):
    if len(names) == 0:
        print("The room is empty")
    elif len(names) > 5:
        print('ITS A MOB')
    elif len(names) >= 3 and len(names) <=5:
        print('The room feels crowded')
    else:
        print("The room is not crowded yet")


crowdedv3(names)
names.pop()
names.pop()
crowdedv3(names)
names.pop()
names.pop()
crowdedv3(names)
names = []
crowdedv3(names)