class A:
    x = 9
    def __init__(self):
        self.x = 7
    def getx(self):
        return self.x
AAA = A()

print(f"x = {A.x}")
print(f"x = {AAA.x}")
print(f"x = {AAA.getx()}")