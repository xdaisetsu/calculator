import numpy as np, time, os
from dll.getch import getch

button_delay = 0.0001
# + 43
# - 45
# * 42
# / 47

inp = []
tk = []
kb = []
hasil = []
n = 0

while True:
    char = getch()
    time.sleep(button_delay)
    try:
        if((ord(char) > 47) and (ord(char) < 58)):
            try:
                temp = str(inp[n])
                temp = temp + char
                inp[n] = int(temp) 
            except:
                inp.append(int(char))

        elif((char == '+') or (char == '-')):
            n += 1
            inp.append(char)
            tk.append(n)
            n += 1

        elif((char == '*') or (char == '/')):
            n += 1
            inp.append(char)
            kb.append(n)
            n += 1

        elif(char == '='):
            os.system('cls' if os.name == 'nt' else 'clear')
            if not kb and not tk:
                print(inp[0],end='',flush=True)
                continue
            
            for i in kb:
                temp = 0
                if(inp[i] == '*'):
                    temp = inp[i-1] * inp[i+1]

                elif(inp[i] == '/'):
                    temp = inp[i-1] / inp[i+1]

                if i > 2:
                    if(inp[i-2] == '-'):
                        hasil.append(temp * -1)
                    else:
                        hasil.append(temp)
                
                else:
                    hasil.append(temp)
                
                try:
                    inp[i-1] = ''
                    inp[i] = ''
                    inp[i+1] = ''
                    if((inp[i+2] == '*') or (inp[i+2] == '/')):
                        inp[i+1] = hasil[-1]
                        hasil[-1] = 0
                except:
                    pass
                #print(inp)
            for j in tk:
                if inp[j]:
                    if(j > 2): #kalau bukan operasi pertama
                        if(inp[i] == '+'):
                            hasil.append(inp[i+1])
                        elif(inp[i] == '-'):
                            hasil.append(inp[i+1] * -1)
                    else:
                        if inp[j+1]:
                            hasil.append(inp[j+1])
                        hasil.append(inp[j-1])
            
            temp = sum(hasil)
            print(temp,end='',flush=True)
            hasil = []
            kb = []
            tk = []
            inp = [temp]
            n = 0
                   
    except:
        continue
    