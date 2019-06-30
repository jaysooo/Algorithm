from datetime import datetime
DIFF_MIN=45
MIN_OF_HOUR=60
def mytimeDelta(dt1):
    hr,mn=[int(n) for n in dt1.split(' ')]

    if mn>=DIFF_MIN:
        mn=mn-DIFF_MIN
    else:
        mn=(60-DIFF_MIN)+mn	
        if hr==0:
            hr=23
        else:
            hr=hr-1
    return "{newhr} {newmn}".format(newhr=hr,newmn=mn)
    
def solution():
    input_dt=input()
    print(mytimeDelta(input_dt))

if __name__=='__main__':
    solution()
