from tempfile import TemporaryFile
from xlwt import Workbook



book=Workbook()
sheet1=book.add_sheet("EFCC Report")
book.add_sheet("Sheet2")

sheet1.write(0,0,'A1')
sheet1.write(0,1,'B1')

row1=sheet1.row(1)
sheet1.write(0,'A2')
sheet1.col(0).width=1000
book.save('simple.xls')
book.save(TemporaryFile())