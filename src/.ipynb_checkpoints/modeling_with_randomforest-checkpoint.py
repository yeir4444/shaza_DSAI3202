import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import time
import itertools
import threading
import multiprocessing

# Load the train_dataset
file_path = '../data/housing_prices_data/train.csv'
train_data = pd.read_csv(file_path, index_col="Id")

# Columns to be deleted
columns_to_delete = ['MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']

# Delete the specified columns
train_data_cleaned = train_data.drop(columns=columns_to_delete, axis=1)

# Define the input features (X) and the output (y)
X = train_data_cleaned.drop('SalePrice', axis=1)
y = train_data_cleaned['SalePrice']

# Identify the categorical columns in X
categorical_columns = X.select_dtypes(include=['object']).columns

# Initialize a LabelEncoder for each categorical column
label_encoders = {column: LabelEncoder() for column in categorical_columns}

# Apply Label Encoding to each categorical column
for column in categorical_columns:
    X[column] = label_encoders[column].fit_transform(X[column])

# Split the first dataset (X, y) into train and test sets with a 70% - 30% split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30, random_state=42)

# Fill NaN values in X_train and X_val with the median of the respective columns
X_train_filled = X_train.fillna(X_train.median())
X_val_filled = X_val.fillna(X_val.median())

# Create a Random Forest model
rf_model = RandomForestRegressor(random_state=42)

# Train the model on the training data
rf_model.fit(X_train_filled, y_train)

# Make predictions on the validation data
y_val_pred_filled = rf_model.predict(X_val_filled)

# Calculate the RMSE on the validation data
rmse_filled = sqrt(mean_squared_error(y_val, y_val_pred_filled))

# Print the RMSE
print(f'RMSE on the validation data: {rmse_filled}')

start_time = time.time()

# Define the parameter ranges
n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
max_features_range = ['sqrt', 'log2', None]  # None means using all features
max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit

# Initialize variables to store the best model and its RMSE and parameters
best_rmse = float('inf')
best_mape = float('inf')
best_model = None
best_parameters = {}

# Loop over all possible combinations of parameters
for n_estimators in n_estimators_range:
    for max_features in max_features_range:
        for max_depth in max_depth_range:
            # Create and train the Random Forest model
            rf_model = RandomForestRegressor(
                n_estimators=n_estimators,
                max_features=max_features,
                max_depth=max_depth,
                random_state=42
            )
            rf_model.fit(X_train_filled, y_train)
            
            # Make predictions and compute RMSE
            y_val_pred = rf_model.predict(X_val_filled)
            rmse = sqrt(mean_squared_error(y_val, y_val_pred))
            # Compute MAPE
            mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
            # If the model is better than the current best, update the best model and its parameters
            if rmse < best_rmse:
                best_rmse = rmse
                best_mape = mape
                best_model = rf_model
                best_parameters = {
                    'n_estimators': n_estimators,
                    'max_features': max_features,
                    'max_depth': max_depth
                }
print(f"The best parameters {best_parameters} for RMSE = {best_rmse}, MAPE: {mape}%")
end_time = time.time()
sequential_time = start_time - end_time
print(f"The sequential execution time is {end_time - start_time}")

#threads_task
start_time = time.time()

n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
max_features_range = ['sqrt', 'log2', None]
max_depth_range = [1, 2, 5, 10, 20, None]

best_rmse = float('inf')
best_mape = float('inf')
best_model = None
best_parameters = {}

lock = threading.Lock()

def train_and_evaluate(n_estimators, max_features, max_depth):
    global best_rmse, best_mape, best_model, best_parameters
    
    rf_model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_features=max_features,
        max_depth=max_depth,
        random_state=42
    )
    rf_model.fit(X_train_filled, y_train)

    y_val_pred = rf_model.predict(X_val_filled)
    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
    
    with lock: 
        if rmse < best_rmse:
            best_rmse = rmse
            best_mape = mape
            best_model = rf_model
            best_parameters = {
                'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth
            }

param_combinations = list(itertools.product(n_estimators_range, max_features_range, max_depth_range))

threads = []
for params in param_combinations:
    t = threading.Thread(target=train_and_evaluate, args=params)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Best parameters: {best_parameters} for RMSE = {best_rmse}, MAPE = {best_mape}%")
end_time = time.time()
print(f"Threading execution time: {end_time - start_time} seconds")

#processes_task

start_time = time.time()

n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
max_features_range = ['sqrt', 'log2', None]
max_depth_range = [1, 2, 5, 10, 20, None]

manager = multiprocessing.Manager()
best_rmse = manager.Value('f', float('inf'))
best_mape = manager.Value('f', float('inf'))
best_parameters = manager.dict()

lock = manager.Lock()

def train_and_evaluate(n_estimators, max_features, max_depth, best_rmse, best_mape, best_parameters, lock):
    rf_model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_features=max_features,
        max_depth=max_depth,
        random_state=42
    )
    rf_model.fit(X_train_filled, y_train)

    y_val_pred = rf_model.predict(X_val_filled)
    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100
    
    with lock: 
        if rmse < best_rmse.value:
            best_rmse.value = rmse
            best_mape.value = mape
            best_parameters.clear()
            best_parameters.update({
                'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth
            })

param_combinations = list(itertools.product(n_estimators_range, max_features_range, max_depth_range))

processes = []
for params in param_combinations:
    p = multiprocessing.Process(target=train_and_evaluate, args=(*params, best_rmse, best_mape, best_parameters, lock))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print(f"Best parameters: {dict(best_parameters)} for RMSE = {best_rmse.value}, MAPE = {best_mape.value}%")
end_time = time.time()
print(f"Multiprocessing execution time: {end_time - start_time} seconds")


