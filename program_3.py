# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:
def calculate_sales_tax(total_sales):
    sales_tax_rate = .05
    county_tax_rate = .025

    sales_tax = sales_tax_rate * total_sales
    county_tax = county_tax_rate * total_sales
    total_sales_tax = sales_tax + county_tax


    print(f"Total Sales: ${total_sales:.2f}")
    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"State Sales Tax: ${sales_tax:.2f}")
    print(f"Total Sales Tax: ${total_sales_tax:.2f}")



def main():
    try:
        total_sales = float(input("Enter the total sales for the month: $"))

        calculate_sales_tax(total_sales)
    except ValueError:
        print("Invalid input. Please enter a valid number for the total sales.")

if __name__ == "__main__":
    main()
# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
