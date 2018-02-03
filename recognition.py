from sklearn.datasets import load_digits
# Import
from sklearn.preprocessing import scale
from preprocess_img import pca_data

# Loading data
digits = load_digits()
data_img = scale(digits.data)
target_img=digits.target

data_pca = pca_data(data_img,0.50)

#svm
#def ml_svm(data=data_pca):
