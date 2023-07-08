import tkinter as tk
from tkinter import ttk

class app():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('450x350')
        self.root.title('Application Settings')
        self.mainframe = tk.Frame(self.root, background='aliceblue')
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        self.text = ttk.Label(self.mainframe, text="Hello, world!", background='aliceblue', font="Bold")
        self.text.grid(row=0, column=0)

        self.text_field = ttk.Entry(self.mainframe,)
        self.text_field.grid(row=1, column=0, pady=10)

        self.text_button = ttk.Button(self.mainframe, text="Set text", command=self.set_text)
        self.text_button.grid(row=1, column=1, pady=10)

        color_options = ['white', 'red', 'green', 'yellow', 'blue', 'black', 'aliceblue']
        self.text_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.text_color_field.grid(row=2, column=0, sticky='NWES', pady=10)

        self.color_button = ttk.Button(self.mainframe, text="Set Color", command=self.set_color)
        self.color_button.grid(row=2, column=1, pady=10, sticky='NWES')

        self.delete_color_button = ttk.Button(self.mainframe, text="Delete Color", command=self.delete_color)
        self.delete_color_button.grid(row=2, column=2, pady=10, sticky='NWES')

        self.delete_text = ttk.Button(self.mainframe, text="Delete Text", command=self.delete)
        self.delete_text.grid(row=1, column=2, pady=10, sticky='NWES')
        
        Font_options = ['medium']
        self.text_font_field = ttk.Combobox(self.mainframe, values=Font_options)
        self.text_font_field.grid(row=4, column=0, sticky='NWES', pady=10)

        self.text_font = ttk.Button(self.mainframe, text="Set Font-text", command=self.set_Font)
        self.text_font.grid(row=4, column=1, pady=10)

        self.reverse_text = ttk.Button(self.mainframe, text='Reverse Text', command=self.reverse)
        self.reverse_text.grid(row=4, column=2, pady=10, sticky='NWES')

        self.root.mainloop()
        return

    def set_text(self):
        self.text.config(text=self.text_field.get())
        self.text_field.delete(0, tk.END)
        self.text_field.focus()
        return
    
    def set_color(self):
        self.text.config(background=self.text_color_field.get())
        self.text_color_field.delete(0, tk.END)
        self.text_color_field.focus()
        return
    
    def reverse(self):
        self.text.config(text=self.text.cget('text')[::-1])
        return
    
    def delete(self):
        self.text.config(text=self.text_color_field.get())
        self.text_color_field.delete(0, tk.END)
        self.text_color_field.focus()
        return
    
    def delete_color(self):
        self.text.config(background=self.text_color_field.get())
        self.text_color_field.delete(0, tk.END)
        self.text_color_field.focus()
        return
    
    def set_Font(self):
        self.text.config(font=self.text_font_field.get())
        self.text_font_field.delete(0, tk.END)
        self.text_font_field.focus()
        return
    
if __name__ == '__main__':
    app()