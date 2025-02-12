def get_price(item, company, ram, price_dict):
    """Returns the price of the selected item based on company and RAM."""
    return price_dict.get(company, {}).get(ram, "Price not available")

def select_ram(options):
    """Handles RAM selection from available options."""
    print("Available RAM options:", ", ".join(options))
    while True:
        ram = input("Enter your choice: ")
        if ram in options:
            return ram
        print("Invalid choice, please select a valid RAM option.")

def select_company(options):
    """Handles company selection from available options."""
    print("Available companies:", ", ".join(options))
    while True:
        company = input("Enter your choice: ")
        if company in options:
            return company
        print("Invalid choice, please select a valid company.")

def handle_computer():
    """Handles computer selection."""
    companies = {"hp": {"4GB": 25000, "8GB": 35000, "12GB": 38000},
                 "dell": {"4GB": 50000, "8GB": 48000, "12GB": 56000},
                 "accer": {"4GB": 80000, "8GB": 85000, "12GB": 90000}}
    
    company = select_company(companies.keys())
    ram = select_ram(companies[company].keys())
    price = get_price("computer", company, ram, companies)
    
    print(f"For your required computer of {company} with {ram} RAM, the price is {price} Rs.")

def handle_laptop():
    """Handles laptop selection."""
    companies = {"apple": {"16GB": 42000, "32GB": 55000, "64GB": 60000},
                 "thinkpad": {"16GB": 42000, "32GB": 47000, "64GB": 47900},
                 "dell": {"16GB": 56000, "32GB": 58600, "64GB": 51000}}
    
    company = select_company(companies.keys())
    ram = select_ram(companies[company].keys())
    price = get_price("laptop", company, ram, companies)
    
    print(f"For your required laptop of {company} with {ram} RAM, the price is {price} Rs.")

def handle_mobile():
    """Handles mobile selection."""
    companies = {"iphone": {"32GB": 60000, "64GB": 70000, "128GB": 75000},
                 "infinix": {"32GB": 25000, "64GB": 30000, "128GB": 35000},
                 "samsung": {"32GB": 52500, "64GB": 70000, "128GB": 95000}}
    
    company = select_company(companies.keys())
    ram = select_ram(companies[company].keys())
    price = get_price("mobile", company, ram, companies)
    
    print(f"For your required mobile of {company} with {ram} RAM, the price is {price} Rs.")

def main():
    """Main function to handle user input and display options."""
    while True:
        item = input("What do you want to buy? (computer/laptop/mobile/exit): ").strip().lower()
        
        if item == "computer":
            handle_computer()
        elif item == "laptop":
            handle_laptop()
        elif item == "mobile":
            handle_mobile()
        elif item == "exit":
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice, please select a valid item.")

if __name__ == "__main__":
    main()