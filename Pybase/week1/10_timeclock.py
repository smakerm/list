import time


while True:
    f_time = time.localtime()
    p_time = f_time[3:6]
    print('%d:%d:%d\r'%p_time,end = '')
    time.sleep(1)
