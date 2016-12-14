import xlrd
import MySQLdb

book = xlrd.open_workbook("/home/jain/counselling.xls")
sheet = book.sheet_by_index(0)

database = MySQLdb.connect(host="localhost", user="root", passwd="root", db="iethostel")

cursor = database.cursor()

query = """INSERT INTO counselling (srno, rollno, name, percentage, choice1, choice2, choice3, choice4, branch) VALUES (%s, %s, %s, %s, %s, %s, %s, %s , %s)"""

for r in range(1, sheet.nrows):
    srno = sheet.cell(r, 0).value
    rollno = sheet.cell(r, 1).value
    name = sheet.cell(r, 2).value
    percentage = sheet.cell(r, 4).value
    choice1 = sheet.cell(r, 5).value
    choice2 = sheet.cell(r, 6).value
    choice3 = sheet.cell(r, 7).value
    choice4 = sheet.cell(r, 8).value
    branch=sheet.cell(r,3).value
    value = (srno, rollno, name, percentage, choice1, choice2, choice3, choice4, branch)
    print value
    cursor.execute(query, value)
cursor.close()
database.commit()
database.close()
