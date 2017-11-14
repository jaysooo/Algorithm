
#case 1
sample = [1,5,3,2,3]
#sample = [5,3,1]
stockLog =[]
sellItem = -1 

for i in reversed(sample):

    if sellItem == -1:
        sellItem=i
        continue
    elif sellItem < i:
        sellItem=i
        continue
    elif sellItem > i :
        stockLog.append(sellItem)
        stockLog.append(i)
        sellItem=-1        
        
    #print(sellItem)

if len(stockLog)%2 == 0 :
    print(len(stockLog))


