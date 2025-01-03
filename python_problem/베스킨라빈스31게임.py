class NotValidNumber(Exception):
    def __init__(self):
        super().__init__("1,2,3 중 하나를 입력하세요")
num = 0

while(True):
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        if(num not in [1,2,3]):
            raise NotValidNumber
    except ValueError:
        print("정수를 입력하세요")
        continue
    except NotValidNumber as E:
        print(E)
        continue
    else:
        break