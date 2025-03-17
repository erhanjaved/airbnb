## Group AECA - Data-Driven Road Safety: Global Accidents Analysis

### 1. Introduction

#### 1.1 Dataset Description 

The Global Road Accidents dataset is a large collection of road accident data from different countries around the world. It includes 132,000 records with each row representing a road accident occurrence. There are 30 columns/features on important details like accident severity, weather conditions, number of vehicles, driver characteristics (e.g. age, gender, and alcohol levels), road type, speed limits, emergency response time, and even economic losses. This dataset is suitable for analyzing traffic accidents and the factors that contribute to them, which can be useful for predicting outcomes like severity and fatalities for future incidents. 

#### 1.2 Data Source

The dataset is publicly available on [Kaggle](https://www.kaggle.com/datasets/ankushpanday1/global-road-accidents-dataset/data)
 under the MIT license. It is mentioned in the documentation that the data is simulated from twelve reports, but does not specify which ones. Likely sources include official reports, government transportation agencies, and traffic safety studies. The dataset is updated annually on Kaggle and was last updated in February 2025.  

#### 1.3 Team Members 

**Carol Zhang**: I am a fifth-year Commerce student with a minor in Data Science. I am interested in the Global Road Accidents dataset because road safety is an important issue worldwide that has impacted almost everyone I know, including myself. I would like to explore how data can help us identify patterns and risk factors to motivate better decision-making. This could potentially prevent or reduce the severity of accidents in the future. 

**Ayuho Negishi**: I am a fifth-year Psychology student minoring in Data Science. My academic background has made me very interested in understanding human behaviour. I am especially curious how driver-related factors (e.g., fatigue, alcohol levels) might reveal broader cultural and behavioural patterns. Although the dataset does not fully capture all the details of cultural context, I hope to find trends in these variables that suggest how social factors affect driving behaviour and accident outcomes.

**Erhan Asad Javed**: I’m a fourth-year Mathematics student with a minor in Data Science. This dataset is particularly interesting to me because it allows me to apply my practical skills in data cleaning and organization to create effective visualizations on a topic that is critically important to modern road safety. My goal is to uncover underlying trends and identify key risk factors associated with car accidents. Through this analysis, I hope to create greater self-awareness and contribute to raising public awareness about road safety.

**Aaron Ma**: I’m a 3rd year Computer Science student. This dataset is particularly interesting to me because road accidents are things that always occur around us, and are more likely to occur compared to things like flying. I’d love to explore the data to be able to identify patterns and trends surrounding the more overlooked attributes such as taking into account response time, vehicle condition, and more.

#### 1.4 Intended Audience 

This project's primary target audience includes policy makers, transportation agencies, and urban planners, who play a critical role in shaping road safety regulations and infrastructure. By analyzing factors such as driver behaviour, road conditions, emergency response efficiency, and socioeconomic impacts, this project aims to provide actionable insights to improve road safety policies. The findings will help identify high-risk areas for prioritization, optimize resource allocation for emergency response services, and reduce the economic burden of road accidents by minimizing fatalities, medical costs, and property damage. By doing so, this project seeks to enhance road safety, reduce accidents, and ultimately save lives. 


### 2. About the Data 

#### 2.1 Data Abstraction
| Attribute Name          | Attribute Type           | Data Semantics                                         | Cardinality                                  |
|-------------------------|--------------------------|--------------------------------------------------------|----------------------------------------------|
| Country                 | Nominal                  | Name of the country where the accident occurred        | 10                                           |
| Year                    | Temporal                 | Year of the accident                                   | 25                                           |
| Month                   | Temporal                 | Month of the accident                                  | 12                                           |
| Day of Week             | Nominal                  | Day of the week when the accident occurred             | 7                                            |
| Time of Day             | Nominal                  | Time of day when the accident occurred                 | 4                                            |
| Urban/Rural             | Binary (Nominal)         | Shows whether the accident was in an urban or rural area| 2                                            |
| Road Type               | Nominal                  | Type of road where the accident occurred               | 3                                            |
| Weather Conditions      | Nominal                  | The weather condition at the time of the accident      | 5                                            |
| Visibility Level        | Quantitative (Continuous)| Visibility level during the accident (higher = better visibility) | 132,000 [50.001928, 499.999646] |
| Number of Vehicles Involved | Quantitative (Discrete) | The total number of vehicles involved in the accident  | 4                                            |
| Speed Limit             | Quantitative (Discrete) | The speed limit of the road at the accident location   | 90 [30, 119]                                 |
| Driver Age Group        | Ordinal                  | Age group of the driver                                | 5                                            |
| Driver Gender           | Binary (Nominal)         | Gender of the driver (Male/Female)                     | 2                                            |
| Driver Alcohol Level    | Quantitative (Continuous)| Blood alcohol level of the driver                      | 132,000 [0.000002, 0.249999]                 |
| Driver Fatigue          | Binary (Quantitative)    | Indicates if the driver was fatigued at the time (1 = Yes, 0 = No) | 2                                        |
| Vehicle Condition       | Ordinal                  | Condition of the vehicle at the time of the accident   | 3                                            |
| Pedestrians Involved    | Quantitative (Discrete)  | Number of pedestrians involved in the accident         | 3 [0, 2]                                     |
| Cyclists Involved       | Quantitative (Discrete)  | Number of cyclists involved in the accident            | 3 [0, 2]                                     |
| Accident Severity       | Ordinal                  | Severity of the accident                               | 3                                            |
| Number of Injuries      | Quantitative (Discrete)  | Total number of injuries in the accident               | 20 [0, 19]                                   |
| Number of Fatalities    | Quantitative (Discrete)  | Total number of fatalities in the accident             | 5 [0, 4]                                     |
| Emergency Response Time | Quantitative (Continuous)| Time taken for the emergency service to respond to the accident | 132,000 [5.000177, 59.999588]           |
| Traffic Volume          | Quantitative (Continuous)| Number of vehicles on the road at the time of the accident | 132,000 [100.062626, 9999.997467]           |
| Road Condition          | Nominal                  | The state of the road when the accident occurred       | 4                                            |
| Accident Cause          | Nominal                  | The primary cause of the accident                      | 5                                            |
| Insurance Claims        | Quantitative (Discrete)  | Number of insurance claims filed after the accident    | 10 [0, 9]                                    |
| Medical Cost            | Quantitative (Continuous)| The medical cost incurred due to the accident          | 132,000 [500.110090, 49999.930130]           |
| Economic Loss           | Quantitative (Continuous)| The estimated economic loss caused by the accident     | 132,000 [1000.335085, 99999.622968]         |
| Region                  | Nominal                  | Continent where the accident occurred                  | 5                                            |
| Population Density      | Quantitative (Continuous)| Population density of the area where the accident occurred | 132,000 [10.002669, 4999.991744]        |

#### 2.2 Exploratory Data Analysis

#### General  
First, we read in the data and generate summary statistics to understand the structure and quality of the dataset. 


```python
accidents = pd.read_csv('data/road_accident_dataset.csv')
accidents.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Year</th>
      <th>Month</th>
      <th>Day of Week</th>
      <th>Time of Day</th>
      <th>Urban/Rural</th>
      <th>Road Type</th>
      <th>Weather Conditions</th>
      <th>Visibility Level</th>
      <th>Number of Vehicles Involved</th>
      <th>...</th>
      <th>Number of Fatalities</th>
      <th>Emergency Response Time</th>
      <th>Traffic Volume</th>
      <th>Road Condition</th>
      <th>Accident Cause</th>
      <th>Insurance Claims</th>
      <th>Medical Cost</th>
      <th>Economic Loss</th>
      <th>Region</th>
      <th>Population Density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USA</td>
      <td>2002</td>
      <td>October</td>
      <td>Tuesday</td>
      <td>Evening</td>
      <td>Rural</td>
      <td>Street</td>
      <td>Windy</td>
      <td>220.414651</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>58.625720</td>
      <td>7412.752760</td>
      <td>Wet</td>
      <td>Weather</td>
      <td>4</td>
      <td>40499.856982</td>
      <td>22072.878502</td>
      <td>Europe</td>
      <td>3866.273014</td>
    </tr>
    <tr>
      <th>1</th>
      <td>UK</td>
      <td>2014</td>
      <td>December</td>
      <td>Saturday</td>
      <td>Evening</td>
      <td>Urban</td>
      <td>Street</td>
      <td>Windy</td>
      <td>168.311358</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>58.041380</td>
      <td>4458.628820</td>
      <td>Snow-covered</td>
      <td>Mechanical Failure</td>
      <td>3</td>
      <td>6486.600073</td>
      <td>9534.399441</td>
      <td>North America</td>
      <td>2333.916224</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USA</td>
      <td>2012</td>
      <td>July</td>
      <td>Sunday</td>
      <td>Afternoon</td>
      <td>Urban</td>
      <td>Highway</td>
      <td>Snowy</td>
      <td>341.286506</td>
      <td>4</td>
      <td>...</td>
      <td>4</td>
      <td>42.374452</td>
      <td>9856.915064</td>
      <td>Wet</td>
      <td>Speeding</td>
      <td>4</td>
      <td>29164.412982</td>
      <td>58009.145124</td>
      <td>South America</td>
      <td>4408.889129</td>
    </tr>
    <tr>
      <th>3</th>
      <td>UK</td>
      <td>2017</td>
      <td>May</td>
      <td>Saturday</td>
      <td>Evening</td>
      <td>Urban</td>
      <td>Main Road</td>
      <td>Clear</td>
      <td>489.384536</td>
      <td>2</td>
      <td>...</td>
      <td>3</td>
      <td>48.554014</td>
      <td>4958.646267</td>
      <td>Icy</td>
      <td>Distracted Driving</td>
      <td>3</td>
      <td>25797.212566</td>
      <td>20907.151302</td>
      <td>Australia</td>
      <td>2810.822423</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Canada</td>
      <td>2002</td>
      <td>July</td>
      <td>Tuesday</td>
      <td>Afternoon</td>
      <td>Rural</td>
      <td>Highway</td>
      <td>Rainy</td>
      <td>348.344850</td>
      <td>1</td>
      <td>...</td>
      <td>4</td>
      <td>18.318250</td>
      <td>3843.191463</td>
      <td>Icy</td>
      <td>Distracted Driving</td>
      <td>8</td>
      <td>15605.293921</td>
      <td>13584.060759</td>
      <td>South America</td>
      <td>3883.645634</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>


    The dataset has 132000 rows and 30 columns.
    


```python
accidents.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 132000 entries, 0 to 131999
    Data columns (total 30 columns):
     #   Column                       Non-Null Count   Dtype  
    ---  ------                       --------------   -----  
     0   Country                      132000 non-null  object 
     1   Year                         132000 non-null  int64  
     2   Month                        132000 non-null  object 
     3   Day of Week                  132000 non-null  object 
     4   Time of Day                  132000 non-null  object 
     5   Urban/Rural                  132000 non-null  object 
     6   Road Type                    132000 non-null  object 
     7   Weather Conditions           132000 non-null  object 
     8   Visibility Level             132000 non-null  float64
     9   Number of Vehicles Involved  132000 non-null  int64  
     10  Speed Limit                  132000 non-null  int64  
     11  Driver Age Group             132000 non-null  object 
     12  Driver Gender                132000 non-null  object 
     13  Driver Alcohol Level         132000 non-null  float64
     14  Driver Fatigue               132000 non-null  int64  
     15  Vehicle Condition            132000 non-null  object 
     16  Pedestrians Involved         132000 non-null  int64  
     17  Cyclists Involved            132000 non-null  int64  
     18  Accident Severity            132000 non-null  object 
     19  Number of Injuries           132000 non-null  int64  
     20  Number of Fatalities         132000 non-null  int64  
     21  Emergency Response Time      132000 non-null  float64
     22  Traffic Volume               132000 non-null  float64
     23  Road Condition               132000 non-null  object 
     24  Accident Cause               132000 non-null  object 
     25  Insurance Claims             132000 non-null  int64  
     26  Medical Cost                 132000 non-null  float64
     27  Economic Loss                132000 non-null  float64
     28  Region                       132000 non-null  object 
     29  Population Density           132000 non-null  float64
    dtypes: float64(7), int64(9), object(14)
    memory usage: 30.2+ MB
    


```python
accidents.isnull().sum()
```




    Country                        0
    Year                           0
    Month                          0
    Day of Week                    0
    Time of Day                    0
    Urban/Rural                    0
    Road Type                      0
    Weather Conditions             0
    Visibility Level               0
    Number of Vehicles Involved    0
    Speed Limit                    0
    Driver Age Group               0
    Driver Gender                  0
    Driver Alcohol Level           0
    Driver Fatigue                 0
    Vehicle Condition              0
    Pedestrians Involved           0
    Cyclists Involved              0
    Accident Severity              0
    Number of Injuries             0
    Number of Fatalities           0
    Emergency Response Time        0
    Traffic Volume                 0
    Road Condition                 0
    Accident Cause                 0
    Insurance Claims               0
    Medical Cost                   0
    Economic Loss                  0
    Region                         0
    Population Density             0
    dtype: int64



There are no missing values for any of the variables in our dataset, meaning that the data is complete and ready for analysis without requiring imputation or handling of null values. 


```python

```
