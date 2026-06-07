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
            self._height = height_grown  # Set directly during initialization

    def get_age(self) -> int:
        return self._age

    def set_age(self, age_added: int) -> None:
        if age_added >= 0:
            self._age = age_added        # Set directly during initialization

    def grow_and_age(self, height_grown: float, age_added: int) -> None:
        """Helper method to accumulate growth and age later on."""
        if height_grown >= 0:
            self._height += height_grown
        if age_added >= 0:
            self._age += age_added


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show_info(self) -> None:
        print("=== Flower")
        # Initial status
        print(f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")
        print(f"Color: {self.color}")
        print(f"{self.name} has not bloomed yet")
        
        # Action
        print(f"[asking the {self.name.lower()} to bloom]")
        self.bloom()
        
        # Updated status
        print(f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")
        print(f"Color: {self.color}")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show_info(self) -> None:
        print("=== Tree")
        print(f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")
        
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.get_height():.1f}cm long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = int(nutritional_value)  # Ensure it is an integer

    def show_info(self) -> None:
        print("=== Vegetable")
        # Initial status
        print(f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")
        
        # Action: Grow 42.0cm and age 20 days, update nutrition to 20
        print(f"[make {self.name.lower()} grow and age for 20 days]")
        self.grow_and_age(42.0, 20)
        self.nutritional_value = 20
        
        # Updated status
        print(f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    flower1 = Flower("Rose", 15.0, 10, "red")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    veg1 = Vegetable("Tomato", 5.0, 10, "April", 0)
    
    print("=== Garden Plant Types ===")
    plants = [flower1, tree1, veg1]
    for plant in plants:
        plant.show_info()
