"""
Employee Performance Analysis

Email: 25ds1000231@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# --------------------------------------------------
# Create dataset of 100 employees with EXACTLY 20 SALES
# --------------------------------------------------
np.random.seed(42)

departments_other = ["Finance", "Marketing", "HR", "Engineering", "Support"]

departments = ["Sales"] * 20 + list(
    np.random.choice(departments_other, size=80)
)

regions = np.random.choice(
    ["North America", "Europe", "Middle East", "Asia Pacific", "Africa"],
    size=100
)

performance_score = np.random.uniform(60, 95, 100).round(2)
years_experience = np.random.randint(1, 20, 100)
satisfaction_rating = np.random.uniform(1.0, 5.0, 100).round(1)

df = pd.DataFrame({
    "employee_id": [f"EMP{i:03d}" for i in range(1, 101)],
    "department": departments,
    "region": regions,
    "performance_score": performance_score,
    "years_experience": years_experience,
    "satisfaction_rating": satisfaction_rating
})


# ---------------------------
# VERIFY SALES COUNT
# ---------------------------
sales_count = (df["department"] == "Sales").sum()
print(">>> SALES COUNT SHOULD BE 20 <<<")
print("Sales Department Count:", sales_count)


# ---------------------------
# Plot
# ---------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="department", data=df)
plt.title("Employee Count by Department")
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()


# ---------------------------
# HTML
# ---------------------------
with open("employee_performance.html", "w") as f:
    f.write("<html><body>")
    f.write("<h1>Employee Performance Analysis</h1>")
    f.write("<p>Email: 25ds1000231@ds.study.iitm.ac.in</p>")
    f.write(f"<p>Sales Department Count = <strong>{sales_count}</strong></p>")
    f.write("<img src='histogram.png'>")
    f.write("</body></html>")
