from tkinter import *

import random
import time


'''
Hello, I am S.M.ABRAR MUSTAKIM TAKI, FROM BRACU
I hope you will like my personal sorting visualizer project
Thank You

'''


root = Tk()
root.title("My Personal Sorting Visualizer😁!")
root.config(bg="#F33015")


data = []


def drawData(data):
    canvas.delete('all')
    c_height = 600
    c_width = 1200
    x_width = c_width/(len(data)+1)
    offset = 30
    #normalizedData = [i / max(data)for i in data]

    for i, height in enumerate(data):
        x0 = i*x_width+offset+10
        y0 = c_height - height * 0.6
        x1 = (i+1)*x_width+offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="#BB2CD9")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def bubble_sort():
    global data

    i = 0
    while i < len(data):
        j = 0
        while j < len(data)-i-1:
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                drawData(data)
                time.sleep(0.000000001)

            j += 1
        i += 1


def selection_sort():
    global data
    a = len(data)
    i = 0
    while i < a-1:
        index_min = i
        j = i+1
        while j < len(data):
            if data[index_min] > data[j]:
                index_min = j
            j += 1

        temp = data[i]
        data[i] = data[index_min]
        data[index_min] = temp
        drawData(data)
        time.sleep(0.000000001)

        i += 1


def generate():
    global data
    minvalue = int(min.get())
    maxvalue = int(max.get())
    size = int(size_number.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minvalue, maxvalue+1))
    drawData(data)


Ui = Frame(root, width=1330, height=200, bg='#FF003A')
Ui.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=1330, height=600, bg='#03F7FA')
canvas.grid(row=1, column=0, padx=10, pady=5)

Button(Ui, text="Selection Sort", command=selection_sort,
       bg="#E8182B").grid(row=0, column=4, padx=5, pady=5)
Button(Ui, text="Bubble Sort", command=bubble_sort,
       bg="#E8182B").grid(row=0, column=3, padx=5, pady=5)

Label(Ui, text="Size: ", bg="#FF003A").grid(
    row=1, column=0, padx=5, pady=5, sticky=W)


size_number = Entry(Ui)
size_number.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Label(Ui, text="Min Value: ", bg="#FF003A").grid(
    row=1, column=2, padx=5, pady=5, sticky=W)
min = Entry(Ui)
min.grid(row=1, column=3, padx=5, pady=5, sticky=W)


Label(Ui, text="Max Value: ", bg="#FF003A").grid(
    row=1, column=4, padx=5, pady=5, sticky=W)
max = Entry(Ui)
max.grid(row=1, column=5, padx=5, pady=5, sticky=W)


Button(Ui, text="generate", command=generate, bg="#E8182B").grid(
    row=0, column=2, padx=5, pady=5)

root.mainloop()
