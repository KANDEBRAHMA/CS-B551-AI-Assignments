# k_nearest_neighbors.py: Machine learning implementation of a K-Nearest Neighbors classifier from scratch.
#
# Submitted by: [enter your full name here] -- [enter your IU username here]
#
# Based on skeleton code by CSCI-B 551 Fall 2021 Course Staff

import numpy as np
from utils import euclidean_distance, manhattan_distance


class KNearestNeighbors:
    """
    A class representing the machine learning implementation of a K-Nearest Neighbors classifier from scratch.

    Attributes:
        n_neighbors
            An integer representing the number of neighbors a sample is compared with when predicting target class
            values.

        weights
            A string representing the weight function used when predicting target class values. The possible options are
            {'uniform', 'distance'}.

        _X
            A numpy array of shape (n_samples, n_features) representing the input data used when fitting the model and
            predicting target class values.

        _y
            A numpy array of shape (n_samples,) representing the true class values for each sample in the input data
            used when fitting the model and predicting target class values.

        _distance
            An attribute representing which distance metric is used to calculate distances between samples. This is set
            when creating the object to either the euclidean_distance or manhattan_distance functions defined in
            utils.py based on what argument is passed into the metric parameter of the class.

    Methods:
        fit(X, y)
            Fits the model to the provided data matrix X and targets y.

        predict(X)
            Predicts class target values for the given test data matrix X using the fitted classifier model.
    """
    def getclass(self,n_distances,weights):
        class_dict = {}
        n_dist = []
        for state in n_distances:
            n_dist.append(state[0])
            if state[0] in class_dict:
                class_dict[state[0]] += 1/state[1]
            else:
                if state[1]> 0:
                    class_dict[state[0]] = 1./state[1]
                class_dict[state[0]] = 0
        if weights == 'distance':
            return max(class_dict,key=class_dict.get)
        elif weights == 'uniform':
            return max(n_dist,key=n_dist.count)


    def getdistances(self,test_vector,n_neighbor,weights):
        dist = []
        for i in self._X:
            dist.append((int(i[-1]),self._distance(i[:-1],test_vector)))
        dist.sort(key = lambda dist: dist[1])
        return self.getclass(dist[:n_neighbor],weights)

    def __init__(self, n_neighbors = 5, weights = 'uniform', metric = 'l2'):
        # Check if the provided arguments are valid
        if weights not in ['uniform', 'distance'] or metric not in ['l1', 'l2'] or not isinstance(n_neighbors, int):
            raise ValueError('The provided class parameter arguments are not recognized.')

        # Define and setup the attributes for the KNearestNeighbors model object
        self.n_neighbors = n_neighbors
        self.weights = weights
        self._X = None
        self._y = None
        self._distance = euclidean_distance if metric == 'l2' else manhattan_distance

    def fit(self, X, y):
        """
        Fits the model to the provided data matrix X and targets y.

        Args:
            X: A numpy array of shape (n_samples, n_features) representing the input data.
            y: A numpy array of shape (n_samples,) representing the true class values for each sample in the input data.

        Returns:
            None.
        """
        self._y = y
        self._X = np.insert(X,X[0].shape[0],self._y,axis = 1)

        #raise NotImplementedError('This function must be implemented by the student.')

    def predict(self, X):
        """
        Predicts class target values for the given test data matrix X using the fitted classifier model.

        Args:
            X: A numpy array of shape (n_samples, n_features) representing the test data.

        Returns:
            A numpy array of shape (n_samples,) representing the predicted target class values for the given test data.
        """
        final_target_variables = []
        for test_vector in X:
            final_target_variables.append(self.getdistances(test_vector,self.n_neighbors,self.weights))
        return np.array(final_target_variables)


        #raise NotImplementedError('This function must be implemented by the student.')
