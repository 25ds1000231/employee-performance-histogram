"""
Employee Performance Analysis

Email: 25ds1000231@ds.study.iitm.ac.in
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Generate synthetic dataset
np.random.seed(42)
departments = ["Sales", "Engineering", "HR", "Marketing", "Finance", "Support"]
regions = ["North", "South", "East", "West"]

data = []
for emp_id in range(1, 101):
    data.append({
        "EmployeeID": emp_id,
        "Department": np.random.choice(departments),
        "Region": np.random.choice(regions),
        "PerformanceScore": np.random.randint(50, 100)
    })

df = pd.DataFrame(data)

# Frequency count
sales_count = (df["Department"] == "Sales").sum()
print("Sales department count:", sales_count)

# Plot histogram
plt.figure(figsize=(8, 5))
sns.countplot(x="Department", data=df)
plt.title("Department Distribution")
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

# Create HTML
with open("employee_performance.html", "w") as f:
    f.write("<html><body>")
    f.write("<h1>Employee Performance Analysis</h1>")
    f.write("<p>Email: 25ds1000231@ds.study.iitm.ac.in</p>")
    f.write(f"<p>Sales Department Count = <strong>{sales_count}</strong></p>")
    f.write("<img src='histogram.png'>")
    f.write("</body></html>")
