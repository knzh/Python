'''
height = "shuru "
height +="\nnihao: "
message=""

while message !="quit":
    message=input(height)
    if message != 'quit':
        print(message)
'''

'''
height = "shuru "
height +="\nnihao: "
message=""
active=True
while active:
    message=input(height)
    if message != 'quit':
        print(message)
        cative = True
    elif message == "quit":
        break
'''

height = "shuru "
height +="\nnihao: "
message=""
active=True
while active:
    message=input(height)
    if message == 'quit':
        
        active = False
    elif message != "quit":
        
        print(message)