import DB2
def getUserDetails():
    username=input("Enter username:")
    password=input("Enter password:")
    return username,password

def create_user():
    name=input("Enter name:")
    username=input("Enter user id:")
    password=input("Enter password:")
    return name,username,password

def userAuth(username):
    while True:
        print("---------------------------------------------------------------------------------")
        print("|                                User Dashboard                                 |")
        print("---------------------------------------------------------------------------------")
        print("1)Search Flight\n2)Book\n3)View my bookings\n4)Logout")
        choiceInp=int(input())
        if choiceInp==1:
            print("1)Search by date\n2)Search by flight time")
            choice=int(input("Enter your choice:"))
            if choice==1:
                flightDate=input("Enter flight date:")
                DB2.viewByDate(flightDate)
            else:
                flightTime=input("Enter flight time:")
                DB2.viewByTime(flightTime)
        elif choiceInp==2:
            flightNo=int(input("Enter flight number to book:"))
            seats=int(input("Enter the number of seats:"))
            if DB2.bookFlight(username,flightNo,seats):
                print(str(seats)+" seats booked successly..!")
        elif choiceInp==3:
            DB2.viewBookedUsers(username)
        else:
            break