from random import randint

""" 예외처리 """
class NotValidNumber(Exception):
    def __init__(self):
        super().__init__("1과 3사이의 정수가 아닙니다.")
""" num입력 """
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
""" num을 받고 그걸 통해 출력 """
def player_declare(num,baskin,status):
    for i in range(num):
        baskin +=1
        if(status == True):
            print("PlayerA:",baskin)
        else:
            print("PlayerB:",baskin)
        if(baskin == 31):
            return baskin
    return baskin

""" 게임 전체 코드 """

num = 0
baskin = 0
status = True

while(baskin <31):
    if(status == True): #플레이어 1의 차례
        num = Input_num(num)
        baskin = player_declare(num,baskin,status)
        status = not status
    else: #플레이어 2의 차례
        num = Input_num(num)
        baskin = player_declare(num,baskin,status)
        status = not status
    
if(status == False):
    print("PlayerB win!")
else:
    print("PlayerA win!")

