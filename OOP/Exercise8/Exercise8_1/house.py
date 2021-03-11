# File:         house.py
# Author:
# Description:  House class

#Setting inital state of the house
class House:

    def __init__(self):

        self.bedroom_bed = "Messy"

        self.bedroom_window = "Dirty"
        self.kitchen_window = "Dirty"
        self.bathroom_window = "Dirty"

        self.bedroom_floor = "Needs vacuuming"
        self.kitchen_floor = "Needs vacuuming"
        self.bathroom_floor = "Needs vacuuming"

        self.bedroom_surfaces = "Needs dusting"
        self.kitchen_surfaces = "Needs dusting"
        self.bathroom_surfaces = "Needs dusting"

        self.fride = "Empty"

        self.toilet_paper = "Running out"

    #Cleaning windows and making the bed.
    def set_windows_and_bed(self):

        print("Making the bed.")
        self.bedroom_bed = "Made"

        print("Washing windows")

        print("Washing bedroom window")
        self.bedroom_window = "Clean"
        print("Washing kitchen windows")
        self.kitchen_window = "Clean"
        print("Washing bathroom window")
        self.bathroom_window = "Clean"
        print(self)

    #Vacuumming the floors and dusting surfaces
    def set_floors_and_surfaces(self):

        print("Starting to vacuum floors")

        print("Vacuuming bedroom")
        self.bedroom_floor = "Vacuumed"
        print("Vacuuming kitchen")
        self.kitchen_floor = "Vacuumed"
        print("Vacuuming bathroom")
        self.bathroom_floor = "Vacuumed"

        print("Rooms vacuumed, starting dusting")
        print()

        print("Dusting bedroom")
        self.bedroom_surfaces = "Dusted"
        print("Dusting kitchen")
        self.kitchen_surfaces = "Dusted"
        print("Dusting bathroom")
        self.bathroom_surfaces = "Dusted"

        print("Dusting finished")

        print(self)

    #Fill the fridge and get toiletpaper
    def set_shopping(self):

        print("Realized that you are running out of food and toilet paper.")
        print("Going shopping")

        self.fride = "Full of food"
        self.toilet_paper = "Plenty"

        print(self)

    #Get a lot more toilet paper.
    def set_pandemic_shopping(self):

        print("Realize that its pandemic and you go and hoard toilet paper")

        self.toilet_paper = "unreasonably much..."

        print(self)

    #Printing houses status.
    def __str__(self):
        return f"""
    Houses status:
    
    Bed: {self.bedroom_bed}
    
    Bedroom window: {self.bedroom_window}
    Kitchen window: {self.kitchen_window}
    Bathroom window: {self.bathroom_window}
    
    Bedroom floor: {self.bedroom_floor}
    Kitchen floor: {self.kitchen_floor}
    Bathroom floor: {self.bathroom_floor}
    
    Bedroom surfaces: {self.bedroom_surfaces}
    Kitchen surfaces: {self.kitchen_surfaces}
    Bathroom surfaces: {self.bathroom_surfaces}
    
    Fridge: {self.fride}
    
    Toilet paper: {self.toilet_paper}
    """