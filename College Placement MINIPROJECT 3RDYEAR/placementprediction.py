import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv(
    r"C:\Users\AKSHAT\OneDrive\Documents\Placement Project\dataset\placement_project.csv"
)

# Remove unnecessary columns
data = data.drop(['sl_no', 'salary'], axis=1)

# Convert text columns into numbers
encoder = LabelEncoder()

for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = encoder.fit_transform(data[column])

# Features and Target
X = data.drop('status', axis=1)
y = data['status']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy =", accuracy)