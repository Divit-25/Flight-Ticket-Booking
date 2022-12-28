import Admin,User,DB2
while True:
    print("---------------------------------------------------------------------------------")
    print("|                         Welcome to Sky Airlines                               |")
    print("---------------------------------------------------------------------------------")
    print("Log in as:\n1)Admin\n2)User\nNew user or admin..?\n3)User Signup\n4)Admin Signup\n5)Exit")
    inp=int(input())
    if inp==1:
        name,passwd=Admin.getAdminCredentials()
        if DB2.validateAdmin(name,passwd):
            Admin.adminAuth()
        else:
            print("Problem with server.Try again later..!")
    elif inp==2:
        name,passwd=User.getUserDetails()
        if DB2.validateUser(name,passwd):
            User.userAuth(name)
        else:
            print("Problem with server.Try again later..!")
    elif inp==3:
        name,user_id,passwd=User.create_user()
        if DB2.userCreation(name,user_id,passwd):
            print("User created Successfully..!")
        else:
            print("Problem with server.Try again later..!")
    elif inp==4:
        name,passwd=Admin.getAdminCredentials()
        if DB2.adminCreation(name,passwd):
            print("Admin created Successfully..!")
        else:
            print("Problem with server.Try again later..!")
    else:
        break