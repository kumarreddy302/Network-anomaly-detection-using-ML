# Network-anomaly-detection-using-ML
This Python script provides a comprehensive implementation of anomaly detection utilizing the Isolation Forest algorithm, a powerful technique widely employed in cybersecurity, data analysis, and anomaly detection tasks. The script begins by loading both training and test datasets from CSV files, employing the versatile Pandas library for efficient data handling. Subsequently, categorical columns within the training data are identified and transformed into numerical representations through one-hot encoding, a crucial preprocessing step for facilitating machine learning model compatibility.

Following data preprocessing, the script proceeds to train an Isolation Forest model on the preprocessed training dataset. Leveraging the model's ability to discern patterns of normal behavior, anomalies are subsequently detected within the test dataset. This detection process involves predicting anomalies based on deviations from the established norms learned during model training. The script outputs the anomaly predictions to the console, providing immediate insights into potential outliers within the test dataset.

Moreover, the script offers a practical utility by saving the anomaly predictions to a CSV file titled "test_data_with_anomaly_predictions.csv." This feature enables further analysis and examination of identified anomalies, allowing for comprehensive anomaly detection and mitigation strategies. Whether employed in cybersecurity applications, data analysis tasks, or anomaly detection research, this script serves as a valuable tool for detecting outliers and anomalies within diverse datasets. With its clear implementation of the Isolation Forest algorithm, this script facilitates effective anomaly detection and contributes to the enhancement of cybersecurity measures and data analysis practices.

#RUN THE CODE

1.Clone the Repository
- ```git clone https://github.com/kumarreddy302/Network-anomaly-detection-using-ML.git```

2.Navigate to Folder
   - ```cd Network-anomaly-detection-using-ML```
3. Install panda and scikit-learn module using pip command
  - ```pip install pandas```
  - ```pip install scikitlearn```
4. Run the python script
  - ``` python network_anomolies.py ```
### Contributions

Contributions to this project are not currently accepted.

Contact:
    Email: kovvurisai750@gmail.com
    WhatsApp: +91 9550763666
