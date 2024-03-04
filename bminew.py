import tkinter as tk
from tkinter import messagebox

class BMI_Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.configure(bg="#F0F0F0")  # Set background color

        self.label_weight = tk.Label(self, text="Weight (kg):", font=("Arial", 14), bg="#F0F0F0")
        self.label_weight.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_weight = tk.Entry(self, font=("Arial", 14))
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)

        self.label_height = tk.Label(self, text="Height (m):", font=("Arial", 14), bg="#F0F0F0")
        self.label_height.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_height = tk.Entry(self, font=("Arial", 14))
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)

        self.button_calculate = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.label_result = tk.Label(self, text="", font=("Arial", 16, "bold"), bg="#F0F0F0")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            result = f"BMI: {bmi:.2f} ({category})"
            self.label_result.config(text=result)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

if __name__ == "__main__":
    app = BMI_Calculator()
    app.mainloop()
