import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder

# Load train data
train_data = pd.read_csv("Train_data.csv")

# Identify categorical columns (excluding 'class')
categorical_cols = train_data.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('class')

# Perform One-Hot Encoding for train data
encoder = OneHotEncoder(handle_unknown='ignore')
encoded_train = pd.DataFrame(encoder.fit_transform(train_data[categorical_cols]).toarray())

# Reassign column names
encoded_train.columns = encoder.get_feature_names_out(categorical_cols)

# Concatenate encoded columns with original data
train_data_encoded = pd.concat([train_data.drop(columns=categorical_cols), encoded_train], axis=1)

# Separate features and labels for train data
X_train = train_data_encoded.drop('class', axis=1)
y_train = train_data_encoded['class']

# Initialize and train the Isolation Forest model
isolation_forest = IsolationForest(contamination=0.1)
isolation_forest.fit(X_train)

# Load test data
test_data = pd.read_csv("Test_data.csv")

# Check if 'class' column exists in test data
if 'class' in test_data.columns:
    # Drop 'class' column from test data
    test_data.drop(columns=['class'], inplace=True)

# Perform One-Hot Encoding for test data
encoded_test = pd.DataFrame(encoder.transform(test_data[categorical_cols]).toarray())
encoded_test.columns = encoder.get_feature_names_out(categorical_cols)
test_data_encoded = pd.concat([test_data.drop(columns=categorical_cols), encoded_test], axis=1)

# Detect anomalies in the test data
anomaly_predictions = isolation_forest.predict(test_data_encoded)

# Print the predictions
print("Anomaly Predictions for Test Data:")
print(anomaly_predictions)

# Save the predictions to a CSV file
test_data['anomaly_prediction'] = anomaly_predictions
test_data.to_csv("test_data_with_anomaly_predictions.csv", index=False)
print("Anomaly predictions saved to 'test_data_with_anomaly_predictions.csv'")
