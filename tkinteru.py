import tkinter

# Create the main window
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# 1. Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text="New Text")

# 4. Input (Entry)
user_input = tkinter.Entry()
user_input.pack()

# 2. Button Function
def button_clicked():
    print("i got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)

# 3. Button
button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

# Start the application loop
window.mainloop()
