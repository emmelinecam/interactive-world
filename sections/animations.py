import time

animation = '|/-\\'

def animations(repeats):
    count = 0
    while count < repeats:
        index = count % len(animation)
        print(animation[index], end = '\r')
        count = count + 1
        time.sleep(0.1)
