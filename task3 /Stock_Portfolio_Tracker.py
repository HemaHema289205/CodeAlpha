import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_message(message, is_error=False):
    """Displays a message to the user."""
    if is_error:
        print(f"\nERROR: {message}\n")
    else:
        print(f"\n{message}\n")

def get_stock_prices():
    """
    Returns a hardcoded dictionary of stock prices.
    This can be extended with more stocks.
    """
    return {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOG": 150.00,
        "MSFT": 420.00,
        "AMZN": 190.00,
        "NVDA": 1000.00,
        "META": 500.00,
        "NFLX": 650.00,
        "SMCI": 800.00,
        "AMD": 160.00
    }

def add_stock_to_portfolio(portfolio, available_prices):
    """
    Prompts the user for stock symbol and quantity,
    then adds or updates the stock in the portfolio.
    """
    while True:
        stock_symbol = input("Enter stock symbol (e.g., AAPL, type 'back' to return): ").strip().upper()
        if stock_symbol == 'BACK':
            return
        if not stock_symbol:
            display_message("Stock symbol cannot be empty.", True)
            continue

        if stock_symbol not in available_prices:
            display_message(f"Stock symbol '{stock_symbol}' not found in our price list. Available: {', '.join(available_prices.keys())}", True)
            continue

        while True:
            try:
                quantity_str = input(f"Enter quantity for {stock_symbol} (type 'back' to return): ").strip()
                if quantity_str.lower() == 'back':
                    break # Go back to stock symbol input
                quantity = int(quantity_str)
                if quantity <= 0:
                    display_message("Quantity must be a positive number.", True)
                else:
                    break
            except ValueError:
                display_message("Invalid quantity. Please enter a whole number.", True)

        if quantity_str.lower() == 'back':
            continue # Continue the outer loop to re-enter stock symbol

        # Add or update stock in portfolio
        portfolio[stock_symbol] = portfolio.get(stock_symbol, 0) + quantity
        display_message(f"Added {quantity} shares of {stock_symbol} to your portfolio.")
        break # Exit the loop after successful addition

def calculate_total_investment(portfolio, stock_prices):
    """
    Calculates the total investment value of the portfolio.
    """
    total_value = 0.0
    for symbol, quantity in portfolio.items():
        price = stock_prices.get(symbol, 0) # Use .get() to avoid KeyError if symbol not found (though it should be)
        total_value += quantity * price
    return total_value

def display_portfolio(portfolio, stock_prices):
    """
    Displays the current stocks in the portfolio and their total value.
    """
    clear_screen()
    print("\n--- Your Current Portfolio ---")
    if not portfolio:
        print("No stocks in your portfolio yet.")
    else:
        print(f"{'Symbol':<10} {'Quantity':<10} {'Price/Share':<15} {'Total Value':<15}")
        print("-" * 50)
        for symbol, quantity in portfolio.items():
            price = stock_prices.get(symbol, 0)
            value = quantity * price
            print(f"{symbol:<10} {quantity:<10} ${price:<13.2f} ${value:<13.2f}")
        print("-" * 50)
        total_investment = calculate_total_investment(portfolio, stock_prices)
        print(f"{'Total Investment:':<35} ${total_investment:.2f}")
    print("----------------------------\n")
    input("Press Enter to continue...") # Pause for user to read

def save_portfolio_to_file(portfolio, stock_prices):
    """
    Saves the portfolio data to a .txt or .csv file.
    """
    if not portfolio:
        display_message("Your portfolio is empty. Nothing to save.", True)
        return

    while True:
        file_type = input("Save as (txt/csv, type 'back' to return): ").strip().lower()
        if file_type == 'back':
            return
        if file_type not in ['txt', 'csv']:
            display_message("Invalid file type. Please choose 'txt' or 'csv'.", True)
            continue

        filename = f"stock_portfolio.{file_type}"
        try:
            if file_type == 'txt':
                with open(filename, 'w') as f:
                    f.write("Stock Portfolio Report\n\n")
                    f.write("--------------------------------------\n")
                    for symbol, quantity in portfolio.items():
                        price = stock_prices.get(symbol, 0)
                        value = quantity * price
                        f.write(f"Stock: {symbol}\n")
                        f.write(f"Quantity: {quantity}\n")
                        f.write(f"Price per Share: ${price:.2f}\n")
                        f.write(f"Total Value for {symbol}: ${value:.2f}\n")
                        f.write("--------------------------------------\n")
                    total_investment = calculate_total_investment(portfolio, stock_prices)
                    f.write(f"\nTotal Portfolio Investment: ${total_investment:.2f}\n")
                display_message(f"Portfolio saved to {filename} successfully!")
            elif file_type == 'csv':
                with open(filename, 'w') as f:
                    f.write("Stock Symbol,Quantity,Price Per Share,Total Value\n")
                    for symbol, quantity in portfolio.items():
                        price = stock_prices.get(symbol, 0)
                        value = quantity * price
                        f.write(f"{symbol},{quantity},{price:.2f},{value:.2f}\n")
                    total_investment = calculate_total_investment(portfolio, stock_prices)
                    f.write(f"\nTotal Investment,,,$ {total_investment:.2f}\n")
                display_message(f"Portfolio saved to {filename} successfully!")
            break # Exit loop after successful save
        except IOError as e:
            display_message(f"Error saving file: {e}", True)
        except Exception as e:
            display_message(f"An unexpected error occurred: {e}", True)

def main():
    """
    Main function to run the stock portfolio tracker application.
    """
    portfolio = {} # Stores {stock_symbol: quantity}
    stock_prices = get_stock_prices()

    while True:
        clear_screen()
        print("--- Simple Stock Portfolio Tracker ---")
        print("1. Add/Update Stock")
        print("2. View Portfolio")
        print("3. Save Portfolio to File")
        print("4. Exit")
        print("--------------------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_stock_to_portfolio(portfolio, stock_prices)
        elif choice == '2':
            display_portfolio(portfolio, stock_prices)
        elif choice == '3':
            save_portfolio_to_file(portfolio, stock_prices)
        elif choice == '4':
            display_message("Exiting the tracker. Goodbye!")
            break
        else:
            display_message("Invalid choice. Please enter a number between 1 and 4.", True)
        
        # Pause before clearing for the next menu display, unless exiting
        if choice != '4':
            pass # The display_portfolio and save_portfolio_to_file functions already pause

if __name__ == "__main__":
    main()

