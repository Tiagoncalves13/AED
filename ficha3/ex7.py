import random

def generatePassword(userName):
    password = ''
    
    for i in range(len(userName)):
        if i % 2 == 0:  
            password += userName[i]
            password += str(random.randint(1, 9))
    
    password += str(len(userName))
    
    return password

userName = input("Digite o username: ")

resultado = generatePassword(userName)
print(resultado)
