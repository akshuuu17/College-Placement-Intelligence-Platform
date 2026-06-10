import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv(
    r"C:\Users\AKSHAT\OneDrive\Documents\Placement Project\dataset\placement_project.csv"
)

# Title
st.title("🎓 College Placement Intelligence Platform")

# Dataset Preview
st.header("Dataset Preview")
st.dataframe(data.head())

# Dataset Shape
st.header("Dataset Information")
st.write("Rows:", data.shape[0])
st.write("Columns:", data.shape[1])

# Placement Status Distribution
st.header("Placement Status Distribution")

status_count = data['status'].value_counts()

st.bar_chart(status_count)

# Dataset Statistics
st.header("Dataset Statistics")
st.write(data.describe())

# Placement Distribution Graph
st.header("Placement Distribution Graph")

fig, ax = plt.subplots()

data['status'].value_counts().plot(kind='bar', ax=ax)

plt.xlabel("Placement Status")
plt.ylabel("Number of Students")

st.pyplot(fig)




# Student Search



st.header("🔍 Student Search")

row_number = st.number_input(
    "Enter Student Row Number",
    min_value=0,
    max_value=len(data)-1,
    value=0
)

if st.button("Show Student Data"):
    st.write(data.iloc[row_number])




# Placement Prediction




st.header("🎯 Placement Prediction")

ssc_p = st.number_input("10th Percentage", 0.0, 100.0)
hsc_p = st.number_input("12th Percentage", 0.0, 100.0)
degree_p = st.number_input("Degree Percentage", 0.0, 100.0)
etest_p = st.number_input("Employability Test Score", 0.0, 100.0)
mba_p = st.number_input("MBA Percentage", 0.0, 100.0)

if st.button("Predict Placement"):

    avg_score = (
        ssc_p +
        hsc_p +
        degree_p +
        etest_p +
        mba_p
    ) / 5

    st.write("Average Score:", round(avg_score, 2))

    if avg_score >= 60:
        st.success("✅ High Chance of Placement")
    else:
        st.error("❌ Low Chance of Placement")

# Footer
st.markdown("---")
st.write("Developed using Python, Pandas, Matplotlib and Streamlit")



#streamlit run app.py   run the dashboard 
