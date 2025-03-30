from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load the Iris dataset
data = datasets.load_iris()
X, y = data.data, data.target

# Split the data: 80% for training (10% labeled, 70% unlabeled) and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_labeled, X_unlabeled, y_labeled, _ = train_test_split(X_train, y_train, test_size=0.875, random_state=42)

# Initialize with a standard SVM on the labeled data
clf = SVC(probability=True)
clf.fit(X_labeled, y_labeled)

# Transductive learning: Iterate and refine
for _ in range(10): # 10 iterations for simplicity
    # Classify the unlabeled data
    probabilities = clf.predict_proba(X_unlabeled)
    y_unlabeled_predicted = probabilities.argmax(axis=1)
    
    # Combine labeled and newly labeled data
    X_combined = np.vstack((X_labeled, X_unlabeled))
    y_combined = np.hstack((y_labeled, y_unlabeled_predicted))
    
    # Refit the model
    clf.fit(X_combined, y_combined)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")