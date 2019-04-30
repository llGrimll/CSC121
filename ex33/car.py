###############################################################################
#
# ex33 in-class 4/25/19 - OOP
#
###############################################################################


class Car:
    """Class takes specifications of new cars."""

    my = "Brand New - Model Year 2020:"

    #  constructor method init
    def __init__(self, make, model, color, price):
        """Return the make and model of a new car."""
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        # nu += 1

    def __str__(self):
        """Return make and model of new car."""
        return f"{Car.my}, {self.make}, {self.model}, {self.color}, {self.price}."


class Used(Car):
    def __init__(self, year, make, model, color, miles, price):
        """Add Miles and price to used car class."""
        super().__init__(make, model, color, price)
        self.year = year
        self.miles = miles

    def __str__(self):
        """Return make and model of used car."""
        return f"Certified Pre-Owned: {self.year} {self.make} {self.model}, {self.color}, {self.miles} miles, ${self.price}."
