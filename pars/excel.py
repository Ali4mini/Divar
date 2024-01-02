import openpyxl
import divar
import time
divar_obj = divar.Divar(headless=True)

wb = openpyxl.load_workbook(filename="test.xlsx")
sheet = wb.active
posts = divar_obj.all_posts("https://divar.ir/marketplace/storeslist/tehran/toolbox")
posts = posts[3:]
x_row = 2
x_column = 1

for post in posts:
    details = divar_obj.post_details(post)

    for detail in details:
        sheet.cell(row = x_row, column = x_column).value = detail
        x_column += 1
    print(details)


    x_column = 1
    x_row += 1






wb.save(filename="test.xlsx")
