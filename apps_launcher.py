import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []
folders = []
orders = []

root = tk.Tk()
root.title(" Apps Launcher")


canvas = tk.Canvas(root, height=600, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.03)

frame2 = tk.Frame(root, bg="pink")
frame2.place(relwidth=0.5, relheight=0.11, relx=0, rely=0.89)

frame3 = tk.Frame(root, bg="pink")
frame3.place(relwidth=0.5, relheight=0.11, relx=0.5, rely=0.89)



def addFolder():
    foldername = tk.filedialog.askdirectory()
    if foldername != '':
        folders.append(foldername)
        labelApps(nameExtractor(folders[len(folders)-1]))

    print("folders: ", folders)


def check_save():
    if os.path.isfile('save.txt'):
        with open('save.txt', 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            if tempApps[0] == '':
                tempApps.pop()
            orders.extend(tempApps)
            for order in orders:
                labelApps(nameExtractor(order))
            print('orders: ', orders)


def labelApps(app):
    label = tk.Label(frame, text=app, bg="gray")
    label.pack()


def nameExtractor(file):
    temp = []
    li = list(file)
    try:
        targetindex = li.index(".")-1
        for i in range(targetindex, 0, -1):
            if li[i] == "/":
                break
            else:
                temp.append(li[i])
        return "".join(temp[::-1])
    except:
        li = li[::-1]
        for l in li:
            if l == "/":
                break
            else:
                temp.append(l)
        return "".join(temp[::-1])


def clearlist():
    apps.clear()
    folders.clear()
    orders.clear()
    print("orders: ", orders)

    for widget in frame.winfo_children():
        widget.destroy()


def startApps():
    orders.extend(apps)
    orders.extend(folders)
    print("orders: ", orders)
    for item in orders:
        os.startfile(item)


def addApp():
    filename = filedialog.askopenfilename(initialdir="Desktop",  title="Selet File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    if filename != '':
        apps.append(filename)

        labelApps(nameExtractor(apps[len(apps)-1]))

    print("apps: ", apps)


openFile = tk.Button(frame2, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42", command=addApp)
openFile.pack()

openFolder = tk.Button(frame2, text="Open Folder", padx=10, pady=5,
                       fg="white", bg="#263D42", command=addFolder)
openFolder.pack()

runApps = tk.Button(frame3, text="Run Apps", padx=10, pady=5,
                    fg="white", bg="#263D42", command=startApps)
runApps.pack()

Clear = tk.Button(frame3, text="Clear", padx=10, pady=5,
                  fg="white", bg="red", command=clearlist)
Clear.pack()


check_save()
root.mainloop()


with open('save.txt', 'w') as f:
    le = len(orders)
    print("orders: ", orders)
    for i in range(le):
        if i != le-1:
            f.write(orders[i] + ',')
        else:
            f.write(orders[i])
