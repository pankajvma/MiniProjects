# Bank Marketing - Subscription Prediction

### Marketing
The action or business of promoting and selling products or services, including market research and advertising.

### Term deposit
Term Deposits are one of the best investment options for people who are looking for a stable and safe return on their investments. In Term Deposits, the sum of money is kept for a fixed maturity and the depositor is not allowed to withdraw this sum till the end of the maturity period. That is why they are called as Term Deposits because they are kept up to a particular term.

## Data Set information

The data is related with direct marketing campaigns of a Portuguese banking institution. 
The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

The dataset bank-additional-full.csv contains all examples (45211) with 17 features, ordered by date (from May 2008 to November 2010), very close to the data analyzed in [Moro et al., 2014]
### Attribute information
#### Input Variables
##### Bank Client Data
**age:** (numeric)  
**job:** type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')  
**marital:** marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)  
**education:** (categorical: primary, secondary, tertiary and unknown)  
**default:** has credit in default? (categorical: 'no','yes')  
**balance:** average yearly balance, in euros (numeric)   
**housing:** has housing loan? (categorical: 'no','yes')  
**loan:** has personal loan? (categorical: 'no','yes')  
##### Related with the last contact of the current campaign:
**contact:** contact communication type (categorical: 'cellular','telephone')  
**day:** last contact day of the month (numeric)  
**month:** last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')  
**duration:** last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known.
##### Other attributes:
**campaign:** number of contacts performed during this campaign and for this client (numeric, includes last contact)  
**pdays:** number of days that passed by after the client was last contacted from a previous campaign (numeric; -1 means client was not previously contacted)  
**previous:** number of contacts performed before this campaign and for this client (numeric)  
**poutcome:** outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')  

#### Output variable (desired target):
**y:** has the client subscribed a term deposit? (binary: 'yes','no')

**Note:** It is mentioned in the Data Set information that thee are no missing values, but still we will run some test forr the same.

## Data Exploration
### import pandas and numpy for Data Analysis


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

import time

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.decomposition import PCA
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

warnings.filterwarnings('ignore')
%matplotlib inline 

df = pd.read_csv('./bank/bank-full.csv')
print('Total samples: ', len(df))
```

    Total samples:  45211
    

### Missing Data


```python
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
```


    
![png](output_7_0.png)
    



```python
df.isnull().sum()
```




    age          0
    job          0
    marital      0
    education    0
    default      0
    balance      0
    housing      0
    loan         0
    contact      0
    day          0
    month        0
    duration     0
    campaign     0
    pdays        0
    previous     0
    poutcome     0
    y            0
    dtype: int64



There are no null values.

### Overview of available data


```python
df.describe()
# df[df['pdays'] != -1].count()
# df[df['previous'] != 0].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>balance</th>
      <th>day</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>45211.000000</td>
      <td>45211.000000</td>
      <td>45211.000000</td>
      <td>45211.000000</td>
      <td>45211.000000</td>
      <td>45211.000000</td>
      <td>45211.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>40.936210</td>
      <td>1362.272058</td>
      <td>15.806419</td>
      <td>258.163080</td>
      <td>2.763841</td>
      <td>40.197828</td>
      <td>0.580323</td>
    </tr>
    <tr>
      <th>std</th>
      <td>10.618762</td>
      <td>3044.765829</td>
      <td>8.322476</td>
      <td>257.527812</td>
      <td>3.098021</td>
      <td>100.128746</td>
      <td>2.303441</td>
    </tr>
    <tr>
      <th>min</th>
      <td>18.000000</td>
      <td>-8019.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>33.000000</td>
      <td>72.000000</td>
      <td>8.000000</td>
      <td>103.000000</td>
      <td>1.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>39.000000</td>
      <td>448.000000</td>
      <td>16.000000</td>
      <td>180.000000</td>
      <td>2.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>48.000000</td>
      <td>1428.000000</td>
      <td>21.000000</td>
      <td>319.000000</td>
      <td>3.000000</td>
      <td>-1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>95.000000</td>
      <td>102127.000000</td>
      <td>31.000000</td>
      <td>4918.000000</td>
      <td>63.000000</td>
      <td>871.000000</td>
      <td>275.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Adding a new column by name 'subscribed' to store the value '1' if subscribed, else '0' 
df['subscribed'] = (df.y == 'yes').astype('int')
df.drop('y', axis=1, inplace=True)
```


```python
# sns.pairplot(df, hue='subscribed')
```

#### Quick Observations on Numerical Data
- Total available data count is 45211 entries  
- Mean Age of the contacted customers is 41 years (Approx)  
- Mininmum Age of the contacted customers is 18 years
- Maximum Age of the contacted customers is 95 years
- Mean of call durationss is 258 seconds  
- Mean account balance for the customers 1362 euros  
- More than 75% of the the values in the column 'pdays' are set to -1. We know from our attribute informations that -1 means client was not previously contacted
- Just similar to the last observation more than 75% of the values inside the columns 'previous' which indicates how many times the customer was contacted before this campaign is 0 i. e. the customer is being contactedd forr the very first time.
- The values '-1' and '0' of the columns 'pdays' and 'previous' respectively are actually pointing towards the same fact.
- Because of the significant redundency of '0' and '-1' in their respective columns We might drop them later if their fluctuations do not show any relation with the outcome i. e. column 'y'.


```python
df.describe(include='object')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>job</th>
      <th>marital</th>
      <th>education</th>
      <th>default</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>month</th>
      <th>poutcome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
      <td>45211</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>12</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>12</td>
      <td>4</td>
    </tr>
    <tr>
      <th>top</th>
      <td>blue-collar</td>
      <td>married</td>
      <td>secondary</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>cellular</td>
      <td>may</td>
      <td>unknown</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>9732</td>
      <td>27214</td>
      <td>23202</td>
      <td>44396</td>
      <td>25130</td>
      <td>37967</td>
      <td>29285</td>
      <td>13766</td>
      <td>36959</td>
    </tr>
  </tbody>
</table>
</div>



#### Quick Observation on Categorical Data
- Out of 45211, more than 44000 i. e. 97.3% customers do not have a credit. The number of customers with credit are negligible when compared to it. We might drop this column later.


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 45211 entries, 0 to 45210
    Data columns (total 17 columns):
     #   Column      Non-Null Count  Dtype 
    ---  ------      --------------  ----- 
     0   age         45211 non-null  int64 
     1   job         45211 non-null  object
     2   marital     45211 non-null  object
     3   education   45211 non-null  object
     4   default     45211 non-null  object
     5   balance     45211 non-null  int64 
     6   housing     45211 non-null  object
     7   loan        45211 non-null  object
     8   contact     45211 non-null  object
     9   day         45211 non-null  int64 
     10  month       45211 non-null  object
     11  duration    45211 non-null  int64 
     12  campaign    45211 non-null  int64 
     13  pdays       45211 non-null  int64 
     14  previous    45211 non-null  int64 
     15  poutcome    45211 non-null  object
     16  subscribed  45211 non-null  int32 
    dtypes: int32(1), int64(7), object(9)
    memory usage: 5.7+ MB
    


```python
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>job</th>
      <th>marital</th>
      <th>education</th>
      <th>default</th>
      <th>balance</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>day</th>
      <th>month</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
      <th>poutcome</th>
      <th>subscribed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>58</td>
      <td>management</td>
      <td>married</td>
      <td>tertiary</td>
      <td>no</td>
      <td>2143</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>261</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44</td>
      <td>technician</td>
      <td>single</td>
      <td>secondary</td>
      <td>no</td>
      <td>29</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>151</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33</td>
      <td>entrepreneur</td>
      <td>married</td>
      <td>secondary</td>
      <td>no</td>
      <td>2</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>76</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47</td>
      <td>blue-collar</td>
      <td>married</td>
      <td>unknown</td>
      <td>no</td>
      <td>1506</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>92</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>33</td>
      <td>unknown</td>
      <td>single</td>
      <td>unknown</td>
      <td>no</td>
      <td>1</td>
      <td>no</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>198</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35</td>
      <td>management</td>
      <td>married</td>
      <td>tertiary</td>
      <td>no</td>
      <td>231</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>139</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>28</td>
      <td>management</td>
      <td>single</td>
      <td>tertiary</td>
      <td>no</td>
      <td>447</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>217</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>42</td>
      <td>entrepreneur</td>
      <td>divorced</td>
      <td>tertiary</td>
      <td>yes</td>
      <td>2</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>380</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>58</td>
      <td>retired</td>
      <td>married</td>
      <td>primary</td>
      <td>no</td>
      <td>121</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>50</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>43</td>
      <td>technician</td>
      <td>single</td>
      <td>secondary</td>
      <td>no</td>
      <td>593</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may</td>
      <td>55</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (45211, 17)




```python
df.groupby('subscribed').size()
```




    subscribed
    0    39922
    1     5289
    dtype: int64



**Quick Observation** 
- 5289 Out of 45211 contacted customers subscribed


```python
df.keys()
```




    Index(['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
           'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
           'previous', 'poutcome', 'subscribed'],
          dtype='object')




```python
# By calculating the prevalance we are checking that out of total customers how many customer have actually suscribed 
def calculate_prevalance(subscribed):
    total_customers = len(df)
    positive_prevalance = sum(subscribed)/total_customers
    positive_prevalance = round(positive_prevalance, 3)
    print(f"The positive prevalnce is: {positive_prevalance}")
    
calculate_prevalance(df['subscribed'].values)
```

    The positive prevalnce is: 0.117
    

### Exploring unique values
- Checking if there are any unnecessary columns
- Finding categorical varieties


```python
df[list(df.columns)[:10]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>job</th>
      <th>marital</th>
      <th>education</th>
      <th>default</th>
      <th>balance</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>58</td>
      <td>management</td>
      <td>married</td>
      <td>tertiary</td>
      <td>no</td>
      <td>2143</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44</td>
      <td>technician</td>
      <td>single</td>
      <td>secondary</td>
      <td>no</td>
      <td>29</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33</td>
      <td>entrepreneur</td>
      <td>married</td>
      <td>secondary</td>
      <td>no</td>
      <td>2</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47</td>
      <td>blue-collar</td>
      <td>married</td>
      <td>unknown</td>
      <td>no</td>
      <td>1506</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>33</td>
      <td>unknown</td>
      <td>single</td>
      <td>unknown</td>
      <td>no</td>
      <td>1</td>
      <td>no</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[list(df.columns)[10:]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
      <th>poutcome</th>
      <th>subscribed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>may</td>
      <td>261</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>may</td>
      <td>151</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>may</td>
      <td>76</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>may</td>
      <td>92</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>may</td>
      <td>198</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (45211, 17)




```python
# check unique values for every column
for feature in df.columns:
    
    # get a list of unique values
    unique_values = df[feature].unique()
    print(f'{feature} : {len(unique_values)} unique values')
```

    age : 77 unique values
    job : 12 unique values
    marital : 3 unique values
    education : 4 unique values
    default : 2 unique values
    balance : 7168 unique values
    housing : 2 unique values
    loan : 2 unique values
    contact : 3 unique values
    day : 31 unique values
    month : 12 unique values
    duration : 1573 unique values
    campaign : 48 unique values
    pdays : 559 unique values
    previous : 41 unique values
    poutcome : 4 unique values
    subscribed : 2 unique values
    


```python
# for every column
check_value_occerrence = []
for feature in df.columns:
    
    # get a list of unique values
    unique_values = df[feature].unique()
    number_of_unique_values = len(unique_values)
    if number_of_unique_values < 30:
        print(f'{feature} : {number_of_unique_values}\n{unique_values}')
        check_value_occerrence.append(feature)
```

    job : 12
    ['management' 'technician' 'entrepreneur' 'blue-collar' 'unknown'
     'retired' 'admin.' 'services' 'self-employed' 'unemployed' 'housemaid'
     'student']
    marital : 3
    ['married' 'single' 'divorced']
    education : 4
    ['tertiary' 'secondary' 'unknown' 'primary']
    default : 2
    ['no' 'yes']
    housing : 2
    ['yes' 'no']
    loan : 2
    ['no' 'yes']
    contact : 3
    ['unknown' 'cellular' 'telephone']
    month : 12
    ['may' 'jun' 'jul' 'aug' 'oct' 'nov' 'dec' 'jan' 'feb' 'mar' 'apr' 'sep']
    poutcome : 4
    ['unknown' 'failure' 'other' 'success']
    subscribed : 2
    [0 1]
    

### Numerical Features


```python
numerical_data = [data for data in df.dtypes[df.dtypes == 'int64'].index]
numerical_data
```




    ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']




```python
df[numerical_data].isnull().sum()
```




    age         0
    balance     0
    day         0
    duration    0
    campaign    0
    pdays       0
    previous    0
    dtype: int64




```python
df[numerical_data].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>balance</th>
      <th>day</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>58</td>
      <td>2143</td>
      <td>5</td>
      <td>261</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44</td>
      <td>29</td>
      <td>5</td>
      <td>151</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33</td>
      <td>2</td>
      <td>5</td>
      <td>76</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47</td>
      <td>1506</td>
      <td>5</td>
      <td>92</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>33</td>
      <td>1</td>
      <td>5</td>
      <td>198</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#creating distribution and box plots
for col in numerical_data : 
    plt.figure(figsize=(12,4))
    
    plt.subplot(1,2,1)
    sns.distplot(df[col])
    plt.xlabel(col)
    plt.ylabel('Density')
    
    plt.subplot(1,2,2)
    sns.boxplot(x='subscribed', y = col, data =df, showmeans = True)
    plt.xlabel('Subscribed')
    plt.ylabel(col)
    
    plt.show()

# fig, axes = plt.subplots(nrows = len(numerical_data)//2, ncols = 2, figsize= (16, 12))
#  plt.tight_layout()

# for col in numerical_data : 
    
#     plt.subplot(1,2,1)
#     sns.distplot(df[col])
#     plt.xlabel(col)
#     plt.ylabel('Density')
    
#     plt.subplot(1,2,2)
#     sns.boxplot(x='subscribed', y = col, data =df, showmeans = True)
#     plt.xlabel('Subscribed')
#     plt.ylabel(col)
    
#     plt.show()
    



```


    
![png](output_34_0.png)
    



    
![png](output_34_1.png)
    



    
![png](output_34_2.png)
    



    
![png](output_34_3.png)
    



    
![png](output_34_4.png)
    



    
![png](output_34_5.png)
    



    
![png](output_34_6.png)
    


**Observation:** 
- From the Density and boxplot shown above we can say that the customerrs with longer call durations are more likely to subscribe for the term deposit
- Most of the customers who actually subscribed were contacted for the very first time
- Except for the column of age and days, all the other numerical features seems to be left skewed.


```python
plt.rcParams.update({'font.size': 11})
for col in numerical_data : 
    if col not in ['balance', 'duration', 'pdays']:
        plt.figure(figsize=(20,10))
        plt.subplot().patch.set_visible(False)
        sns.countplot(x = df[col], data = df)
        plt.xlabel(col.title())
        plt.ylabel('Count')

        plt.show()
```


    
![png](output_36_0.png)
    



    
![png](output_36_1.png)
    



    
![png](output_36_2.png)
    



    
![png](output_36_3.png)
    


Balance, duration, pdays can be stored in bins


```python
plt.subplots(figsize=(20,5)) 
plt.rcParams.update({'font.size': 12})
    
plt.subplot(1, 2, 1)
sns.histplot(x = df['balance'], data = df)
plt.ylabel('Count')

plt.subplot(1, 2, 2)
sns.histplot(x = df['duration'], data = df)
plt.ylabel('Count')
plt.show()

plt.subplot()
sns.histplot(x = df['pdays'], data = df)
plt.ylabel('Count')

plt.show()
```


    
![png](output_38_0.png)
    



    
![png](output_38_1.png)
    


**Observations**
- The maximum targeted age group is 30 to 37 Years old with more than 2000 people of age 32
- More than 2500 people were contacted on 20th day of the month
- more than 17500 customers were contacted only once during the campaign

## Categorical Features

Categorical variables are non-numeric data such as job and education. To turn these non-numerical data into variables, the simplest thing is to use a technique called one-hot encoding, which will be explained below.


```python
object_data = [data for data in df.dtypes[df.dtypes == 'object'].index]
object_data
```




    ['job',
     'marital',
     'education',
     'default',
     'housing',
     'loan',
     'contact',
     'month',
     'poutcome']



### Graphical Representation of Categorical Features


```python
plt.rcParams.update({'font.size': 11})

plt.figure(figsize=(16,4))
plt.subplot().patch.set_visible(False)
sns.countplot(x = df['job'], data = df)
plt.xlabel('Job')
plt.ylabel('Count')

plt.rcParams.update({'font.size': 16})

for col in range(1, len(object_data) - 1, 2): 
    plt.figure(figsize=(16,4))
    col_index = col
    column_name = object_data[col_index]
    col_index += 1
    plt.subplot(1, 2, 1).patch.set_visible(False)
    sns.countplot(x = df[column_name], data = df)
    plt.xlabel(column_name.title())
    plt.ylabel('Count')
                 
    plt.subplot(1, 2, 2)
    column_name = object_data[col_index]
    sns.countplot(x = df[column_name], data = df)
    plt.xlabel(column_name.title())
    plt.ylabel('Count')
    
    plt.show()
```


    
![png](output_43_0.png)
    



    
![png](output_43_1.png)
    



    
![png](output_43_2.png)
    



    
![png](output_43_3.png)
    



    
![png](output_43_4.png)
    


**Observations**
- We can see the most of the targeted customers are either in management or are blue-coller (9000+ each)
- More than 25000 of the customers are married
- 20000+ customers have received secondary education
- 40000+ customers do not have any credit
- Around 25000+ have taken a housing loan
- 35000+ People do not have any kind of personal loan
- Around 30000+ people were contacted over cellular phones
- Most of the customers were contacted in the month of May
- Most of the people are being contacted for the very first time hence most of the values in the column poutcomee are unknown
- 5289 Out of 45211 contacted customers subscribed


```python
plt.rcParams.update({'font.size': 11})

plt.figure(figsize=(16,4))
plt.subplot().patch.set_visible(False)
sns.countplot(x = df['job'], hue='subscribed', data = df)
plt.xlabel('Job')
plt.ylabel('Count')

plt.rcParams.update({'font.size': 16})

# plt.show()

for col in range(1, len(object_data) - 1, 2): 
    plt.figure(figsize=(16,4))
    col_index = col
    column_name = object_data[col_index]
    col_index += 1
    plt.subplot(1, 2, 1).patch.set_visible(False)
    sns.countplot(x=df[column_name],hue='subscribed',data=df)
    
    column_name = object_data[col_index]
    plt.subplot(1, 2, 2).patch.set_visible(False)
    sns.countplot(x=df[column_name],hue='subscribed',data=df)
    
#     plt.show()
```


    
![png](output_45_0.png)
    



    
![png](output_45_1.png)
    



    
![png](output_45_2.png)
    



    
![png](output_45_3.png)
    



    
![png](output_45_4.png)
    



```python
for col in object_data:
    print(df.groupby(['subscribed', col]).size())
```

    subscribed  job          
    0           admin.           4540
                blue-collar      9024
                entrepreneur     1364
                housemaid        1131
                management       8157
                retired          1748
                self-employed    1392
                services         3785
                student           669
                technician       6757
                unemployed       1101
                unknown           254
    1           admin.            631
                blue-collar       708
                entrepreneur      123
                housemaid         109
                management       1301
                retired           516
                self-employed     187
                services          369
                student           269
                technician        840
                unemployed        202
                unknown            34
    dtype: int64
    subscribed  marital 
    0           divorced     4585
                married     24459
                single      10878
    1           divorced      622
                married      2755
                single       1912
    dtype: int64
    subscribed  education
    0           primary       6260
                secondary    20752
                tertiary     11305
                unknown       1605
    1           primary        591
                secondary     2450
                tertiary      1996
                unknown        252
    dtype: int64
    subscribed  default
    0           no         39159
                yes          763
    1           no          5237
                yes           52
    dtype: int64
    subscribed  housing
    0           no         16727
                yes        23195
    1           no          3354
                yes         1935
    dtype: int64
    subscribed  loan
    0           no      33162
                yes      6760
    1           no       4805
                yes       484
    dtype: int64
    subscribed  contact  
    0           cellular     24916
                telephone     2516
                unknown      12490
    1           cellular      4369
                telephone      390
                unknown        530
    dtype: int64
    subscribed  month
    0           apr       2355
                aug       5559
                dec        114
                feb       2208
                jan       1261
                jul       6268
                jun       4795
                mar        229
                may      12841
                nov       3567
                oct        415
                sep        310
    1           apr        577
                aug        688
                dec        100
                feb        441
                jan        142
                jul        627
                jun        546
                mar        248
                may        925
                nov        403
                oct        323
                sep        269
    dtype: int64
    subscribed  poutcome
    0           failure      4283
                other        1533
                success       533
                unknown     33573
    1           failure       618
                other         307
                success       978
                unknown      3386
    dtype: int64
    

**Obeservations**
- The customerrs in job category 'retired' have shown higher interest in the term deposit as compared to the others.
- Customers with a tertiary level of education were more like to subscribe for the term deposit.
- The people who do not have a credit have shown interest in the term deposit.
- The people who do not have a housing loan have shown relatively higher interest in the term deposit.
- Customers who were contacted during the month of March, September, December, and October repectively have mostly subscribed to the term deposit.


```python
df['education'].replace('unknown',0, inplace=True)
df['education'].replace('primary',1, inplace=True)
df['education'].replace('secondary',2, inplace=True)
df['education'].replace('tertiary',3, inplace=True)
```


```python
df['education'].dtypes
```




    dtype('int64')




```python
df.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>education</th>
      <th>balance</th>
      <th>day</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
      <th>subscribed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>age</th>
      <td>1.000000</td>
      <td>-0.173615</td>
      <td>0.097783</td>
      <td>-0.009120</td>
      <td>-0.004648</td>
      <td>0.004760</td>
      <td>-0.023758</td>
      <td>0.001288</td>
      <td>0.025155</td>
    </tr>
    <tr>
      <th>education</th>
      <td>-0.173615</td>
      <td>1.000000</td>
      <td>0.050572</td>
      <td>0.021661</td>
      <td>0.002554</td>
      <td>0.000194</td>
      <td>0.007092</td>
      <td>0.025295</td>
      <td>0.051341</td>
    </tr>
    <tr>
      <th>balance</th>
      <td>0.097783</td>
      <td>0.050572</td>
      <td>1.000000</td>
      <td>0.004503</td>
      <td>0.021560</td>
      <td>-0.014578</td>
      <td>0.003435</td>
      <td>0.016674</td>
      <td>0.052838</td>
    </tr>
    <tr>
      <th>day</th>
      <td>-0.009120</td>
      <td>0.021661</td>
      <td>0.004503</td>
      <td>1.000000</td>
      <td>-0.030206</td>
      <td>0.162490</td>
      <td>-0.093044</td>
      <td>-0.051710</td>
      <td>-0.028348</td>
    </tr>
    <tr>
      <th>duration</th>
      <td>-0.004648</td>
      <td>0.002554</td>
      <td>0.021560</td>
      <td>-0.030206</td>
      <td>1.000000</td>
      <td>-0.084570</td>
      <td>-0.001565</td>
      <td>0.001203</td>
      <td>0.394521</td>
    </tr>
    <tr>
      <th>campaign</th>
      <td>0.004760</td>
      <td>0.000194</td>
      <td>-0.014578</td>
      <td>0.162490</td>
      <td>-0.084570</td>
      <td>1.000000</td>
      <td>-0.088628</td>
      <td>-0.032855</td>
      <td>-0.073172</td>
    </tr>
    <tr>
      <th>pdays</th>
      <td>-0.023758</td>
      <td>0.007092</td>
      <td>0.003435</td>
      <td>-0.093044</td>
      <td>-0.001565</td>
      <td>-0.088628</td>
      <td>1.000000</td>
      <td>0.454820</td>
      <td>0.103621</td>
    </tr>
    <tr>
      <th>previous</th>
      <td>0.001288</td>
      <td>0.025295</td>
      <td>0.016674</td>
      <td>-0.051710</td>
      <td>0.001203</td>
      <td>-0.032855</td>
      <td>0.454820</td>
      <td>1.000000</td>
      <td>0.093236</td>
    </tr>
    <tr>
      <th>subscribed</th>
      <td>0.025155</td>
      <td>0.051341</td>
      <td>0.052838</td>
      <td>-0.028348</td>
      <td>0.394521</td>
      <td>-0.073172</td>
      <td>0.103621</td>
      <td>0.093236</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.subplots(figsize=(10,5)) 
sns.heatmap(df.corr(), cbar=True, cmap="RdBu_r", linewidths=1)
plt.title("Correlation Matrix", fontsize=18)
plt.show()
```


    
![png](output_51_0.png)
    



```python
# frequency of particular value in a columns where 
for column in check_value_occerrence:
    print(f'{df.groupby(column).size()}\n')
```

    job
    admin.           5171
    blue-collar      9732
    entrepreneur     1487
    housemaid        1240
    management       9458
    retired          2264
    self-employed    1579
    services         4154
    student           938
    technician       7597
    unemployed       1303
    unknown           288
    dtype: int64
    
    marital
    divorced     5207
    married     27214
    single      12790
    dtype: int64
    
    education
    0     1857
    1     6851
    2    23202
    3    13301
    dtype: int64
    
    default
    no     44396
    yes      815
    dtype: int64
    
    housing
    no     20081
    yes    25130
    dtype: int64
    
    loan
    no     37967
    yes     7244
    dtype: int64
    
    contact
    cellular     29285
    telephone     2906
    unknown      13020
    dtype: int64
    
    month
    apr     2932
    aug     6247
    dec      214
    feb     2649
    jan     1403
    jul     6895
    jun     5341
    mar      477
    may    13766
    nov     3970
    oct      738
    sep      579
    dtype: int64
    
    poutcome
    failure     4901
    other       1840
    success     1511
    unknown    36959
    dtype: int64
    
    subscribed
    0    39922
    1     5289
    dtype: int64
    
    

## Feature Engineering

Feature Engineering is classifying features such as numerial and categorical into groups in order to deeply section and analyze the data.Here, we will create features for our predictive model. For each section, we will add new variables to the dataframe and then keep track of which columns of the dataframe we want to use as part of the predictive model features. We will break down this section into numerical and categorical features.


```python
df.dtypes
```




    age            int64
    job           object
    marital       object
    education      int64
    default       object
    balance        int64
    housing       object
    loan          object
    contact       object
    day            int64
    month         object
    duration       int64
    campaign       int64
    pdays          int64
    previous       int64
    poutcome      object
    subscribed     int32
    dtype: object




```python
# Check for missing values
df[object_data].isnull().sum()
```




    job          0
    marital      0
    education    0
    default      0
    housing      0
    loan         0
    contact      0
    month        0
    poutcome     0
    dtype: int64




```python
encoded_df = df.copy()
```


```python
for col in object_data:
    encoded_df[col] = df[col].astype('category')
    encoded_df[col+"_encoded"] = encoded_df[col].cat.codes
encoded_df.dtypes
```




    age                     int64
    job                  category
    marital              category
    education            category
    default              category
    balance                 int64
    housing              category
    loan                 category
    contact              category
    day                     int64
    month                category
    duration                int64
    campaign                int64
    pdays                   int64
    previous                int64
    poutcome             category
    subscribed              int32
    job_encoded              int8
    marital_encoded          int8
    education_encoded        int8
    default_encoded          int8
    housing_encoded          int8
    loan_encoded             int8
    contact_encoded          int8
    month_encoded            int8
    poutcome_encoded         int8
    dtype: object




```python
encoded_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>job</th>
      <th>marital</th>
      <th>education</th>
      <th>default</th>
      <th>balance</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>day</th>
      <th>...</th>
      <th>subscribed</th>
      <th>job_encoded</th>
      <th>marital_encoded</th>
      <th>education_encoded</th>
      <th>default_encoded</th>
      <th>housing_encoded</th>
      <th>loan_encoded</th>
      <th>contact_encoded</th>
      <th>month_encoded</th>
      <th>poutcome_encoded</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>58</td>
      <td>management</td>
      <td>married</td>
      <td>3</td>
      <td>no</td>
      <td>2143</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44</td>
      <td>technician</td>
      <td>single</td>
      <td>2</td>
      <td>no</td>
      <td>29</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>9</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33</td>
      <td>entrepreneur</td>
      <td>married</td>
      <td>2</td>
      <td>no</td>
      <td>2</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>47</td>
      <td>blue-collar</td>
      <td>married</td>
      <td>0</td>
      <td>no</td>
      <td>1506</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>33</td>
      <td>unknown</td>
      <td>single</td>
      <td>0</td>
      <td>no</td>
      <td>1</td>
      <td>no</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>11</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>45206</th>
      <td>51</td>
      <td>technician</td>
      <td>married</td>
      <td>3</td>
      <td>no</td>
      <td>825</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>17</td>
      <td>...</td>
      <td>1</td>
      <td>9</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>45207</th>
      <td>71</td>
      <td>retired</td>
      <td>divorced</td>
      <td>1</td>
      <td>no</td>
      <td>1729</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>17</td>
      <td>...</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>45208</th>
      <td>72</td>
      <td>retired</td>
      <td>married</td>
      <td>2</td>
      <td>no</td>
      <td>5715</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>17</td>
      <td>...</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2</td>
    </tr>
    <tr>
      <th>45209</th>
      <td>57</td>
      <td>blue-collar</td>
      <td>married</td>
      <td>2</td>
      <td>no</td>
      <td>668</td>
      <td>no</td>
      <td>no</td>
      <td>telephone</td>
      <td>17</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>45210</th>
      <td>37</td>
      <td>entrepreneur</td>
      <td>married</td>
      <td>2</td>
      <td>no</td>
      <td>2971</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>17</td>
      <td>...</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>45211 rows × 26 columns</p>
</div>




```python
encoded_df.columns
```




    Index(['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
           'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
           'previous', 'poutcome', 'subscribed', 'job_encoded', 'marital_encoded',
           'education_encoded', 'default_encoded', 'housing_encoded',
           'loan_encoded', 'contact_encoded', 'month_encoded', 'poutcome_encoded'],
          dtype='object')




```python
encoded_df.drop(object_data, axis=1, inplace=True)
encoded_df.columns
```




    Index(['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous',
           'subscribed', 'job_encoded', 'marital_encoded', 'education_encoded',
           'default_encoded', 'housing_encoded', 'loan_encoded', 'contact_encoded',
           'month_encoded', 'poutcome_encoded'],
          dtype='object')




```python
plt.subplots(figsize=(25,10)) 
sns.heatmap(encoded_df[['job_encoded', 'marital_encoded', 'education_encoded',
                        'default_encoded', 'housing_encoded', 'loan_encoded', 'contact_encoded',
                        'month_encoded', 'poutcome_encoded', 'subscribed']].corr(), cbar=True, cmap="RdBu_r",linewidths=1, annot=True)
plt.title("Correlation Matrix", fontsize=18)
# plt.show()
```




    Text(0.5, 1.0, 'Correlation Matrix')




    
![png](output_61_1.png)
    



```python
#defaut feature does not play imp role
print(encoded_df.groupby(['default_encoded']).size())
print(encoded_df.groupby(['subscribed','default_encoded']).size())
```

    default_encoded
    0    44396
    1      815
    dtype: int64
    subscribed  default_encoded
    0           0                  39159
                1                    763
    1           0                   5237
                1                     52
    dtype: int64
    


```python
print('10 most frequent values in the column "previous":')
print(encoded_df.groupby(['previous']).size()[:10])
print()
print("Data in previous column compared to the 'y':")
print(encoded_df.groupby(['subscribed','previous']).size())
```

    10 most frequent values in the column "previous":
    previous
    0    36954
    1     2772
    2     2106
    3     1142
    4      714
    5      459
    6      277
    7      205
    8      129
    9       92
    dtype: int64
    
    Data in previous column compared to the 'y':
    subscribed  previous
    0           0           33570
                1            2189
                2            1650
                3             848
                4             543
                            ...  
    1           26              1
                29              1
                30              1
                55              1
                58              1
    Length: 66, dtype: int64
    


```python
print(encoded_df.groupby(['pdays']).size())
print(encoded_df.groupby(['subscribed','pdays']).size())
```

    pdays
    -1      36954
     1         15
     2         37
     3          1
     4          2
            ...  
     838        1
     842        1
     850        1
     854        1
     871        1
    Length: 559, dtype: int64
    subscribed  pdays
    0           -1       33570
                 1           9
                 2          35
                 3           1
                 4           1
                         ...  
    1            804         1
                 805         1
                 828         1
                 842         1
                 854         1
    Length: 914, dtype: int64
    


```python
encoded_df.shape
```




    (45211, 17)



### Dropping non-related columns
- **default:** It has 44369 'no' values. It denotes that 44369 out of 45211 customers do not have a credit in default.
- **contact:** This column can't contribute anymore in our prediction as the standard meddium of communication is 'cellular' now.
- **month and day:** We can drop these two columns as they aren't showing any significant correlation with our target variable.
- **pdays and previous:** Most frequent values in these two columns are -1, and 0. both these values have a frequency of 36954 and are pointing towards the same  fact. We can drop both of them as they aren't showing any significant correlation with our target variable.
- **poutcome:** We will drop this column as it has 36959 'unknown' values, also it isn't showing any significant correlation with the target.


```python
df.drop(['default', 'contact', 'month', 'day', 'pdays', 'previous', 'poutcome'], axis=1, inplace= True)
```


```python
df.shape
```




    (45211, 10)




```python
print(f"Job Unknown: {df[df['job']=='unknown']['job'].count()}")
print(f"Education Unknown: {df[df['education']== 0]['education'].count()}")
print(f"Job and Education Unknown: {df[(df['job']=='unknown') & (df['education']== 0)]['education'].count()}")
print(f"Job or Education Unknown:{df[(df['job']=='unknown') | (df['education']== 0)]['education'].count()}")
```

    Job Unknown: 288
    Education Unknown: 1857
    Job and Education Unknown: 127
    Job or Education Unknown:2018
    

### Dropping rows with unknown values
- We are dropping the rows with 'unknown' as entry from the education and job column. Column 'education' has 1857, and 'job' has 288 unknown values.
- A total of 127 rows have 'unknown' entry in both the education and job column.
- Dropping these entries will removes a total of 2018 values from our dataframe.


```python
df.drop(df[df['job']=='unknown'].index, inplace=True)
# in the education column we have asssigned the value 0 to 'unknown'
df.drop(df[df['education']==0].index, inplace=True)
```


```python
df.shape
```




    (43193, 10)




```python
# Checking calls with duration 0
df[(df['duration']==0)]['duration'].count()
```




    3




```python
# Checking if any customer with cal duration 0 has subscribed for the term deposit
df[(df['duration']==0) & (df['subscribed']) == 1]['duration'].count()
```




    0



- As expected, none of the cusomers with call duration 0 subscribed for the term deposit.  
Hence we can drop these entries.


```python
df.drop(df[df['duration']==0].index, inplace=True)
df.shape
```




    (43190, 10)




```python
# Updating Object data list
object_data = [data for data in df.dtypes[df.dtypes == 'object'].index]
object_data
```




    ['job', 'marital', 'housing', 'loan']




```python
def remove_outliers(data, column , minimum, maximum):
    col_values = data[column].values
    data[column] = np.where(np.logical_or(col_values<minimum, col_values>maximum), col_values.mean(), col_values)
    return data
```


```python
min_val = df["duration"].min()
max_val = 1500
df = remove_outliers(data=df, column='duration' , minimum=min_val, maximum=max_val)

min_val = df["age"].min()
max_val = 80
df = remove_outliers(data=df, column='age' , minimum=min_val, maximum=max_val)

min_val = df["campaign"].min()
max_val = 6
df = remove_outliers(data=df, column='campaign' , minimum=min_val, maximum=max_val)
```

### One-Hot Encoding


```python
#with one hot encoding
df_ohe = df.copy()
obj_data_ohe = pd.get_dummies(df_ohe[object_data],drop_first = False)
obj_data_ohe.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>job_admin.</th>
      <th>job_blue-collar</th>
      <th>job_entrepreneur</th>
      <th>job_housemaid</th>
      <th>job_management</th>
      <th>job_retired</th>
      <th>job_self-employed</th>
      <th>job_services</th>
      <th>job_student</th>
      <th>job_technician</th>
      <th>job_unemployed</th>
      <th>marital_divorced</th>
      <th>marital_married</th>
      <th>marital_single</th>
      <th>housing_no</th>
      <th>housing_yes</th>
      <th>loan_no</th>
      <th>loan_yes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
obj_data_ohe.keys()
```




    Index(['job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid',
           'job_management', 'job_retired', 'job_self-employed', 'job_services',
           'job_student', 'job_technician', 'job_unemployed', 'marital_divorced',
           'marital_married', 'marital_single', 'housing_no', 'housing_yes',
           'loan_no', 'loan_yes'],
          dtype='object')




```python
obj_data_ohe.shape
```




    (43190, 18)




```python
df_ohe = pd.concat([df_ohe, obj_data_ohe], axis=1)
df_ohe.drop('subscribed', axis=1, inplace=True)
df_ohe['subscribed'] = df['subscribed']
```


```python
df_ohe.keys()
```




    Index(['age', 'job', 'marital', 'education', 'balance', 'housing', 'loan',
           'duration', 'campaign', 'job_admin.', 'job_blue-collar',
           'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
           'job_self-employed', 'job_services', 'job_student', 'job_technician',
           'job_unemployed', 'marital_divorced', 'marital_married',
           'marital_single', 'housing_no', 'housing_yes', 'loan_no', 'loan_yes',
           'subscribed'],
          dtype='object')




```python
# Dropping object data from dataframe df_ohe, as we are going to use the encoded columns
df_ohe.drop(object_data, axis=1, inplace=True)
```


```python
df_ohe.keys()
```




    Index(['age', 'education', 'balance', 'duration', 'campaign', 'job_admin.',
           'job_blue-collar', 'job_entrepreneur', 'job_housemaid',
           'job_management', 'job_retired', 'job_self-employed', 'job_services',
           'job_student', 'job_technician', 'job_unemployed', 'marital_divorced',
           'marital_married', 'marital_single', 'housing_no', 'housing_yes',
           'loan_no', 'loan_yes', 'subscribed'],
          dtype='object')




```python
df_ohe.shape
```




    (43190, 24)



### Summary of Feature engneering


```python
print('Total number of features:', len(df_ohe.keys()))
print('Numerical Features:',len(df_ohe.keys()) - len(obj_data_ohe.keys()))
print('Encoded Categorical Features:', len(obj_data_ohe.keys()))
```

    Total number of features: 24
    Numerical Features: 6
    Encoded Categorical Features: 18
    


```python
# Checking for any null values
df_ohe.isnull().sum().sort_values(ascending = False)
```




    subscribed           0
    loan_yes             0
    education            0
    balance              0
    duration             0
    campaign             0
    job_admin.           0
    job_blue-collar      0
    job_entrepreneur     0
    job_housemaid        0
    job_management       0
    job_retired          0
    job_self-employed    0
    job_services         0
    job_student          0
    job_technician       0
    job_unemployed       0
    marital_divorced     0
    marital_married      0
    marital_single       0
    housing_no           0
    housing_yes          0
    loan_no              0
    age                  0
    dtype: int64




```python
# Copying data to a new dataframe, which includes the columns of interest.
df_model = df_ohe.copy()

print("Columns of our interest:")

for col in df_model:
    print(f'\t\t\t{col}')
```

    Columns of our interest:
    			age
    			education
    			balance
    			duration
    			campaign
    			job_admin.
    			job_blue-collar
    			job_entrepreneur
    			job_housemaid
    			job_management
    			job_retired
    			job_self-employed
    			job_services
    			job_student
    			job_technician
    			job_unemployed
    			marital_divorced
    			marital_married
    			marital_single
    			housing_no
    			housing_yes
    			loan_no
    			loan_yes
    			subscribed
    


```python
sns.countplot(x=df_model['subscribed'], data=df_ohe)
```




    <AxesSubplot:xlabel='subscribed', ylabel='count'>




    
![png](output_93_1.png)
    



```python
df_model_yes = df_model[df_model['subscribed']==1]
for _ in range(6):
    df_model = pd.concat([df_model,df_model_yes])
df_model_yes = df_model[df_model['subscribed']==1].head(2500)
df_model = pd.concat([df_model,df_model_yes])
```


```python
sns.countplot(x=df_model['subscribed'], data=df_ohe)
```




    <AxesSubplot:xlabel='subscribed', ylabel='count'>




    
![png](output_95_1.png)
    



```python
df_model[list(df_model.columns)[:12]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>education</th>
      <th>balance</th>
      <th>duration</th>
      <th>campaign</th>
      <th>job_admin.</th>
      <th>job_blue-collar</th>
      <th>job_entrepreneur</th>
      <th>job_housemaid</th>
      <th>job_management</th>
      <th>job_retired</th>
      <th>job_self-employed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>58.0</td>
      <td>3</td>
      <td>2143</td>
      <td>261.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>44.0</td>
      <td>2</td>
      <td>29</td>
      <td>151.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33.0</td>
      <td>2</td>
      <td>2</td>
      <td>76.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35.0</td>
      <td>3</td>
      <td>231</td>
      <td>139.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>28.0</td>
      <td>3</td>
      <td>447</td>
      <td>217.0</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_model[list(df_model.columns)[12:]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>job_services</th>
      <th>job_student</th>
      <th>job_technician</th>
      <th>job_unemployed</th>
      <th>marital_divorced</th>
      <th>marital_married</th>
      <th>marital_single</th>
      <th>housing_no</th>
      <th>housing_yes</th>
      <th>loan_no</th>
      <th>loan_yes</th>
      <th>subscribed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Testing Models


```python
def print_report(classifier, x_train, y_train, y_test, y_pred):
    accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10, n_jobs = -1)
    print(f'{classifier} Confusion  matrix:')
    print(confusion_matrix(y_test, y_pred))
    print(f'{classifier} accuracy mean {accuracies.mean()}')
    print(f'{classifier} accuracy std dev {accuracies.std()}')
    print(f'{classifier} preciosn score {precision_score(y_test, y_pred)}')
    print(f'{classifier} recall score {recall_score(y_test, y_pred)}')
    print(f'{classifier} f1 score {f1_score(y_test, y_pred)}')
    print('*'*50)
```


```python
from sklearn.metrics import precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
```


```python
x = df_model.drop('subscribed',axis = 1).values
y = df_model['subscribed'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
```


```python

```


```python
lR = LogisticRegression()
lR.fit(x_train, y_train)
```




    LogisticRegression()




```python
# Predicting the Test set results
y_pred = lR.predict(x_test)
```


```python
print_report(lR, x_train, y_train, y_test, y_pred)
```

    LogisticRegression() Confusion  matrix:
    [[7647 1911]
     [2323 7073]]
    LogisticRegression() accuracy mean 0.7751396279881527
    LogisticRegression() accuracy std dev 0.004652558949552185
    LogisticRegression() preciosn score 0.7872885129118433
    LogisticRegression() recall score 0.752767134951043
    LogisticRegression() f1 score 0.7696409140369967
    **************************************************
    


```python
# KNN
kNN = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p =2)
kNN.fit(x_train, y_train)
```




    KNeighborsClassifier()




```python
y_pred = kNN.predict(x_test)
```


```python
print_report(kNN, x_train, y_train, y_test, y_pred)
```

    KNeighborsClassifier() Confusion  matrix:
    [[7368 2190]
     [  91 9305]]
    KNeighborsClassifier() accuracy mean 0.8702999528517225
    KNeighborsClassifier() accuracy std dev 0.005564356162604067
    KNeighborsClassifier() preciosn score 0.8094823836450631
    KNeighborsClassifier() recall score 0.9903150276713495
    KNeighborsClassifier() f1 score 0.890814226221818
    **************************************************
    


```python
# Fitting SVM to the trainig  set
svm = SVC(kernel = 'linear', random_state=0)
svm.fit(x_train, y_train)
```




    SVC(kernel='linear', random_state=0)




```python
y_pred = svm.predict(x_test)
```


```python
print_report(svm, x_train, y_train, y_test, y_pred)
```


```python
# Naive Bayes
nb = GaussianNB()
nb.fit(x_train, y_train)

```


```python
y_pred = nb.predict(x_test)
```


```python
print_report(nb, x_train, y_train, y_test, y_pred)
```


```python
# Decision Tree
dt = DecisionTreeClassifier(criterion = 'entropy')
dt.fit(x_train, y_train)
```


```python
y_pred = dt.predict(x_test)
```


```python
print_report(dt, x_train, y_train, y_test, y_pred)
```


```python
# Random Forest Classifier
rfc = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')
rfc.fit(x_train, y_train)
```


```python
y_pred = rfc.predict(x_test)
```


```python
# Applying k_Fold Cross Validation
print_report(rfc, x_train, y_train, y_test, y_pred)
```


```python

```


```python

```


```python

```
