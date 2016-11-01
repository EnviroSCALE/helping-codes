import sqlite3
from xlsxwriter.workbook import Workbook

#All
workbook = Workbook("data.xlsx")
worksheet = workbook.add_worksheet()
sqlite_file = "data.sqlite"

worksheet.write('A1', 'id')
worksheet.write('B1', 'timestamp')
worksheet.write('C1', 'event')
worksheet.write('D1', 'value')
worksheet.write('E1', 'prio_class')
worksheet.write('F1', 'prio_value')
worksheet.write('G1', 'lat')
worksheet.write('H1', 'alt')
worksheet.write('I1', 'lon')
worksheet.write('J1', 'time')

conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
mysel=c.execute("select id, timestamp, event, value, prio_class, prio_value, lat, alt, long, datetime(timestamp,'unixepoch', 'localtime') as time from sensor ")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i+1, j, value)
workbook.close()


def xlsxWriteByEvent(event_name, sqlite_file="data.sqlite"):
    workbook = Workbook("data_" + str(event_name) + ".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'id')
    worksheet.write('B1', 'timestamp')
    worksheet.write('C1', 'event')
    worksheet.write('D1', 'value')
    worksheet.write('E1', 'prio_class')
    worksheet.write('F1', 'prio_value')
    worksheet.write('G1', 'lat')
    worksheet.write('H1', 'alt')
    worksheet.write('I1', 'lon')
    worksheet.write('J1', 'time')

    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    mysel=c.execute("select id, timestamp, event, value, prio_class, prio_value, lat, alt, long, datetime(timestamp,'unixepoch', 'localtime') as time from sensor where event = " + "'" +str(event_name) +"'" )
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value)
    workbook.close()


xlsxWriteByEvent("co2")
xlsxWriteByEvent("humidity")
xlsxWriteByEvent("temperature")
xlsxWriteByEvent("methane")
xlsxWriteByEvent("dust")
xlsxWriteByEvent("lpg")