cnt, max = map(int, input().split(" "))

resultList = []
for i in range(cnt):
    inputList = list(map(int,input().split(" ")))
    resultList.append(inputList)

cnt = 1
result = ''
for i in range(len(resultList)):
    flg = True
    for j in range(len(resultList)):
        #print(resultList[j][i])
        if(resultList[j][i] >= max):
            flg = False
            break
    if(flg):
        if(result == ''):
            result += str(cnt)
        else:
            result += ' ' + str(cnt)

    cnt = cnt + 1

if(result == ''):
    print('wait')
else:
    print(result)

