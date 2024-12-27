start, stop = map(int, input().split())
 
i = start

while True:
    if(i > stop):
        break
    x = str(i);
    if(x[len(x) - 1] == '3') :
        i+=1
        continue;
    print(i, end=' ')
    i += 1

