import pyodbc

server='192.168.1.1'
database = 'OTC_prod'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect(DRIVER='{ODBC Driver 17 for SQL Server}',SERVER='194.247.132.146',PORT=1443, DATABASE='OTC_prod', trusted_connection='yes')
cursor = cnxn.cursor()

cursor.execute("SELECT TOP 5 InstrumentId as 'Тикер', convert(decimal(10,2),round(StandardPrice,2)) as 'Цена',convert(decimal(50),Quantity) as 'Объем' , CASE WHEN direction=1 THEN 'Покупка' WHEN direction=-1 THEN 'Продажа' END as 'Тип' FROM OTC_prod..Quotes as q (nolock) join OTC_prod..QuoteRevisions as qr (nolock) on q.CurrentRevisionId=qr.Id join OTC_prod..Instruments as i (nolock) on i.Id=q.InstrumentId WHERE convert(date, qr.CreationTime) < GETDATE() AND qr.State = 'Active' AND q.PartyId not like 'TECH%' AND i.InstrumentClassId = 'Stocks' AND qr.StandardPrice*qr.Quantity > 2000 ORDER BY qr.CreationTime DESC")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1])+ " "+str(row[2])+ " " + str(row[3]))
    row = cursor.fetchone()
