import pyodbc

server='192.168.1.1'
database = 'database_name'
username = ''
password=''
driver= '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT TOP 10 Id,CurrencyId FROM [OTC_prod].[dbo].[CurrencyQuotes]")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
