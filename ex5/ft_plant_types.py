class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height_grown: float) -> None:
        if height_grown >= 0:
            self._height = height_grown

    def get_age(self) -> int:
        return self._age

    def set_age(self, age_added: int) -> None:
        if age_added >= 0:
            self._age = age_added

    def grow_and_age(self, height_grown: float, age_added: int) -> None:
        if height_grown >= 0:
            self._height += height_grown
        if age_added >= 0:
            self._age += age_added

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        print(f"{self.name.capitalize()} has not bloomed yet")

        print(f"[asking the {self.name} to bloom]")
        self.bloom()

        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")
        print(f"Color: {self.color}")
        if self._is_blooming is True:
            print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._is_producing_shade = False

    def produce_shade(self) -> None:
        self._is_producing_shade = True
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")
        print(f"[asking the {self.name} to produce shade]")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = int(nutritional_value)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")
        print(f"[make {self.name} grow and age for 20 days]")
        self.grow_and_age(42.0, 20)
        self.nutritional_value = 20
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    flower1 = Flower("rose", 15.0, 10, "red")
    tree1 = Tree("oak", 200.0, 365, 5.0)
    veg1 = Vegetable("tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Flower.show(flower1)
    print()
    print("=== Tree")
    Tree.show(tree1)
    print()
    print("=== Vegetable")
    Vegetable.show(veg1)
