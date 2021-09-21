import time

#COUNT DOWN TIMER======================================
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    #print('-- START --')

# BREATH SEQUENCE========================================
def breath():
    n = int(input('\n MINUTE: '))  ;  j = 0
    print('\n STARTING IN: ')
    countdown(int(5))
    print('\n')

    for i in range(0, n):
        sec = n*60
        while j <= (sec-5):
            j = j+5  #;  print(j)
            rem = j % 2  #;  print('rem ',rem)
            if rem != 0:
                print(' > > > INHALE < < <\n')
                countdown(int(5))#time.sleep(4.9)
            else:
                print(' < < < EXHALE > > >\n')
                countdown(int(5))#time.sleep(4.9)

    print('\n-- COMPLETED --')

#======================================================
breath()
input('\n PRESS ENTER TO EXIT')