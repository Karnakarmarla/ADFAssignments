import pytest
from userdata_insertion import *
from userdata_insertion import User
con=Connection()
user = User()

def test_connection_db():
    assert con.mydb

def test_logger_creation():
    assert con.logger !=None

def test_table_creation():
    con.table_creation()
    con.mycursor.execute("select count(*) from Request_Info")
    assert con.mycursor.fetchall()[0][0]==73

def test_add_user():
    list=['Vinay', 'VV', 'RJMN', '1996-05-17', 'Male', 'Indian', 'Hyd', 'Telangana', '74125', 'nbg', '78451', 'po45nvv']
    user.add_user(list,con)
    con.mycursor.execute("select * from Request_Info where PAN='po45nvv'")
    sql_out=tuple(con.mycursor.fetchone())
    assert sql_out

def test_age_eligibility():
    user.dob=datetime.strptime('2000-01-01','%Y-%m-%d').date()
    user.gender='male'
    user.age_eligibility(con)
    assert user.reason == "age is less than expected"

def test_nationality_eligibility():
    user.nationality="Japanese"
    user.nationality_eligibility(con)
    assert user.reason.find("Nationality is not matched")!=-1

def test_state_eligibility():
    user.state="assam"
    user.state_eligibility(con)
    assert user.reason.find("State is not matched in the list")==-1

def test_salary_eligibility():
    user.salary=965412
    user.salary_eligibility(con)
    assert user.salary>90000

def test_request_eligibilty():
    user.pan='trq546dzx'
    user.request_eligibility(con)
    assert user.reason.find("Recently request is received")==-1

def test_add_response():
    con.mycursor.execute("select count(*) from Response_Info where Request_Id=%s", (con.mycursor.lastrowid,))
    if len(user.reason)==0:
        assert con.mycursor.fetchall()[0][0]>=1
    else:
        assert con.mycursor.fetchall()[0][0]==0







