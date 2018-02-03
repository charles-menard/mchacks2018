from sklearn.datasets import load_digits
# Import
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from .python_service.img import Preprocessor

# Split the `digits` data into training and test sets

# Loading data
digits = load_digits()
data = scale(digits.data)
targets=digits.target

X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, targets, digits.images, test_size=0.25, random_state=42)

X_train = pca_data(data=X_train,variance=0.50)

#svm
#def ml_svm(data=data_pca):
