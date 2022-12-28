import DB2
def getAdminCredentials():
    username=input("Enter username:")
    password=input("Enter password:")
    return username,password
def adminAuth():
    while True:
        print("---------------------------------------------------------------------------------")
        print("|                                Admin Dashboard                                |")
        print("---------------------------------------------------------------------------------")
        print("1)Add Flights\n2)Remove flights\n3)View bookings\n4)Exit")
        inp=int(input())
        if inp==1:
            no=int(input("Enter flight number(Unique):"))
            time=input("Enter time of departure:")
            date=input("Enter date of departure:")
            start=input("Enter starting place:")
            dest=input("Enter destination to reach:")
            if DB2.addFlightDetails(no,time,date,start,dest):
                print("Flight added successfully")
            else:
                print("Problem with server.Try again later..!")
            print("---------------------------------------------------------------------------------")
        elif inp==2:
            no=int(input("Enter flight number(Unique):"))
            if DB2.removeFlight(no):
                print("Flight deleted successfully")
            else:
                print("Problem with server.Try again later..!")
            print("---------------------------------------------------------------------------------")
        elif inp==3:
            print("1)Search booking by flight number\n2)Search booking by flight time")
            choice=int(input("Enter your choice:"))
            if choice==1:
                no=int(input("Enter flight number(Unique):"))
                DB2.bookingByNo(no)
            else:
                time=input("Enter time:")
                DB2.bookingByTime(time)
        else:
            break