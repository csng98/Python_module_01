class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected\n")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected\n")


class Flower(Plant):
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old, "
              f"Color: {self.color}")
        self.bloom()
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
            print(f"[asking {self.name} to bloom]")
        print()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        shade_area = self.trunk_diameter * self.height * 3.14/1000
        round_area = (int)(shade_area)
        return round_area

    def show_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade()} square meters of"
              " shade")
        print()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest{self.name}  {self.nutritional_value}")


if __name__ == "__main__":
    flower1 = Flower("Rose", 25, 30, "red")
    tree1 = Tree("Oak", 500, 1825, 50)
    veg1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===")
    print()
    plants = [flower1, tree1, veg1]
    for plant in plants:
        plant.show_info()
