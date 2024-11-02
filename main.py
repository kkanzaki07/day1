import customtkinter as ctk

def click() -> None:
    label.configure(text="Hello World!")
    print("Hello World!")

root = ctk.CTk()
root.geometry('300x150')
root.title("Day 1")

button = ctk.CTkButton(master=root, text="Click Me!", command=click)
button.pack(pady=20)

label = ctk.CTkLabel(master=root, text="")
label.pack()

root.mainloop()