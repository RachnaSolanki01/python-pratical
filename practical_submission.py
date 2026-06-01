import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class LibraryDashboard:

    def __init__(self):
        self.data = pd.read_csv("library_transactions.csv")

    def show_data(self):
        print(self.data.head())

    def statistics(self):

        print("Total Transactions =", len(self.data))

        # Control Structure
        if self.data.isnull().sum().sum() > 0:
            print("Missing values found")
        else:
            print("No missing values found")

        print("\nMost Borrowed Book")
        print(self.data["Book Title"].value_counts().head(1))

        print("\nMost Active User")
        print(self.data["User ID"].value_counts().head(1))

        # NumPy Array
        duration_array = np.array(
            self.data["Borrowing Duration (Days)"]
        )

        print("\nAverage Borrowing Duration")
        print(np.mean(duration_array))

        print("\nStandard Deviation")
        print(np.std(duration_array))

    def filter_genre(self, genre):

        result = self.data[
            self.data["Genre"] == genre
        ]

        print(result)

    def generate_report(self):

        print("\nLIBRARY REPORT")
        print("--------------------")

        print("Total Transactions:", len(self.data))

        print("\nBooks Borrowed:")

        print(
            self.data["Book Title"].value_counts()
        )

library = LibraryDashboard()

library.show_data()

library.statistics()

library.filter_genre("Fiction")

library.generate_report()


#Bar Chart
top_books = library.data["Book Title"].value_counts()

top_books.plot(kind="bar")

plt.title("Most Borrowed Books")

plt.show()



#Pie Chart

library.data["Genre"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.show()


#Line Chart

library.data["Date"] = pd.to_datetime(library.data["Date"])

monthly = library.data.groupby(library.data["Date"].dt.month).size()

monthly.plot(marker="o")

plt.title("Monthly Borrowing Trend")

plt.show()


#Heatmap

library.data["Date"] = pd.to_datetime(library.data["Date"])

library.data["Month"] = (library.data["Date"].dt.month)

heat_data = pd.crosstab(library.data["Genre"], library.data["Month"])

sns.heatmap(heat_data,annot=True)

plt.title("Borrowing Activity Heatmap")
plt.show()
