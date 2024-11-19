import tkinter as  tk

root = tk.Tk()

#Cài đặt window size
root.geometry("300x100")
#Tên title
root.title('Dang Nhap')
#Khai báo
name_var = tk.StringVar()
passwd_var = tk.StringVar()
#Tạo hàm xuất ra màn hình tk và mk in ra màn hình
def submit():
    name = name_var.get()
    password = passwd_var.get()
    print(f"Ten dang nhap la: {name}")
    print(f"Mat khau la: {password}")
#Tạo lable tk, mk
name_lable = tk.Label(root, text= 'Ten dang nhap', font=('TimeNewRoman',10,'bold'))
name_entry = tk.Entry(root, textvariable= name_var, font=('TimeNewRoman',10,'normal'))
passwd_lable = tk.Label(root, text= 'Mat khau', font=('TimeNewRoman',10,'bold'))
passwd_entry = tk.Entry(root, textvariable= passwd_var, font=('TimeNewRoman',10,'normal'))
#Tạo nút xác nhân
sub_btn = tk.Button(root, text='Xac nhan', command= submit)
#Đặt vị trí
name_lable.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passwd_lable.grid(row=1, column=0)
passwd_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
#Hiện thông tin lên màn hình
root.mainloop()