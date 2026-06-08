class Plant:
    class PlantStats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.PlantStats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

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

    def grow(self, height_grown: float) -> None:
        if height_grown >= 0:
            self._height += height_grown
        self._stats.increment_grow()

    def age(self, age_added: int) -> None:
        if age_added >= 0:
            self._age += age_added
        self._stats.increment_age()

    def show(self) -> None:
        self._stats.increment_show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0  # Trees need extra stats tracking

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0
        self.color = color

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_analytics(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._stats.display()
    if hasattr(plant, '_shade_calls'):
        print(f"{plant._shade_calls} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_plant_analytics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_analytics(rose)
    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_analytics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_analytics(oak)
    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_analytics(sunflower)
    print()
    print("=== Anonymous")
    anon_plant = Plant.create_anonymous()
    anon_plant.show()
    display_plant_analytics(anon_plant)
