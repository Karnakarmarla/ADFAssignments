"""Example for Mysql database connectivity with python """
from datetime import date
from datetime import datetime
import logging
import json
from dateutil import relativedelta
import mysql.connector
class Connection():
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='root',\
                                            host='localhost',database='db1')
        self.mycursor=self.mydb.cursor(buffered=True)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        file_handler = logging.FileHandler('logFile.log', mode='w')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def table_creation(self):
        '''Creating Request_Info and Response_Info tables'''
        self.mycursor.execute("create table if not exists Request_Info(Request_Id int NOT NULL \
                AUTO_INCREMENT,FirstName varchar(50),MiddleName varchar(50),LastName varchar(50),\
                DOB date,Gender varchar(50),Nationality varchar(50),Current_City varchar(50),\
                State varchar(50),Pin_Code int,Qualification varchar(50),Salary int,\
                PAN varchar(50),Request_Date date,primary key(Request_Id))")

        self.mycursor.execute("create table if not exists Response_Info(Response_Id int not null \
                AUTO_INCREMENT,Request_Id int,Response varchar(255),primary key(Response_Id),\
                foreign key(Request_Id) references Request_Info(Request_Id))")
        self.mydb.commit()

class User:
    """User class represents user typical structure"""
    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.dob = None
        self.gender = None
        self.nationality = None
        self.current_city = None
        self.state = None
        self.pin_code = None
        self.qualification = None
        self.salary = None
        self.pan = None
        self.reason =""

    def add_user(self, user_data,con):
        """ Used for adding user data to Request_Info tabe"""
        self.first_name = user_data[0]
        self.middle_name = user_data[1]
        self.last_name = user_data[2]
        self.dob = datetime.strptime(user_data[3],'%Y-%m-%d').date()
        self.gender = user_data[4]
        self.nationality = user_data[5]
        self.current_city = user_data[6]
        self.state = user_data[7]
        self.pin_code = int(user_data[8])
        self.qualification = user_data[9]
        self.salary = int(user_data[10])
        self.pan = user_data[11]

        sql1 = "insert into Request_Info(FirstName,MiddleName,LastName,DOB,Gender,Nationality,\
        Current_City,State,Pin_Code,Qualification,Salary,PAN,Request_Date )\
         values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (self.first_name, self.middle_name, self.last_name, self.dob, self.gender,
                self.nationality,self.current_city,self.state, self.pin_code,
                self.qualification, self.salary, self.pan,datetime.now().date())
        con.mycursor.execute(sql1, data)
        con.mydb.commit()

    def age_eligibility(self,con):
        """Checks for age eligibility"""
        diff = relativedelta.relativedelta(date.today(), self.dob)
        if self.gender.lower() == "male":
            if diff.years <= 21:
                self.reason = "age is less than expected"
        elif self.gender.lower()== "female":
            if diff.years <= 18:
                self.reason = "age is less than expected"
        con.logger.info("age_eligibilty method executed")
    def nationality_eligibility(self,con):
        """Used for vaidating nationality"""
        if self.nationality.lower() not in ['indian', 'american']:
            self.reason = self.reason+", Nationality is not matched"
        con.logger.info("nationality_eligibility method executed")

    def state_eligibility(self,con):
        """Validates state of user"""
        state_list = ['andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chhattisgarh',\
                      'karnataka','madhya-pradesh','odisha', 'tamil-nadu',\
                      'telangana', 'west-bengal']
        if self.state.lower() not in state_list:
            self.reason = self.reason+", State is not matched in the list"
        con.logger.info("state_eligibility method method executed")

    def salary_eligibility(self,con):
        '''Used for checking salary validaton'''
        if self.salary < 10000 or self.salary > 90000:
            self.reason = self.reason+", salary is not matching the range"
        con.logger.info("salary_eligibility method executed")

    def request_eligibility(self,con):
        '''Checks for request received within 5 days'''
        data=(self.pan,)
        print(self.pan)
        sql1="select Request_Date from Request_Info where PAN=%s"
        con.mycursor.execute(sql1,data)
        request_date = con.mycursor.fetchone()
        print(request_date[0])
        diff=relativedelta.relativedelta(date.today(),request_date[0])
        print(diff.days)
        if diff.days <= 5 and diff.days !=0:
            self.reason=self.reason+", Recently request is received within 5 days "
        con.logger.info("request_eligibility method is executed")

    def add_response(self,con):
        ''' Used for adding Json response to Response_Info table'''
        if len(self.reason) == 0:
            response = "Success"
            json_obj = json.dumps({"Request_Id": con.mycursor.lastrowid, "Response": response})
            sql1 = "insert into Response_Info(Request_Id,Response) values(%s,%s)"
            data = (con.mycursor.lastrowid, json_obj)
            con.mycursor.execute(sql1, data)
            con.mydb.commit()
            with open('response.txt', 'a',encoding='utf8') as outfile:
                json.dump({"Request_Id": con.mycursor.lastrowid, "Response": response}, outfile)
                outfile.write('\n')
            con.logger.info("Response is added successfully")
        else:
            response = "Failure"
            json_obj = json.dumps({"Request_Id": con.mycursor.lastrowid, "Response": response,\
                                   "Reason": self.reason})
            sql1 = "insert into Response_Info(Request_Id,Response) values(%s,%s)"
            data = (con.mycursor.lastrowid, json_obj)
            con.mycursor.execute(sql1, data)
            con.mydb.commit()
            with open('response.txt', 'a',encoding='utf8') as outfile:
                json.dump({"Request_Id": con.mycursor.lastrowid, "Response": response,\
                           "Reason": self.reason}, outfile)
                outfile.write('\n')
            con.logger.info("Response is added successfully")



if __name__ == "__main__":
    con=Connection()
    con.table_creation()
    try:
        user_data = list(map(str, input("Enter firstname, middlename, lastname, DOB, gender,\
         Nationality,Current-city,state, pin-code, Qualification, salary, PAN-number: ").split()))
        print(user_data)

        user = User()
        user.add_user(user_data,con)
        user.age_eligibility(con)
        user.nationality_eligibility()
        user.state_eligibility(con)
        user.salary_eligibility(con)
        user.request_eligibility(con)
        user.add_response(con)
    except Exception:
        con.logger.error("Error occured in main")
    finally:
        con.mydb.close()