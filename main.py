import tkinter


def  calculate():
    try:
        user_weight = float(weight_entry.get())
        user_height = float(height_entry.get())
        bmi = user_weight / (user_height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


window = tkinter.Tk()
window.title("BMI")
window.geometry("800x600")
window.config(bg= "light green")

weight_label = tkinter.Label(text= "Please Enter Your Weight")
weight_label.config(font=("Arial",10), bg= "light blue")
weight_label.pack()

weight_entry = tkinter.Entry(width=10)
weight_entry.pack(pady=10)


height_label = tkinter.Label(text= "Please Enter Your Height (in m)")
height_label.config(font=("Arial",10), bg= "light blue")
height_label.pack(pady= 10)

height_entry = tkinter.Entry()
height_entry.pack()



calculate_button = tkinter.Button(text= "Calculate", command= calculate)
calculate_button.pack(pady= 20)


result_label = tkinter.Label(bg="light green")
result_label.pack(pady= 20)

window.mainloop()