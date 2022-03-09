# Stroke-Prediction

**Motive:** According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. This data is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.
* Built a **Logistic Regression** model with AUC of 0.82

## Code and Resources Used 
**Python Version:** 3.7  

**Packages:** pandas, numpy, sklearn, matplotlib, seaborn

**Data:** The dataset is taken from [Kaggle](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)

## Kaggle link for the project
* You also can view this project on [Kaggle](https://www.kaggle.com/ruthvikpvs/stroke-data-analysis-and-prediction)

## Exploratory Data Analysis
Looked into all the features of the data and did Uni-variate and Bi-variate and Multi-variate analysis on the data in relation to Stroke. One of the plots from the EDA can be seen in the pictures below.

![alt text](https://github.com/ricky1435/Stroke-Prediction/blob/main/Work%20type%20and%20stroke.png "Relation between Work type and Stroke Occurence")

## Data Preprocesing
* Removed all unnecessary columns
* Transformed all the categorical features into numerical ones using [One Hot Encoding](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
* Standardized the numerical features using sklearns StandardScaler
* The dataset was **heavily imbalanced** so I used [SMOTE](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/) to oversample the occurence of stroke and to balance the dataset.

## Model Building

I tried three different models and evaluated them using AUC(Area under the Curve). AUC is better measure of classifier performance than accuracy because it does not bias on size of test or evaluation data.

The three Models are:
*	**Logistic Regression** – Because the target feature is a binary classifier
* **Decisions Tree Classifier**
* **Random Forest Classifier**

## Model Performance
As I am considering AUC as my measure of model performance, **Logistic Regression** model performed way better than the other 2 models.

*	**Logistic Regression** – AUC: 0.82
* **Decisions Tree Classifier** - AUC: 0.55
* **Random Forest Classifier** - AUC: 0.76

