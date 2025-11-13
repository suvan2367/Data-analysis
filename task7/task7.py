import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the database and insert sample sales data
def setup_database():
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()
    
    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Insert sample data
    sales_records = [
        ('Apple', 10, 0.5),
        ('Banana', 5, 0.3),
        ('Apple', 8, 0.5),
        ('Orange', 15, 0.6),
        ('Banana', 7, 0.3),
        ('Orange', 5, 0.6),
    ]

    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_records)
    conn.commit()
    conn.close()

# Step 2: Query the data and load into pandas
def get_sales_summary():
    conn = sqlite3.connect("sales_data.db")
    query = """
    SELECT 
        product, 
        SUM(quantity) AS total_qty, 
        ROUND(SUM(quantity * price), 2) AS revenue
    FROM sales
    GROUP BY product
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Step 3: Print and plot results
def display_summary(df):
    print("Sales Summary:")
    print(df)

    # Plot revenue per product
    df.plot(kind='bar', x='product', y='revenue', legend=False)
    plt.title("Revenue per Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("sales_chart.png")  # Save the chart
    plt.show()

# Run the complete flow
setup_database()
sales_df = get_sales_summary()
display_summary(sales_df)
