#imports
from sklearn.datasets import load_digits
from sklearn import metrics
from preprocess_img import ml_preprocessing
from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
from saver import Saver
from sklearn.grid_search import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
from fetch_data import fetchImage
from sklearn.neural_network import MLPClassifier

# Loading data

#Parameter candidates for the grid search of SVC


def trainModel(nom_du_model, classifier="svm"):
    # create the test and data for training
    X, y, listOfLabels  = fetchImage(nom_du_model)
    X_train, X_test, y_train, y_test = ml_preprocessing(X,y,variance=0.75,test_size=0.25,random_state=42)


    if classifier == "svm" :
        parameters_canditates= [
        {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},]
        estimator = svm.SVC()
    elif classifier == "rdf" :
        parameters_canditates=[{
        "criterion" : ["gini", "entropy"],
        "max_features" : ["auto", "sqrt", "log2"],
        "bootstrap" : [True, False]
        }]
        estimator = ExtraTreesClassifier()
    elif classifier == "mlp":
        parameters_canditates =[
        {"activation":["identity", "logistic", "tanh", "relu"],
        "solver":["lbfgs","sgd","adam"],"alpha":[1e-05],"hidden_layer_sizes":[(5,2)],"random_state":[1]},
        ]
        estimator = MLPClassifier()

    #grid search
    clf = GridSearchCV(estimator=estimator, param_grid=parameters_canditates, n_jobs=-1)
    #fitting the model
    clf.fit(X_train, y_train)

    # Save model
    my_saver = Saver()
    my_saver.save(clf, "./trained_models", nom_du_model+"_model")
    #clf = my_saver.load("./trained_models", nom_du_model+"_model")

    # Print out the results
    """
    print('Best score for training data:', clf.best_score_)
    print('Best `C`:',clf.best_estimator_.C)
    print('Best kernel:',clf.best_estimator_.kernel)
    print('Best `gamma`:',clf.best_estimator_.gamma)
    """
    # prediction of labels
    y_pred=clf.predict(X_test)

    # Print out the confusion matrix
    confusion = metrics.confusion_matrix(y_test, y_pred)

    theta = metrics.accuracy_score(y_pred, y_test)
    sns.heatmap(confusion.T, square=True, annot=True, fmt='d', cbar=False)
    plt.title("Accuracy score %.2f" % theta)
    plt.xlabel('true label')
    plt.ylabel('predicted label')
    plt.savefig("./trained_models/accuracy_"+nom_du_model+"_model.png")

#trainModel("fruits",classifier="svm")
