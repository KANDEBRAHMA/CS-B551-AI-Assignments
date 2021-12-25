# a4
Skeleton code for Assignment 4

### Part 1: K-Nearest Neighbors Classification

In machine learning world, K-Nearest Neighbors Classification model has prominent role.
My approach to this problem is there are two different metrics used to calculate distance for the features of the dataset.
    * Manhattan distance
        * Manhattan distance is calculated as the sum of the absolute differences between the two vectors.
    * Eucledian Distance
        * Eucledian Distance is calculated from the Cartesian vectors of the datapoints using the Pythagorean theorem.
    
* Fitting the train dataset
    * I have encorporated data features along with respective target class for better access later.

* Predicting the target class for test dataset:
    * For each datapoint in test:
        * I have calculated distance based on the metrics provided for all datapoints in the train dataset.
        * From all the distances we got, taking the k-neighbors with least distance along with their target class.
            * If the distance parameter is uniform, we rank them uniformly and return most occurred target class among them and predict that this datapoint assign to that particular target class.
            * If the distance paramter is distance, we assigns weights proportional to the inverse of the distance from the test sample to each neighbor.
                * After the assigning weights in above fashion, we sum of all the weights for a class variable and assign the datapoint to target class that has highest weight.

### Part 2: Multilayer Perceptron Classification

In machine learning, the field of artificial neural networks is often just called neural networks or multilayer perceptrons.

* Fitting the Train Dataset:
    * Randomly initializing hidden weights in the shape of(length of features,number of neurons in hidden layer).
    * Randomly initializing output weights in the shape of(number of neurons in hidden layer, number of target classes).
    * Forward Propagation:
        * We calculate the dot product of features and hidden weights and pass them through the specified activation function and store them weights of hidden layer neurons.
        * Then, we calculate the dot product of hidden layer neurons with output weights and pass them through the specified activation and softmax the result and store them as weights of output layer neurons.
        * Once we get all the weights we call backpropogation function.
    
    * Backward Propagation:
        * Calculate error in output layer
        * Update all weight between hidden and output layer
        * Calculate error in hidden layer
        * Update all weight between hidden and output layer

    We will stop calling backpropagation once the error was minimum.

    So, after the forward and backward propagation on the datapoints in the train dataset we get the updated weights that we can use for predicting the target class for test data points.

* Predicting the Class for test data set:
    * Perform forward propagation with updated weights and the weights having maximum probability at the output layer will the target class for that datapoint.

* Different Activations functions used are:
    * Sigmoid 
    * Tanh
    * Identity 
    * Relu

    Reference is taken from https://cs230.stanford.edu/files/C1M3.pdf

    * One hot encoding:
        * Creating a numpy array with zeros of shape(size of dataset,unique target classes)
        * Then by iterating over targets we update numpy array with specified target column with one.