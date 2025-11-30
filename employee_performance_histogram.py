# employee_performance_histogram.py
# Author email (for verification): 25ds1000231@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import base64
from textwrap import dedent

def main():
    # 1. Load the 100-employee dataset
    csv_path = "employee_performance_dataset.csv"  # Change if your file has a different name
    df = pd.read_csv(csv_path)

    # 2. Calculate frequency count for the "Sales" department
    sales_count = (df["department"] == "Sales").sum()
    print(f"Number of employees in Sales department: {sales_count}")

    # 3. Create a histogram / bar chart of department distribution
    dept_counts = df["department"].value_counts().sort_index()

    plt.figure(figsize=(8, 6))
    dept_counts.plot(kind="bar")
    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.tight_layout()

    # Save the figure as PNG
    png_path = "employee_performance_histogram.png"
    plt.savefig(png_path)
    plt.close()

    # 4. Create an HTML file that includes:
    #    - Your email
    #    - The Sales department frequency
    #    - The histogram embedded as a base64 image (self-contained HTML)

    # Read the PNG and convert to base64 so the HTML is standalone
    with open(png_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Optional: store the main code snippet as text to embed in the HTML
    code_snippet = dedent(
        """\
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.read_csv("employee_performance_dataset.csv")
        sales_count = (df["department"] == "Sales").sum()
        print(f"Number of employees in Sales department: {sales_count}")

        dept_counts = df["department"].value_counts().sort_index()
        plt.figure(figsize=(8, 6))
        dept_counts.plot(kind="bar")
        plt.title("Employee Count by Department")
        plt.xlabel("Department")
        plt.ylabel("Number of Employees")
        plt.tight_layout()
        plt.show()
        """
    )

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee Performance - Department Histogram</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ccc;
        }}
    </style>
</head>
<body>
    <h1>Employee Performance - Department Distribution</h1>
    <p><strong>Author email (for verification):</strong> 25ds1000231@ds.study.iitm.ac.in</p>
    <p><strong>Number of employees in Sales department:</strong> {sales_count}</p>

    <h2>Department Histogram</h2>
    <img src="data:image/png;base64,{img_b64}" alt="Department Histogram">

    <h2>Main Analysis Code Snippet</h2>
    <pre><code>{code_snippet}</code></pre>
</body>
</html>
"""

    html_path = "employee_performance.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Saved HTML report to {html_path}")


if __name__ == "__main__":
    main()
