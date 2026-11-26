# book_stored

# Bookstore Inventory and Analytics System

## Project Objective
A Python application to manage bookstore inventory, record book sales, calculate sales metrics, and create visual reports.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Project Files
- `bookstore_system.py` - Main Python program.
- `inventory.csv` - Sample inventory dataset.
- `sales.csv` - Sample sales dataset.

## Installation
Open a terminal in this folder and run:

```bash
pip install numpy pandas matplotlib seaborn
```

## Run the Project
```bash
python bookstore_system.py
```

## Main Features
1. Add, remove, update, and display books.
2. Record sales and automatically update stock.
3. Load, clean, and save CSV datasets using Pandas.
4. Calculate total revenue, average sales-record revenue, total books sold, best-selling book, and monthly revenue growth using NumPy and Pandas.
5. Analyze revenue by book, genre, and author.
6. Create a bar chart, monthly line graph, genre revenue pie chart, and price-sales correlation heatmap.

## Dataset Columns

### inventory.csv
`Title, Author, Genre, Price, Quantity`

### sales.csv
`Date, Title, Quantity Sold, Total Revenue`

Dates use the `YYYY-MM-DD` format.

## Notes
- The program creates empty CSV files automatically if the files are missing.
- Keep both CSV files in the same folder as `bookstore_system.py`.
- The supplied CSV files contain sample data. You can replace or extend them with your own records.
