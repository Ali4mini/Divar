import openpyxl
import divar
import time
divar_obj = divar.Divar(URL="https://divar.ir/s/tehran/buy-apartment/doolab?districts=1017%2C975&user_type=personal")
divar_obj.login("9125992786", "cookies/cookie.pkl")

wb = openpyxl.load_workbook(filename="test.xlsx")
sheet = wb.active
posts = divar_obj.all_posts()
x_row = 2
x_column = 1
for post in posts:
    details = divar_obj.post_details(post)
    for detail in details:
        sheet.cell(row = x_row, column = x_column).value = detail
        x_column += 1
    x_column = 1
    x_row += 1






wb.save(filename="test.xlsx")