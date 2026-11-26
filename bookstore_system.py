import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"

class bookstore:

    def __init__(self):
        self.inventory = pd.DataFrame(
                    columns=["Title", "Author", "Genre", "Price", "Quantity"]
                )
        self.sales = pd.DataFrame(
                    columns=["Date", "Title", "Quantity Sold", "Total Revenue"]
                )
        self.load_data()
        
    def load_data(self):
        if os.path.exists(INVENTORY_FILE):
            self.inventory = pd.read_csv(INVENTORY_FILE)

        else:
            self.inventory.to_csv(INVENTORY_FILE , index=False)


        if os.path.exists(SALES_FILE):
            self.inventory = pd.read_csv(INVENTORY_FILE)

        else:
            self.inventory.to_csv(SALES_FILE , index=False)

            for column in ["Price", "Quantity"]:
                    self.inventory[column] = pd.to_numeric(
                        self.inventory[column], errors="coerce"
                    )
            for column in ["Quantity Sold", "Total Revenue"]:
                    self.sales[column] = pd.to_numeric(
                        self.sales[column], errors="coerce"
                    )
                    self.inventory = self.inventory.dropna(
                                subset=["Title", "Author", "Genre", "Price", "Quantity"]
                            )
                    self.sales = self.sales.dropna(
                                subset=["Date", "Title", "Quantity Sold", "Total Revenue"]
                            )
                    self.inventory["Quantity"] = self.inventory["Quantity"].astype(int)
                    self.sales["Quantity Sold"] = self.sales["Quantity Sold"].astype(int)
                    self.sales["Date"] = pd.to_datetime(
                    self.sales["Date"], errors="coerce"
                            )
                    self.sales = self.sales.dropna(subset=["Date"])
                    self.save_data()

    def save_data(self):

        self.inventory.to_csv(INVENTORY_FILE , index=False)
        sales_to_saves = self.sales.copy
        if not sales_to_saves.empty:
             sales_to_saves["Date"] = pd.to_datetime(
                             sales_to_saves["Date"]
              to_save.to_csv(SALES_FILE, index=False)
             
             
    def add_book(self, title, author, genre, price, quantity):
    to_save.to_csv(SALES_FILE, index=False)
    
        def add_book(self, title, author, genre, price, quantity):
    """Add a new book or increase stock if the title already exists."""
    if price <= 0 or quantity < 0:
        print("Price must be positive and quantity cannot be negative.")
        return

     match = self.inventory["Title"].str.lower() == title.lower()
            if match.any():
                self.inventory.loc[match, "Quantity"] += quantity
                self.inventory.loc[match, ["Author", "Genre", "Price"]] = [
                    author, genre, price
                ]


                print("Book already existed. Its details and stock were updated.")

            else:
                new_book=d.DataFrame([{
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Price": price,
                "Quantity": quantity}])
                }])
        self.inventory = pd.concat(
                [self.inventory, new_book], ignore_index=True
                        )
        print("Book added successfully.")
        self.save_data()
            
        def remove_book(self, title):
                    """Remove a book from inventory using its title."""
                    before = len(self.inventory)
                    self.inventory = self.inventory[
                        self.inventory["Title"].str.lower() != title.lower()
                    ]
                    if len(self.inventory) < before:
                        print("Book removed successfully.")
                    else:
                        print("Book was not found.")
                    self.save_data()

        def update_book(self, title):
                """Update author, genre, price, and/or stock for an existing book."""
                matches = self.inventory.index[
                    self.inventory["Title"].str.lower() == title.lower()
                ]
                if len(matches) == 0:
                    print("Book was not found.")
                    return
        
                index = matches[0]
                print("Press Enter to keep the current value.")
                author = input(f"Author [{self.inventory.at[index, 'Author']}]: ").strip()
                genre = input(f"Genre [{self.inventory.at[index, 'Genre']}]: ").strip()
                price_text = input(f"Price [{self.inventory.at[index, 'Price']}]: ").strip()
                quantity_text = input(
                    f"Quantity [{self.inventory.at[index, 'Quantity']}]: "
                ).strip()

        def display_inventory(self):
            if self.inventory.empty:
                 print("Inventory is empty")

            else:
                 print("BOOK INVENTORY")
                 print(self.inventory.to_string(index=False))

        def recoard_sale(self ,tittle , quantity_sold):
            if quantity_sold <= 0:
                        print("Quantity sold must be greater than zero.")
                        return
            
            matches = self.inventory.index[
                        self.inventory["Title"].str.lower() == title.lower()
                    ]
            if len(matches) == 0:
                        print("Book was not found.")
                        return

            price = float(self.inventory.at[index, "Price"])
            revenue = price * quantity_sold
            self.inventory.at[index, "Quantity"] -= quantity_sold
            
            new_sale = pd.DataFrame([{
            "Date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "Title": self.inventory.at[index, "Title"],
            "Quantity Sold": quantity_sold,
            "Total Revenue": revenue
             }])
            self.sales = pd.concat([self.sales, new_sale], ignore_index=True)
            self.save_data()
            print(f"Sale recorded. Total revenue: Rs. {revenue:.2f}")

            def sales_analysis(self):
                    """Calculate sales metrics using Pandas and NumPy."""
                    if self.sales.empty:
                        print("No sales data is available for analysis.")
                        return
            
                    quantities = self.sales["Quantity Sold"].to_numpy(dtype=float)
                    revenues = self.sales["Total Revenue"].to_numpy(dtype=float)
            
                    total_revenue = np.sum(revenues)
                    average_sale_revenue = np.mean(revenues)
                    total_books_sold = np.sum(quantities)
            
                    print("\nSALES ANALYSIS")
                    print(f"Total revenue: Rs. {total_revenue:.2f}")
                    print(f"Average revenue per sales record: Rs. {average_sale_revenue:.2f}")
                    print(f"Total books sold: {int(total_books_sold)}")
            
                    book_sales = self.sales.groupby("Title")["Quantity Sold"].sum()
                    if not book_sales.empty:
                        print("\nBest-selling book:")
                        print(f"{book_sales.idxmax()} ({int(book_sales.max())} copies)")
            
                    print("\nRevenue by book:")
                    print(
                        self.sales.groupby("Title")["Total Revenue"]
                        .sum().sort_values(ascending=False).to_string()
                    )
            
                    
                    monthly = self.sales.copy()
                    monthly["Month"] = pd.to_datetime(monthly["Date"]).dt.to_period("M")
                    monthly_revenue = monthly.groupby("Month")["Total Revenue"].sum()
                    if len(monthly_revenue) >= 2:
                        growth = monthly_revenue.pct_change().replace(
                            [np.inf, -np.inf], np.nan
                        ) * 100
                        print("\nMonthly revenue growth (%):")
                        print(growth.round(2).to_string())
                    else:
                        print("\nMonthly growth needs sales from at least two different months.")
            
                    
                    details = self.sales.merge(
                        self.inventory[["Title", "Author", "Genre"]],
                        on="Title",
                        how="left"
                    )
                    if not details.empty:
                        print("\nRevenue by genre:")
                        print(details.groupby("Genre")["Total Revenue"].sum().to_string())
                        print("\nRevenue by author:")
                        print(details.groupby("Author")["Total Revenue"].sum().to_string())
            
                def create_visualizations(self):
                    """Create bar, line, pie, and heatmap charts."""
                    if self.sales.empty:
                        print("No sales data is available to create charts.")
                        return
            
                    sns.set_theme(style="whitegrid")
                    sales = self.sales.copy()
                    sales["Date"] = pd.to_datetime(sales["Date"])
            
            

             
            while True:
                    print("\n========== BOOKSTORE INVENTORY AND ANALYTICS SYSTEM ==========")
                    print("1. Add Book")
                    print("2. Remove Book")
                    print("3. Update Book")
                    print("4. Display Inventory")
                    print("5. Record Sale")
                    print("6. Sales Analysis")
                    print("7. Create Visualizations")
                    print("8. Exit")
        
                    choice = input("Enter your choice (1-8): ").strip()
        
                    if choice == "1":
                        title = input("Enter book title: ").strip()
                        author = input("Enter author name: ").strip()
                        genre = input("Enter book genre: ").strip()
                        try:
                            price = float(input("Enter book price: "))
                            quantity = int(input("Enter stock quantity: "))
                            self.add_book(title, author, genre, price, quantity)
                        except ValueError:
                            print("Please enter a valid number for price and quantity.")
        
                    elif choice == "2":
                        self.remove_book(input("Enter title to remove: ").strip())
        
                    elif choice == "3":
                        self.update_book(input("Enter title to update: ").strip())
                    elif choice == "4":
                                    self.display_inventory()
                    
                    elif choice == "5":
                                    title = input("Enter book title: ").strip()
                                    try:
                                        quantity = int(input("Enter quantity sold: "))
                                        self.record_sale(title, quantity)
                                    except ValueError:
                                        print("Quantity must be a whole number.")
                    
                    elif choice == "6":
                                    self.sales_analysis()
                    
                                
                                    break
                    
                    else:
                                    print("Invalid choice. Please select a number from 1 to 8.")
                    
                    
                    if __name__ == "__main__":
                        
                    
        
                    


         

