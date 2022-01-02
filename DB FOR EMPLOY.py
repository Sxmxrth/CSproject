c import mysql.connector as mysql

def Create_db(db_pass):
    
    db = mysql.connect(host="localhost", user="root", passwd=db_pass)
    c = db.cursor()
    query="CREATE SCHEMA `emp_info` "
    c.execute(query)
    db.commit()
    db.close()

def Create_table(db_pass):
    
    db = mysql.connect(host="localhost", user="root", passwd=db_pass, database="emp_info")
    c = db.cursor()
    query='''CREATE TABLE `emp_info`.`emp_data` (
              `Emp_ID` INT NOT NULL AUTO_INCREMENT,
              `Emp_Name` VARCHAR(45) NULL,
              `Emp_Address` VARCHAR(45) NULL,
              `Emp_Dob` DATE NULL,
              `Emp_Status` VARCHAR(45) NULL,
              `Emp_Salary` INT NULL,
              `Emp_Passwd` VARCHAR(45) NOT NULL,
              `emp_Remark` VARCHAR(45) NULL,
              PRIMARY KEY (`Emp_ID`, `Emp_Passwd`))'''
    
    c.execute(query)
    db.commit()
    db.close()
    
passwd=input("type your  db password= ")

Create_db(passwd)
Create_table(passwd)