#Jacob Durgan, Henry Derrick, Jack Perkins

def choices():
    print("Please choose what you would like to do.")
    choice = input("For Signing Up Type 1, For Signing in Type 2, If Forgot Username Type 3, If Forgot Password Or Want To Reset Password Type 4: ")
    if choice == "1":
       return getdetails()
    elif choice == "2":
       return checkdetails()
    elif choice == "3":
       return forgotU()
    elif choice == "4":
       return forgotP()
    else:
       print('Enter a listed option')
       choices()

def getdetails():
    print("Please Provide")
    email = str(input("Email: "))
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    info = f.read()
    if email in info:
        return "Email Unavailable. Please Try Again"
    f.close()
    name = str(input("Name: "))
    password = str(input("Password: "))
    forget = str(input("Favorite Number: "))
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'w')
    info = info + "\n" + email + "\n" + name + "\n" + password + "\n" + forget + "\n"
    f.write(info)
    f.close()
    #f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    #string_list = f.readlines()
    #f.close()
    #print(string_list)
    
def checkdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            print("Welcome Back, " + name)
            manage(name, password)
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."

def forgotU():
   email = str(input("Please Provide Email: "))
   forget = str(input("What Is Your Favorite Number?: "))
   f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
   info = f.read()
   f.close()
   info = info.split() 
   index = info.index(email) + 3
   usr_num = info[index]
   if usr_num == forget and email in info:
      name = str(input("Please Enter A New Username: "))
      f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
      string_list = f.readlines()
      f.close
      with open("/content/drive/Shared drives/Photo_Memory/User_Data.txt") as myFile:
          for num, line in enumerate(myFile, 1):
              if email in line:
                  index1 = num
      string_list[index1] = name + "\n"
      f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'w')
      new_f = "".join(string_list)
      f.write(new_f)
      f.close()
      print("Username Changed!")
   else:
      return "That Is Not this Email's Favorite Number! Please Try Again" 

def forgotP():
   email = str(input("Please Provide Email: "))
   forget = str(input("What Is Your Favorite Number?: "))
   f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
   info = f.read()
   f.close()
   info = info.split() 
   index = info.index(email) + 3
   usr_num = info[index]
   if usr_num == forget and email in info:
     password = str(input("Please Enter A New Password: "))
     f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
     string_list = f.readlines()
     f.close
     with open("/content/drive/Shared drives/Photo_Memory/User_Data.txt") as myFile:
         for num, line in enumerate(myFile, 1):
             if email in line:
                 index1 = num + 1
     string_list[index1] = password + "\n"
     f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'w')
     new_f = "".join(string_list)
     f.write(new_f)
     f.close()
     print("Password Changed!")
   else:
     return "That Is Not this Email's Favorite Number! Please Try Again" 

def manage(name, password):
    name1 = name
    password1 = password
    print("Please choose what you would like to do.")
    choice = input("For Changing Email Type 1, For Changing Username Type 2, For Changing Password Type 3: ")
    if choice == "1":
       return manageE(name1, password1)
    elif choice == "2":
       return manageU(name1, password1)
    elif choice == "3":
       return manageP(name1, password1)
    else:
       print('Enter a listed option')
       manage()

def manageU(name1, password1):
    name = str(input("Please Enter A New Username: "))
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    string_list = f.readlines()
    f.close
    with open("/content/drive/Shared drives/Photo_Memory/User_Data.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if password1 in line:
                index1 = num - 2
    string_list[index1] = name + "\n"
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'w')
    new_f = "".join(string_list)
    f.write(new_f)
    f.close()
    print("Username Changed!")

def manageP(name1, password1):
    password = str(input("Please Enter A New Password: "))
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    string_list = f.readlines()
    f.close
    with open("/content/drive/Shared drives/Photo_Memory/User_Data.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if name1 in line:
                index1 = num
    string_list[index1] = password + "\n"
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'w')
    new_f = "".join(string_list)
    f.write(new_f)
    f.close()
    print("Password Changed!")

def manageE(name1, password1):
    email = str(input("Please Enter A New Email: "))
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'r')
    string_list = f.readlines()
    f.close
    with open("/content/drive/Shared drives/Photo_Memory/User_Data.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if name1 in line:
                index1 = num - 2
    string_list[index1] = email + "\n"
    f = open("/content/drive/Shared drives/Photo_Memory/User_Data.txt",'w')
    new_f = "".join(string_list)
    f.write(new_f)
    f.close()
    print("Email Changed!")

print(choices())
