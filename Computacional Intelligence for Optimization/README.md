# Computacional Intelligence for Optmization 


*Problem type:* Apply a genetic algorithm (GA) to solve an optimization problem 


## General Context 
Drug discovery is often a very laborious and expensive process, namely when trying to predict
pharmacological characteristics of new compounds, such as toxicity or bioavailability. Starting from a dataset of known chemical compounds bioavailability, the goal is to generalize by finding a function that makes a prediction of the
bioavailability with the minimum error possible.
To tackle the problem of predicting bioavailability, we have implemented a multiple linear
regression, as shown in figure 1, with genetic algorithms (GAs) as the optimization function, in order to
find the coefficients (slopes) values of each molecular descriptor, that minimizes the error between the
prediction and the compared target. As a fitness function, we have used the root mean square (RMSE),
which implementation is detailed later in this document.
Our dataset is composed of 359 rows and 242 columns. Each row represents a different
pharmacological compound. The first 241 columns are the different molecular descriptors, and the last
one is the bioavailability of the compound, which corresponds in the model defined in the figure 1, by
the independent variables (Xi) and the dependent variable (Y), respectively.


## Project Overview
1. Implement some selection operators and some mutation and crossover operators
