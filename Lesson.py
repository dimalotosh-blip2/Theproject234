
class МоваПрограмування:
    def __init__(self, імʼя):
        self.імʼя = імʼя 

    def вивести_привітання(self):
        print(f"Привіт від мови програмування {self.імʼя}!")

class Python(МоваПрограмування):
    def __init__(self):
        super().__init__("Python")

    def вивести_привітання(self):
        print(f"Привіт! Я {self.імʼя}, і я відомий своєю простотою.")

class JavaScript(МоваПрограмування):
    def __init__(self):
        super().__init__("JavaScript")
    
class Java(МоваПрограмування):
    def __init__(self):
        super().__init__("Java")
    
    def компілювати(self):
        print(f"{self.імʼя} компілюється для віртуальної машини Java (JVM).")
 