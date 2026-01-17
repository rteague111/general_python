import pandas as pd
import sqlite3
from dataclasses import dataclass
from enum import Enum

# Enums and dataclass

class Category(Enum):
    TOOLS = "Tools"
    ELECTRONICS = "Electronics"
    ACCESSORIES = "Accessories"

@dataclass
class Product:
    name: str
    category: Category
    price: float
    quantity:int

# sample data

products = [

Product("Soldering Iron", Category.TOOLS, 29.99, 5),
Product("Multimeter", Category.ELECTRONICS, 49.50, 3),
Product("Wire Stripper", Category.TOOLS, 15.75, 10),
Product("USB Oscilliscope", Category.ELECTRONICS, 89.99, 2),
Product("Magnetic Tray", Category.ACCESSORIES, 9.99, 8),

]

# SQLite setup

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE inventory(
    name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER      
)
""")

cursor.executemany("""
INSERT INTO inventory (name, category, price, quantity)
VALUES (?, ?, ?, ?)
""", [(p.name, p.category.value, p.price, p.quantity) for p in products])

conn.commit()

# Query and Pandas Analysis

df = pd.read_sql_query("SELECT * FROM inventory", conn)

# Group by category and get average price

avg_price = df.groupby("category")["price"].mean().reset_index()
print("Average price per category: \n", avg_price)

#---------------
# BONUS PRACTICE BLOCK!: .xf formatting:
# single value
avg = df["price"].mean()
print(f"\nAverage price: ${avg: .2f}")
#whole column
df["price_rounded"] = df["price"].round(2)
print(df[["name", "price_rounded"]])
#groupby average category
avg_price = df.groupby("category")["price"].mean().round(2).reset_index()
print("\nAverage price per category: \n", avg_price)
#--------------

# Filter products over $30

expensive = df[df["price"] > 30]
print("\nProducts over $30: \n", expensive)

# show printing price with quantity total
df["total_value"] = df["price"] * df["quantity"]
print("\nTotal inventory value per item: \n", df[["name", "total_value"]])

# group and aggregate

category_summary = df.groupby("category").agg({
    "price": "mean",
    "quantity": "sum",
    "total_value": "sum"    
}).reset_index()

print("\nCategory summary: \n", category_summary)

# filter and sory

high_value = df[df["total_value"] > 100].sort_values(by="total_value", ascending=False)
print("\nHigh-Value items: \n", high_value)

# SQL Query with conditions

query = """
SELECT * FROM inventory
WHERE category = 'Tools' AND price < 30
"""

tools_under_30 = pd.read_sql_query(query, conn)
print("\nTools under $30: \n", tools_under_30)

#optional: enum filtering in python

tools_df = df[df["category"] == Category.TOOLS.value]
print("\nFiltered by Enum (Tools): \n", tools_df)

conn.close()