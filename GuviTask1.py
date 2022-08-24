def Register():
  import re
  text1 = input('Create Email id:')
  format = re.compile(('[a-zA-z0-9\_]+@+[a-zA-z]+\.+[a-zA-z]+'))
  Emid = format.findall(text1)
  
  text2 = input('Create password:')
  format2 = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$')
  paswd = format2.findall(text2)

  if Emid and paswd:
    print('Email and password are valid')
    f = open('TASK1.txt','a')
    f.write(text1+','+text2+'\n')

    f.close()
  elif Emid and not paswd:
    print('Pass invalid')
  elif not Emid and paswd:
    print('Emaild invalid')
  elif not Emid and not paswd:
    print('Emaild and passwd invalid')
    Register()
def login():
  read = open('TASK1.txt','r')

  mail = input('Enter Email id:')
  passw = input('Enter password:')
  d = []
  f = []
  for i in read:
    a,b = i.split(',')
    b = b.strip()
    d.append(a)
    f.append(b)


  if mail in d and passw in f:
    print('Login Success')
  else:
    if mail in d and passw not in f:
      print('incorret password')
      choice = input('Forgot pas/Retry')
      if choice == 'Retry':
        login()
      elif choice == 'Forgot pas':
        pos = d.index(mail)
        print(f[pos])

        
    elif mail not in d and passw in f:
      print('incorrect Email id,If you dont have a account please -Register-')
      Register()
    elif mail not in d and passw not in f:
      print('Incorrect Email and password,If you dont have a account please -Register-')
      Register()

def home(option=None):
  option = input('Login/Signup')

  if option == 'Login':
    login()
  elif option == 'Signup':
    Register()
  else:
    print('please enter a valid option')
home()