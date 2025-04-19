import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


digits = load_digits()
X, y = digits.data, digits.target 

# Convert pixel values into binary (Threshold: 8)
X_binary = np.where(X < 8, 0, 1)

# Split dataset: 10% for training (179 samples), remaining for testing
X_train, X_test, y_train, y_test = train_test_split(X_binary, y, train_size=179, stratify=y, random_state=42)

# Define values of K to test
k_values = [1, 3, 5, 10, 20]
accuracies = []

# Run KNN for different K values and calculate accuracy
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train) 
    y_pred = knn.predict(X_test)  
    accuracy = accuracy_score(y_test, y_pred) * 100 
    accuracies.append(accuracy) 
    print(f"Accuracy for k={k}: {accuracy:.2f}%")

# Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='-', color='b', markersize=8, label="Accuracy")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Accuracy (%)")
plt.title("KNN Classification Accuracy vs. K")
plt.xticks(k_values)  
plt.grid(True)
plt.legend()
plt.show()
