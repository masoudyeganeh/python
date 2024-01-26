from sklearn.metrics import mean_squared_error

# Given values
Y_true = [2, 4, 3, 2, 5, 6, 7]  # Y_true = Y (original values)

# calculated values
Y_pred = [2, 3.5, 2.7, 2, 4.3, 6, 7.5]  # Y_pred = Y'

# Calculation of Mean Squared Error (MSE)
mean_squared_error(Y_true, Y_pred)

print(mean_squared_error(Y_true, Y_pred))