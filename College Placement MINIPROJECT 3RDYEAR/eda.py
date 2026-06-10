"""import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    r"C:\Users\AKSHAT\OneDrive\Documents\Placement Project\dataset\placement_project.csv"
)

# Placement Status Count
data['status'].value_counts().plot(kind='bar')

plt.title("Placement Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Students")

plt.show()"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    r"C:\Users\AKSHAT\OneDrive\Documents\Placement Project\dataset\placement_project.csv"
)

plt.scatter(data['ssc_p'], data['etest_p'])

plt.xlabel("10th Percentage")
plt.ylabel("Employability Test Score")
plt.title("10th Percentage vs Employability Test Score")

plt.show()