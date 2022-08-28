
def solution():
    input_time = input().split()
    hour, minute = int(input_time[0]),int(input_time[1])
    oven_runtime = int(input())
    if ( oven_runtime + minute ) >= 60:
        hour += (oven_runtime + minute)//60
        minute = (oven_runtime + minute)%60
    else:
        minute += oven_runtime
        
    if hour >= 24:
        hour-=24
    
    print(f"{hour} {minute}")

    



solution()