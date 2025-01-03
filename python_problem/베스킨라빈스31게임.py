class NotValidNumber(Exception):
    def __init__(self):
        super().__init__("1,2,3 중 하나를 입력하세요")
num = 0
baskin = 0
status=True

def Input_num(x):
    while(True):
        try:
            x = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if(x not in [1,2,3]):
                raise NotValidNumber
        except ValueError:
            print("정수를 입력하세요")
            continue
        except NotValidNumber as E:
            print(E)
            continue
        else :
            return x
def player_declare(num,baskin,status):
    for i in range(num):
        baskin +=1
        if(status == True):
            print("player:",baskin)
        else:
            print("Computer:",baskin)
        if(baskin == 31):
            return baskin
    return baskin

num = Input_num(num)
player_declare(num,baskin,status)