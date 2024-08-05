# Taxi Fare Prediction Project

## Overview
This project aims to develop a machine learning model to predict taxi fares based on historical trip data. Utilizing Python and several machine learning algorithms, the model achieves high accuracy and provides insights into factors influencing taxi fares.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Flask
- **Development Environment**: Jupyter Notebook

## Data Collection and Preprocessing
1. **Data Source**: NYC Taxi and Limousine Commission (TLC) trip record data.
2. **Data Cleaning**: Handled missing values, removed duplicates, and filtered outliers.
3. **Feature Engineering**:
   - **Trip Details**: Extracted pickup and drop-off latitude and longitude.
   - **Time Features**: Included pickup date and time, day of the week, and hour of the day.
   - **Distance Calculation**: Used the Haversine formula to compute the distance between pickup and drop-off points.
   - **Weather Conditions**: Integrated weather data when available.

## Model Development
1. **Model Selection**: Implemented Random Forest, Linear Regression, Gradient Boosting, and XGBoost.
2. **Training and Testing**: Split the data into training and testing sets.
3. **Hyperparameter Tuning**: Optimized model parameters using GridSearchCV.
4. **Model Evaluation**: Evaluated models using RMSE, MAE, and R² score metrics.

## Random Forest Implementation
- **Fitting the Model**: Trained the Random Forest model on the training data.
- **Feature Importance**: Assessed feature importance to determine influential factors.
- **Performance Evaluation**: Evaluated the model’s performance on the test set.

## Results and Visualization
- **Model Comparison**: Compared the performance of different models.
- **Visualization**: Used Matplotlib and Seaborn to visualize:
  - Predicted vs. actual fare distributions
  - Feature importance
  - Residual plots to assess model fit

## Deployment and Future Work
- **Deployment**: Developed a Flask-based web interface for real-time fare predictions.
- **API Integration**: Created an API endpoint to receive trip details and return fare predictions.
- **Future Enhancements**: Plan to improve model accuracy by incorporating additional features like traffic data and public events.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/taxi-fare-prediction.git
