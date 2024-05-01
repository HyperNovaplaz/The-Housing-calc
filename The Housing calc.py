import tkinter as tk
from tkinter import ttk, messagebox

class FlatPriceCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flat Price Calculator")
        self.master.geometry("500x700")  # Increased window size
        self.center_window()  # Center the window on the screen
        self.master.resizable(False, False)  # Disable resizing

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TLabel", foreground="black", font=("Helvetica", 12))
        self.style.configure("TEntry", fieldbackground="lightgray", font=("Helvetica", 12))
        self.style.configure("Custom.TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12, "bold"))

        # Entry fields for flat details
        self.label_area = ttk.Label(master, text="Area (in sq. ft.):")
        self.label_area.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_area = ttk.Entry(master, justify="center")
        self.entry_area.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # More entry fields for flat details (bedrooms, bathrooms, condition)
        # ... (omitted for brevity)

        # Entry fields for sale price parameters
        self.label_sale_price = ttk.Label(master, text="Sale Price Parameters:", font=("Helvetica", 14, "bold"))
        self.label_sale_price.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.label_price_sqft = ttk.Label(master, text="Price per sq. ft.:")
        self.label_price_sqft.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_price_sqft = ttk.Entry(master, justify="center")
        self.entry_price_sqft.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        self.label_price_bedroom = ttk.Label(master, text="Price per bedroom:")
        self.label_price_bedroom.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_price_bedroom = ttk.Entry(master, justify="center")
        self.entry_price_bedroom.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        self.label_price_bathroom = ttk.Label(master, text="Price per bathroom:")
        self.label_price_bathroom.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.entry_price_bathroom = ttk.Entry(master, justify="center")
        self.entry_price_bathroom.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

        self.label_price_condition = ttk.Label(master, text="Price per condition point:")
        self.label_price_condition.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.entry_price_condition = ttk.Entry(master, justify="center")
        self.entry_price_condition.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

        # Entry fields for rent parameters
        self.label_rent = ttk.Label(master, text="Rent Parameters:", font=("Helvetica", 14, "bold"))
        self.label_rent.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        self.label_rent_sqft = ttk.Label(master, text="Rent per sq. ft.:")
        self.label_rent_sqft.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.entry_rent_sqft = ttk.Entry(master, justify="center")
        self.entry_rent_sqft.grid(row=10, column=1, padx=10, pady=5, sticky="ew")

        self.label_rent_bedroom = ttk.Label(master, text="Rent per bedroom:")
        self.label_rent_bedroom.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.entry_rent_bedroom = ttk.Entry(master, justify="center")
        self.entry_rent_bedroom.grid(row=11, column=1, padx=10, pady=5, sticky="ew")

        self.label_rent_bathroom = ttk.Label(master, text="Rent per bathroom:")
        self.label_rent_bathroom.grid(row=12, column=0, padx=10, pady=5, sticky="w")
        self.entry_rent_bathroom = ttk.Entry(master, justify="center")
        self.entry_rent_bathroom.grid(row=12, column=1, padx=10, pady=5, sticky="ew")

        self.label_rent_condition = ttk.Label(master, text="Rent per condition point:")
        self.label_rent_condition.grid(row=13, column=0, padx=10, pady=5, sticky="w")
        self.entry_rent_condition = ttk.Entry(master, justify="center")
        self.entry_rent_condition.grid(row=13, column=1, padx=10, pady=5, sticky="ew")

        # Entry fields for loan parameters
        self.label_loan = ttk.Label(master, text="Loan Parameters:", font=("Helvetica", 14, "bold"))
        self.label_loan.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

        self.label_interest_rate = ttk.Label(master, text="Loan Interest Rate (%):")
        self.label_interest_rate.grid(row=15, column=0, padx=10, pady=5, sticky="w")
        self.entry_interest_rate = ttk.Entry(master, justify="center")
        self.entry_interest_rate.grid(row=15, column=1, padx=10, pady=5, sticky="ew")

        self.label_loan_term = ttk.Label(master, text="Loan Term (years):")
        self.label_loan_term.grid(row=16, column=0, padx=10, pady=5, sticky="w")
        self.entry_loan_term = ttk.Entry(master, justify="center")
        self.entry_loan_term.grid(row=16, column=1, padx=10, pady=5, sticky="ew")

        self.label_down_payment = ttk.Label(master, text="Down Payment (%):")
        self.label_down_payment.grid(row=17, column=0, padx=10, pady=5, sticky="w")
        self.entry_down_payment = ttk.Entry(master, justify="center")
        self.entry_down_payment.grid(row=17, column=1, padx=10, pady=5, sticky="ew")

        # Calculate button
        self.btn_calculate = ttk.Button(master, text="Calculate Price", command=self.calculate_price, style="Custom.TButton")
        self.btn_calculate.grid(row=18, column=0, columnspan=2, pady=20, sticky="ew")

        # Progress label
        self.progress_label = ttk.Label(master, text="")
        self.progress_label.grid(row=19, column=0, columnspan=2, pady=10)

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = self.master.winfo_reqwidth()
        window_height = self.master.winfo_reqheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.master.geometry(f"+{x}+{y}")

    def calculate_price(self):
        try:
            # Retrieve flat details
            area = float(self.entry_area.get())
            bedrooms = int(self.entry_bedrooms.get())
            bathrooms = int(self.entry_bathrooms.get())
            condition = int(self.entry_condition.get())

            # Retrieve sale price parameters
            price_sqft = float(self.entry_price_sqft.get())
            price_bedroom = float(self.entry_price_bedroom.get())
            price_bathroom = float(self.entry_price_bathroom.get())
            price_condition = float(self.entry_price_condition.get())

            # Retrieve rent parameters
            rent_sqft = float(self.entry_rent_sqft.get())
            rent_bedroom = float(self.entry_rent_bedroom.get())
            rent_bathroom = float(self.entry_rent_bathroom.get())
            rent_condition = float(self.entry_rent_condition.get())

            # Retrieve loan parameters
            interest_rate = float(self.entry_interest_rate.get())
            loan_term = int(self.entry_loan_term.get())
            down_payment = float(self.entry_down_payment.get())

            # Calculate total sale price
            total_sale_price = (area * price_sqft) + (bedrooms * price_bedroom) + (bathrooms * price_bathroom) + \
                               (condition * price_condition)

            # Calculate total rent price
            total_rent_price = (area * rent_sqft) + (bedrooms * rent_bedroom) + (bathrooms * rent_bathroom) + \
                               (condition * rent_condition)

            # Calculate loan details
            loan_amount = total_sale_price * (1 - (down_payment / 100))
            monthly_payment = self.calculate_monthly_payment(loan_amount, interest_rate, loan_term)

            # Update progress label with results
            self.progress_label.configure(text=f"Sale Price: ${total_sale_price:,.2f}\n"
                                                 f"Rent Price: ${total_rent_price:,.2f}\n"
                                                 f"Loan Amount: ${loan_amount:,.2f}\n"
                                                 f"Monthly Payment: ${monthly_payment:,.2f}",
                                           foreground="green")
        except ValueError:
            self.progress_label.configure(text="Please enter valid numeric values.", foreground="red")

    def calculate_monthly_payment(self, principal, annual_rate, years):
        monthly_rate = (annual_rate / 100) / 12
        months = years * 12
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
        return monthly_payment

def main():
    root = tk.Tk()
    app = FlatPriceCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
