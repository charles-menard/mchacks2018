from sklearn.datasets import load_digits
# Import
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
<<<<<<< HEAD:python_service/train.py
from .python_service.img import Preprocessor
=======
from sklearn.decomposition import PCA

>>>>>>> 83efbbc277f1b11bf11f0e70b463afd24f09bc9c:python_service/model_trainer/train.py

# Split the `digits` data into training and test sets

# Loading data
digits = load_digits()
data = scale(digits.data)
targets=digits.target

def pca_data(data,variance=0.50):
    pca = PCA(variance).fit(data)
    components = pca.transform(data)
    return components

data = pca_data(data=data,variance=0.75)

X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, targets, digits.images, test_size=0.25, random_state=42)



# Import the `svm` model
from sklearn import svm

# Create the SVC model
svc_model = svm.SVC(gamma=0.001, C=100., kernel='linear')

# Fit the data to the SVC model
svc_model.fit(X_train, y_train)

# Predict the label of `X_test`
y_pred=svc_model.predict(X_test)

# Import `metrics` from `sklearn`
from sklearn import metrics

# Print out the confusion matrix with `confusion_matrix()`
print(metrics.confusion_matrix(y_test, y_pred))
