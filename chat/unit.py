class Unit:
    def __init__(self, name, content, age:int):
        self.name, self.content, self.age = name, content, age

    def __str__(self):
        return f"Personne: {self.name}, âge: {self.age}, content: {self.content}"

    def is_beetwen(self, first, second):
        if self.age <= max(first, second) and self.age >= min(first, second):
            return True
        return False
    
    