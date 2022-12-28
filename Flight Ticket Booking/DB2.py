import ibm_db

dbconnection = ibm_db.connect("DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dyh88301;PWD=iSw12q0xL7exo4GO","", "")
if dbconnection :
    print('connected')
else:
    print("failed to connect")

Server = ibm_db.server_info(dbconnection)


    
def userCreation(name, user_id,password):
    statement = "insert into User (name , user_id , password) values ('"+name+"','"+user_id+"','"+password+"');"
    if ibm_db.exec_immediate(dbconnection, statement):
        return True
    else:
        return False

def validateUser(user_id, password):
    statement = ibm_db.exec_immediate(dbconnection, "select password from user where user_id='"+user_id+"';")
    entries = 0
    while ibm_db.fetch_row(statement) != False:
        entries += 1
        value = ibm_db.result(statement, 0)
        print("Password: ", value)
        DBpassword = value
        if DBpassword != password:
            return False
        else:            
            return True

def validateAdmin(username,password):
    statement=ibm_db.exec_immediate(dbconnection,"select password from ADMIN where username='"+username+"';")
    entries = 0
    while ibm_db.fetch_row(statement) != False:
        entries += 1
        value = ibm_db.result(statement, 0)
        DBpassword = value
        if DBpassword != password:
            return False
        else:            
            return True

def adminCreation(username,password):
    statement = "insert into ADMIN (username,password) values ('"+username+"','"+password+"');"
    if ibm_db.exec_immediate(dbconnection, statement):
        return True
    else:
        return False


def addFlightDetails(flight_no,flight_time,flight_date,start,dest):
    statement = "insert into Flight (flight_no,flight_time,flight_date,start,dest) values ('"+str(flight_no)+"','"+flight_time+"','"+flight_date+"','"+start+"','"+dest+"');"
    if ibm_db.exec_immediate(dbconnection,statement):
        return True
    else:
        return False

def viewByDate(date):
    sql= "select * from flight where flight_date='"+date+"';"
    statement=ibm_db.exec_immediate(dbconnection,sql)
    dictionary = ibm_db.fetch_both(statement)
    print("-------------------------------------------------------------------------------------")
    print("| Flight Number | Flight Time | Flight Date |      Start      |      Destination    |")
    print("-------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:13s}|{:13s}|{:17s}|{:21s}|".format( str(dictionary[1]),dictionary[2],dictionary[3],dictionary[4],dictionary[5] )) 
        print("-------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(statement)

def viewByTime(time):
    sql= "select * from flight where flight_time='"+time+"';"
    statement=ibm_db.exec_immediate(dbconnection,sql)
    dictionary = ibm_db.fetch_both(statement)
    print("-------------------------------------------------------------------------------------")
    print("| Flight Number | Flight Time | Flight Date |      Start      |      Destination    |")
    print("-------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:13s}|{:13s}|{:17s}|{:21s}|".format( str(dictionary[1]),dictionary[2],dictionary[3],dictionary[4],dictionary[5] )) 
        print("-------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(statement)


def removeFlight(flight_no):
    statement = "delete from flight where flight_no='"+flight_no+"';"
    if ibm_db.exec_immediate(dbconnection,statement):
        return True
    else:
        return False

def viewBookedUsers(user_id):
    sql= "select * from booking where user_id='"+user_id+"';"
    statement=ibm_db.exec_immediate(dbconnection,sql)
    dictionary = ibm_db.fetch_both(statement)
    print("----------------------------------------------------------------------------------------------------")
    print("| Flight Number | Flight Time | Flight Date |      Start      |      Destination    | Seats Booked |")
    print("----------------------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:13s}|{:13s}|{:17s}|{:21s}|{:15s}".format( str(dictionary[1]),dictionary[2],dictionary[3],dictionary[4],dictionary[5],str(dictionary[6]) )) 
        print("----------------------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(statement)


def bookingByNo(flight_no):
    sql= "select * from booking where flight_no='"+str(flight_no)+"';"
    statement=ibm_db.exec_immediate(dbconnection,sql)
    dictionary = ibm_db.fetch_both(statement)
    while dictionary != False:
        user_id=dictionary[0]
        statement=ibm_db.exec_immediate(dbconnection,"select name from user where user_id='"+user_id+"';")
        dictionary = ibm_db.fetch_both(statement)
        name=dictionary[0]
        print("----------------------------------------------------------------------------")
        print("|     Booked Person Name                     |          No of Seats        |")
        print("----------------------------------------------------------------------------")
        while dictionary != False:
                sql= "select seat from booking where user_id='"+user_id+"';"
                statement=ibm_db.exec_immediate(dbconnection,sql)
                dictionary = ibm_db.fetch_both(statement)
                print("|{:44s}|{:29s}".format(name,str(dictionary[0])))
                print("----------------------------------------------------------------------------")
                dictionary = ibm_db.fetch_both(statement)
        dictionary = ibm_db.fetch_both(statement)

def bookingByTime(flight_time):
    sql="select * from Booking where flight_time='"+flight_time+"';"
    statement=ibm_db.exec_immediate(dbconnection,sql)
    dictionary = ibm_db.fetch_both(statement)
    while dictionary != False:
        user_id=dictionary[0]
        statement=ibm_db.exec_immediate(dbconnection,"select name from user where user_id='"+user_id+"';")
        dictionary = ibm_db.fetch_both(statement)
        name=dictionary[0]
        print("----------------------------------------------------------------------------")
        print("|     Booked Person Name                     |          No of Seats        |")
        print("----------------------------------------------------------------------------")
        while dictionary != False:
                sql= "select seat from booking where user_id='"+user_id+"';"
                statement=ibm_db.exec_immediate(dbconnection,sql)
                dictionary = ibm_db.fetch_both(statement)
                print("|{:44s}|{:29s}".format(name,str(dictionary[0])))
                print("----------------------------------------------------------------------------")
                dictionary = ibm_db.fetch_both(statement)
        dictionary = ibm_db.fetch_both(statement)

def bookFlight(user_id,flight_no,seats):
    sql= "select * from flight where flight_no='"+str(flight_no)+"';"
    statement=ibm_db.exec_immediate(dbconnection,sql)
    dictionary = ibm_db.fetch_both(statement)
    flight_date=""
    flight_time=""
    start=""
    dest=""
    while dictionary != False:
        flight_time=dictionary[1]
        flight_date=dictionary[2]
        start=dictionary[3]
        dest=dictionary[4]
        dictionary = ibm_db.fetch_both(statement)
    statement = "insert into Booking (user_id,flight_no,flight_time,flight_date,start,dest,seat) values ('"+user_id+"','"+str(flight_no)+"','"+flight_time+"','"+flight_date+"','"+start+"','"+dest+"','"+str(seats)+"');"
    if ibm_db.exec_immediate(dbconnection,statement):
        return True
    else:
        return False