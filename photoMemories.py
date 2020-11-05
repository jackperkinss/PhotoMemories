#Jacob Durgan, Henry Derrick, Jack Perkins


def getdetails(email, name, password, forget):
    f = open("/home/JDURG001/mysite/User_Data.txt",'r')
    info = f.read()
    if email in info:
        return "Email Unavailable. Please Try Again"
    f.close()
    f = open("/home/JDURG001/mysite/User_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("/home/JDURG001/mysite/User_Data.txt",'w')
    info = info + "\n" + email + "\n" + name + "\n" + password + "\n" + forget + "\n"
    f.write(info)
    f.close()

def checkdetails(username, password):
    f = open("/home/JDURG001/mysite/User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        usr_password = info[index]
        if usr_password == password:
            return 1


def forgetP(email, forget, password):
   f = open("/home/JDURG001/mysite/User_Data.txt",'r')
   info = f.read()
   f.close()
   info = info.split()
   index = info.index(email) + 3
   usr_num = info[index]
   if usr_num == forget and email in info:
     f = open("/home/JDURG001/mysite/User_Data.txt",'r')
     string_list = f.readlines()
     f.close
     with open("/home/JDURG001/mysite/User_Data.txt") as myFile:
         for num, line in enumerate(myFile, 1):
             if email in line:
                 index1 = num + 1
     string_list[index1] = password + "\n"
     f = open("/home/JDURG001/mysite/User_Data.txt",'w')
     new_f = "".join(string_list)
     f.write(new_f)
     f.close()
     print("Password Changed!")
   else:
     return "That Is Not this Email's Favorite Number! Please Try Again"

def manage(username, password):
    name1 = username
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

def manageU(name, password1):

    f = open("/home/JDURG001/mysite/User_Data.txt",'r')
    string_list = f.readlines()
    f.close
    with open("/home/JDURG001/mysite/User_Data.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if password1 in line:
                index1 = num - 2
    string_list[index1] = name + "\n"
    f = open("/home/JDURG001/mysite/User_Data.txt",'w')
    new_f = "".join(string_list)
    f.write(new_f)
    f.close()

def manageP(username1, password):
    f = open("/home/JDURG001/mysite/User_Data.txt",'r')
    string_list = f.readlines()
    f.close
    with open("/home/JDURG001/mysite/User_Data.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if username1 in line:
                index1 = num - 1
    string_list[index1] = password + "\n"
    f = open("/home/JDURG001/mysite/User_Data.txt",'w')
    new_f = "".join(string_list)
    f.write(new_f)
    f.close()

def manageE(username1, email):
    f = open("/home/JDURG001/mysite/User_Data.txt",'r')
    string_list = f.readlines()
    f.close
    with open("/home/JDURG001/mysite/User_Data.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if username1 in line:
                index1 = num - 3
    string_list[index1] = email + "\n"
    f = open("/home/JDURG001/mysite/User_Data.txt",'w')
    new_f = "".join(string_list)
    f.write(new_f)
    f.close()
