# Handwritten-Digits-Classification-using-KNN


## **1. Dataset Information**

### **Dataset Used: Scikit-learn Digits Dataset**

The **Digits dataset** from Scikit-learn consists of 1,797 grayscale images of handwritten digits (0-9).
 Each image is **8×8 pixels**, where each pixel has an intensity value ranging from **0 to 16**.


## **2. Sample Data Table**

Below is a small sample of the dataset, showing pixel intensity values before and after binary conversion.

| Sample Index | Pixel 1 | Pixel 2 | Pixel 3 | ... | Pixel 64 | Label |
| ------------ | ------- | ------- | ------- | --- | -------- | ----- |
| 0            | 0       | 0       | 5       | ... | 0        | **0** |
| 1            | 0       | 0       | 0       | ... | 0        | **1** |
| 2            | 0       | 0       | 8       | ... | 2        | **2** |
| 3            | 0       | 0       | 10      | ... | 0        | **3** |
| 4            | 0       | 1       | 16      | ... | 4        | **4** |

### **Binary Converted Data (Threshold Applied: values < 8 → 0, values ≥ 8 → 1)**

| Sample Index | Pixel 1 | Pixel 2 | Pixel 3 | ... | Pixel 64 | Label |
| ------------ | ------- | ------- | ------- | --- | -------- | ----- |
| 0            | 0       | 0       | 0       | ... | 0        | **0** |
| 1            | 0       | 0       | 0       | ... | 0        | **1** |
| 2            | 0       | 0       | 1       | ... | 0        | **2** |
| 3            | 0       | 0       | 1       | ... | 0        | **3** |
| 4            | 0       | 0       | 1       | ... | 0        | **4** |






## **3. Algorithm Used**

The **K-Nearest Neighbors (KNN) Algorithm** is used for classification. The steps are:

1. **Load the Digits Dataset** from scikit-learn.
2. **Convert the data to binary form**, setting values **below 8 to 0** and **8 or above to 1**.
3. **Split the data**, using **10% (179 samples) for training** and **the remaining for testing**.
4. **Apply KNN Classifier** for different values of **k = {1,3,5,10,20}**.
5. **Predict labels** for the test data.
6. **Calculate classification accuracy** for each k value.
7. **Plot accuracy vs k value** to visualize performance.




## **4. Results & Graphs**



![Screenshot 2025-04-03 172658](https://github.com/user-attachments/assets/e63599fc-ad7c-4e7c-aaff-c0283600b270)



![Screenshot 2025-04-03 172709](https://github.com/user-attachments/assets/1d1f631e-d633-4029-a907-00c973d8c59b)








