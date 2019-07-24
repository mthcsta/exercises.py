#--coding:utf8;--
#qpy:3
#qpy:console
# imports

import random, os, time

player1 = 'X'
player2 = 'Z'

# funções
def box(l):
    return("[" + str(body[l]) + "]")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def view(turn=1):
    clear()
    print(
    	'::: Tic-tac-toe :::' + "\n" +
    	box(0) + box(1) + box(2) + "\n" + 
     box(3) + box(4) + box(5) + "\n" + 
     box(6) + box(7) + box(8)
    )
    print('_'*15)
    if not turn:
        print('status: Wait...')
    elif turn == 'end':
        print('status: End')
    
def botPlay():
    values = filter(lambda x: isinstance(x, int), body)
    value = random.choice(list(values)) - 1
    body[value] = player2
def check(user=1): # 1 = X / 0 = Z    
    user = {True: player1, False: player2} [ user == 1 ]
    marks = list(map(lambda x: 1 if body[x] == user else 0, range(9)))    
    win = False 
    ix = 0   
    for i in range(3):
        if(
        	marks[ix] and marks[ix+1] and marks[ix+2]
        	or
        	marks[i] and marks[i+3] and marks[i+6]
        	or
        	i==0 and marks[i] and marks[i+4] and marks[i+8]
        	or
        	i==2 and marks[i] and marks[i+2] and marks[i+4]
        	):
            win = True  
        ix = ix + 3
    if(win==False and len(list(filter(lambda x: not isinstance(x, int), body)))==9):
        return 'draw'
        
    return win
    
def end(user=1):
    if user:
        message = 'You Win!'
    else:
        message = 'You Lose!'
    
    print('\n','-'*10,message,'-'*10,'\n')
def draw():
    print('\n','-'*10,'D R A W','-'*10,'\n')



# variáveis
body = list([1,2,3,4,5,6,7,8,9])

# game
view()
while True:
    output = input('Type where you want to mark...\n')
    error = None
    try:
        output = int(output) - 1
        if not (output>=0 and output <9):
            raise ValueError
        if not (isinstance(body[output], int)):
            raise ValueError
        
    except ValueError:
        error = ' × Please enter a valid number.'
    
    if(error):
        print(error)
        time.sleep(1)
    else:        
        body[output] = player1
       
        view(0)
        if check():
            view('end')
            if(check()=='draw'):
                draw()
            else:
                end()
            break
        time.sleep(1)
        botPlay()
        view()
        if check(0):
            view('end')
            if(check(0)=='draw'):
                draw()
            else:
                end(0)
            break
      
    view()
