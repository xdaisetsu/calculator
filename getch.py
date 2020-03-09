import sys, termios, tty, os
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    
    if( ((ord(ch) > 47) and (ord(ch) < 58)) or (ch == '+') or (ch == '-') or (ch == '/') or (ch == '*') ):
        print(ch, sep=' ', end='', flush=True)
        return ch
    
    elif ((ch == '=') or (ch == 'c')):
        return ch
    
    elif(ch == 'p'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thanks for using my services!")
        return exit(0)