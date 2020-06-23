from typing import Protocol

class Named(Protocol):
    name: str

def greet(obj: Named) -> None:
    print(f"Hi {obj.name}")

class Dog:
    name = "good dog"

x = Dog()

greet(x)
