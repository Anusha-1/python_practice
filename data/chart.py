#pip install openpyxl 
#like we can automate these and read into a pdf file and send an email everyday


from openpyxl.chart import BarChart,Reference
import openpyxl

wb=openpyxl.Workbook() #creating a new workbook
sheet=wb.active #we are referring active sheet(sheet1)

for i in range(10):  # for now we are dynamically creating , but in real time from api calls / db we get data
    sheet.append([i])  #always has to give [] else it wont be a list.

values=Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)
chart=BarChart()
chart.add_data(values)
chart.title='BOA profits chart'
chart.x_axis.title='X_Axis'
chart.y_axis.title='Y_Axis'
sheet.add_chart(chart,'E2')
wb.save('barchart.xlsx')
print('barchart created......')


#if we do schedule this and send the charts everyday to business. 