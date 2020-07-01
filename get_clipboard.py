import Tkinter as tk
import time

item_list = []

def getClipboardText():

    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    return root.clipboard_get()

def add_item(item):

        for line in item.splitlines():
            if "crafted" in line:
                print line
                item_list.append(line)


old_data = getClipboardText()

while True:

    data = getClipboardText()
    if data != old_data:
    
        add_item(data)
        old_data = data

#        for x in item_list:
#            print x

    time.sleep(0.1)
