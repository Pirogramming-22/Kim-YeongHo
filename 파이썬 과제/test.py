bus_pay = 1350
balance = int(input())

while(balance > 0):
    balance -= bus_pay
    if(balance >= 0):
        print(balance)