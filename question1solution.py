import re

def check_password_strength(password):

    regex = ("^(?=.*[a-z])(?=." + 
             "*[A-Z])(?=.*\\d)" + 
             "(?=.*[-+_!@#$%^&*., ?]).+$")

    p = re.compile(regex)

    reg = False

    if(re.search(p, password)):
        reg = True
    else:
        reg = False

    if(len(password) < 8):
        return False
    elif(reg == False):
        return False
    else:
        return True



if __name__ == '__main__':
    password = input("Enter password:")    
    if check_password_strength(password) :
        print("Password Strength is good")
    else :
        print("Password Strength is not good")




