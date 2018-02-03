#imports
from sklearn.datasets import load_digits
from sklearn import metrics
from preprocess_img import ml_preprocessing
from sklearn import svm
from saver import Saver
from sklearn.grid_search import GridSearchCV
#from fetch_data import fetchImage

# Loading data
digits = load_digits()
data = digits.data
labels=digits.target

#Parameter candidates for the grid search of SVC
parameters_canditates= [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},]
estimator = svm.SVC()

def train(nom_du_model,data,labels,estimator,parameters_canditates):
    # create the test and data for training
    X_train, X_test, y_train, y_test = ml_preprocessing(data,labels,variance=0.75,test_size=0.25,random_state=42)

    #grid search
    clf = GridSearchCV(estimator=estimator, param_grid=parameters_canditates, n_jobs=-1)

    #fitting the model
    clf.fit(X_train, y_train)

    # Save model
    my_saver = Saver()
    my_saver.save(clf, "./trained_models", nom_du_model+"_model")

    # Print out the results
    print('Best score for training data:', clf.best_score_)
    print('Best `C`:',clf.best_estimator_.C)
    print('Best kernel:',clf.best_estimator_.kernel)
    print('Best `gamma`:',clf.best_estimator_.gamma)

    # prediction of labels
    y_pred=clf.predict(X_test)

    # Print out the confusion matrix
    print(metrics.confusion_matrix(y_test, y_pred))

train("number",data,labels,estimator,parameters_canditates)
