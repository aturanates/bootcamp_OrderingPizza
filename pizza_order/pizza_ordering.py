import csv
import datetime

class Pizza:
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 10.0)
    def __str__(self):
         return """
        Our pizza starts with a freshly made dough, hand-stretched to create the perfect crust. We use only the finest quality ingredients for our toppings, including tangy tomato sauce, creamy mozzarella cheese, and a variety of delicious meats and vegetables.

        Whether you prefer a classic margherita with its simple yet satisfying combination of tomato sauce, mozzarella, and fresh basil, or a meat lover's pizza piled high with pepperoni, sausage, and bacon, we've got you covered. Vegetarians can enjoy our veggie pizza, loaded with mushrooms, onions, peppers, and olives, or customize their own pizza with their favorite veggies.

        Our pizza is baked in a traditional wood-fired oven, ensuring that the crust is crispy and golden brown, while the toppings are cooked to perfection. Every slice is bursting with flavor and satisfaction, making our pizza the perfect choice for any occasion.
            """



class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 12.0)
    def __str__(self):
        return """
        This pizza starts with a freshly made dough, hand-stretched to create the perfect crust. We then top it with a tangy tomato sauce made from the freshest ingredients, and a generous amount of creamy, melted mozzarella cheese.

        To finish it off, we add a sprinkle of fragrant fresh basil leaves, which gives this pizza its signature flavor and aroma.

        The Margherita pizza has a rich history, dating back to the late 19th century in Naples, Italy. It was named after Queen Margherita of Savoy, who reportedly fell in love with this simple yet delicious pizza during a visit to Naples.

        At our restaurant, we take pride in honoring this traditional recipe and using only the best quality ingredients. Our Margherita pizza is baked in a traditional wood-fired oven, ensuring a crispy and golden crust that perfectly complements the savory and aromatic toppings.
        """

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 15.0)
    def __str__(self):
        return"""
        Pide is a traditional Turkish flatbread that is similar to pizza but with its own distinctive flavor and texture. Our Pide starts with a freshly made dough that is hand-rolled and shaped into a long, oval shape.

        We then add a variety of delicious toppings, including spiced ground beef or lamb, fresh vegetables such as tomatoes, onions, and peppers, and a sprinkle of tangy feta cheese.

        Our Pide is baked in a stone oven, ensuring that the crust is crispy and golden brown while the toppings are cooked to perfection. Once it comes out of the oven, we add a drizzle of olive oil and a sprinkle of fresh herbs such as parsley or oregano for a burst of flavor.

        This Turkish pizza is perfect for those who want to try something different yet still crave the comforting flavors of pizza. It's also a great option for those who follow a halal diet as all of our meat is halal-certified.
        """

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 18.0)
    def __str__(self):
        return """
        Our pizzas are made with only the freshest and highest quality ingredients, including a hand-tossed crust made from our signature dough recipe. We then add a layer of tangy tomato sauce made with vine-ripened tomatoes and a blend of savory herbs and spices.

        Our toppings are always fresh and delicious, including premium meats like pepperoni, sausage, and bacon, as well as a variety of fresh vegetables such as mushrooms, onions, and peppers. We also offer a range of specialty pizzas like the classic Meat Lovers or the popular Hawaiian, all loaded with toppings for the ultimate flavor experience.

        At Domino's, we pride ourselves on our commitment to quality and convenience. That's why we offer fast and friendly delivery straight to your doorstep, or you can choose to pick up your order at one of our many locations.

        We also have a range of delicious sides and desserts to complement your pizza, including hot wings, garlic bread, and our famous lava cakes.
        """


class Decorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description()

    def get_cost(self):
        return self._pizza.get_cost()


class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cost = 2.0

    def get_description(self):
        return self._pizza.get_description() + ", Olives"

    def get_cost(self):
        return self._pizza.get_cost() + self._cost


class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cost = 3.0

    def get_description(self):
        return self._pizza.get_description() + ", Mushrooms"

    def get_cost(self):
        return self._pizza.get_cost() + self._cost


class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cost = 4.0

    def get_description(self):
        return self._pizza.get_description() + ", Goat Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + self._cost


class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cost = 5.0

    def get_description(self):
        return self._pizza.get_description() + ", Meat"

    def get_cost(self):
        return self._pizza.get_cost() + self._cost


class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cost = 2.5

    def get_description(self):
        return self._pizza.get_description() + ", Onions"

    def get_cost(self):
        return self._pizza.get_cost() + self._cost


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._cost = 3.5

    def get_description(self):
        return self._pizza.get_description() + ", Corn"

    def get_cost(self):
        return self._pizza.get_cost() + self._cost


#Main

menu_file = open("menu.txt","r")
print(menu_file)