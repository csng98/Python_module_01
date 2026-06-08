class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self._height

    def set_height(self, new_height: int) -> None:
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

    def current_info(self) -> None:
        print(f"Current state: {self.name} {self._height}cm,"
              f" {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25, 30)
    print()
    plant1.set_height(-5)
    plant1.set_age(-5)
    plant1.current_info()
