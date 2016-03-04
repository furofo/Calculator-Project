__author__ = 'furofo1'

import tkinter

class Calculator:
    def __init__(self):

        window = tkinter.TK()
        window.title("Calculator")

        self.string = tkinter.StringVar()
        entry = tkinter.Entry(window, textvariable = self.string)
        entry.grid(row = 0, column = 0, columnspan = 6)
        entry.focus()
        values = ["7","8", "9", "/", "Clear" , "<",
                  "4", "5", "6", "*", "(",")", "1", "2", "3", "-",
                  "=", "0", ".","%", "+"]
        for txt in values:
            if(txt == "="):
                btn = tkinter.Button(window, height = 2, width = 4, padx = 23, pady = 23, text = txt)
                btn.pack(window)
