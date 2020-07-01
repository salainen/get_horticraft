import Tkinter as tk
import time
import sys
from collections import Counter

item_list = []

final_items = []

def getClipboardText():

    ''' Get clipboard content
    
    '''

    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    return root.clipboard_get()

def exit_routine():

    ''' Go through the list and print counts
    
    go through the list of crafting options, and
    print them with counts
    '''

    final_list = Counter(item_list)

    for key, value in final_list.items():
        final_items.append(str(value) + "x " + str(key))
        print str(value) + "x " + str(key)

    with open('output.txt', 'w') as f:
        for y in final_items:
            f.write(y + "\n")

    sys.exit()

def add_item(item):

        ''' fill the list
        
        Keep adding items to the list until user copies
        a Quicksilver flask, at which point the exit_routine
        is called

        '''
        for line in item.splitlines():
            if "crafted" in line:
                item_list.append(line)
            if "Quicksilver" in line:
                exit_routine()

# get the current clipboard content, to make sure it's 
# ignored in the collection phase.
old_data = getClipboardText()

# main routine:
while True:

    data = getClipboardText()
    if data != old_data:
    
        add_item(data)
        old_data = data

    time.sleep(0.1)