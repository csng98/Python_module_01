class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def update(self, gpd: float) -> None:
        self.height += gpd
        self.age += 1

    def show_status(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show_status()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.update(gpd=0.8)
        rose.show_status()
    total_growth = rose.height - start_height
    print(f"Growth this week: {total_growth:.1f}cm")