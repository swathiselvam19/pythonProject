import openpyxl

book = openpyxl.load_workbook("C:\\Users\Admin\OneDrive\Desktop\Pythondata.pyxl")
sheet = book.active

cell = sheet.cell(row=2,column=4)
print(cell.value)