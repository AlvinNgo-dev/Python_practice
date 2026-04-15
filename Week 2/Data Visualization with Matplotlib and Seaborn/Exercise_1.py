import matplotlib.pyplot as plt

# Line Plot
years = [2012, 2013, 2014, 2015, 2016, 2017,
         2018, 2019, 2020, 2021, 2022, 2023]
sales = [220, 240, 260, 300, 280, 310, 330, 360, 340, 380, 400, 420]

plt.plot(years, sales, label="Sales Trend", color="blue", marker="o")
plt.title("Sales over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
# plt.show()

# Bar chart
categories = ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]
plt.bar(categories, revenue, color="green")
plt.title("Revenue by Category")
# plt.show()

# Scatter Plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]
plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Study hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
# plt. show()

# Histogram
sales_2020 = [200, 220, 250, 270, 300, 320, 310, 290, 280, 260]
sales_2021 = [210, 230, 260, 280, 310, 330, 340, 320, 300, 290]
sales_2022 = [220, 240, 270, 300, 330, 360, 350, 340, 320, 310]

plt.hist(sales_2020, bins=5, alpha=0.6, label="2020")
plt.hist(sales_2021, bins=5, alpha=0.6, label="2021")
plt.hist(sales_2022, bins=5, alpha=0.6, label="2022")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Overlaid Sales Histograms")
plt.legend()
# plt.show()


plt.figure(figsize=(10, 14))

# Multiple plot
# ---- Subplot 1: Line Plot ----
plt.subplot(4, 1, 1)   # (rows, cols, index)
plt.plot(years, sales, marker="o")
plt.title("Sales over Years")
plt.xlabel("Years")
plt.ylabel("Sales")

# ---- Subplot 2: Bar Chart ----
plt.subplot(4, 1, 2)
plt.bar(categories, revenue)
plt.title("Revenue by Category")
plt.ylabel("Revenue")

# ---- Subplot 3: Scatter Plot ----
plt.subplot(4, 1, 3)
plt.scatter(hours_studied, exam_scores)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")

# ---- Subplot 4: Histogram ----
plt.subplot(4, 1, 4)
plt.hist(sales_2020, bins=5, alpha=0.6, label="2020")
plt.hist(sales_2021, bins=5, alpha=0.6, label="2021")
plt.hist(sales_2022, bins=5, alpha=0.6, label="2022")
plt.title("Overlaid Sales Histograms")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.legend()

# Adjust layout and show
plt.tight_layout()
plt.show()
