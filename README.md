# "Timeseries Analysis and Prediction"
BEng Computer and Electronic Systems Final Project (University of Strathclyde).

Time-series prediction using machine learning algorithms on Scottish River levels
around Glasgow.

## Part One
First part of the project included designing and implementing PostgreSQL database
for storing river level and weather information data.

This simple application was implemented in Flask - Python micro-framework.
The data was collected from SEPA (Scottish Environmental Protection Agency) and
OpenWeatherMap API.

Whole code for this part is available in data_collecting_app folder.

## Part Two
Part two involved investigating and implementing number of Machine Learning algorithms.

The problem was represented as a regression problem and performance of three
different algorithms was compared:

- Recurrent Neural Networks
- Support Vector Regression
- Gaussian Process Regression

Algorithms were implemented in Python using the standard scientific stack, details
can be found in the machine_learning folder or in the Dissertation.

## Remaining Content
This repository also contains a poster that was presented in the initial stage
of the project. The poster focuses on some initial assumption of the project and
it's timeline.

Lastly, the dissertation (final report) is included for more detailed description
of the work performed for the project.
