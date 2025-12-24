import pandas as pd

df = pd.read_csv("data2/borrow_records.csv")

print("=== Data preview ===")
print(df)

print("\n=== Borrow count by user_type ===")
print(df.groupby("user_type").size())

print("\n=== Top borrowed books ===")
print(df["book_id"].value_counts())

print("\n=== Borrow type distribution ===")
print(df["book_type"].value_counts())
