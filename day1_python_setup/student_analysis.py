import pandas as pd

data = {
    "Student": ["Ali", "Sara", "John", "Maya"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print("Student Data")
print(df)

average = df["Marks"].mean()

print("Average Marks:", average)