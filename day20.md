# DATA VISHUALIZATION AND FEATURE ENGINEERING
## 1.DATA VISHUALIZATION
### Types of input variables
* Numerical variables
  - Continuous\
     Can take on any value within a specific range.\
      eg:age,weight.temperature,etc...
  - discrete\
     Can only take on specific values.\
      eg:Number of children, number of cars,etc....
* categorical variables
    Data that represents categories or groups.
#### Classification 
* Predicts discrete values.
* Output variable is categorical.
#### Regression
* Predicts continuous numerical values.
* Output variable is continuous.
#### Labels(predicted variables) and features(input variables)
### Vishualization
#### Libraries
##### 1.MatPlotLib
  - Figures : Create a figure using plt.figure().
  - Axis labels : Add labels to the x and y axes using plt.xlabel() and plt.ylabel(),customize the font size, font weight, and other properties of the labels.
  - Sub figures : Create multiple subplots within a single figure using plt.subplot().
  - Ticks : customize the appearance of ticks using plt.xticks() and plt.yticks()
#### Types of plot
* Line plot\
    Showing trends over time.
* Bar Charts\
    Comparing categorical data.
* Pie Charts\
    Showing the composition of a whole.
* Histogram\
    Understanding the distribution of numerical data.
* CDF plot\
    It represents the cumulative distribution function.
* KDE plot\
    It estimating the probability density function.
* Scatter plot with color\
     Identifying relationships between two numerical variables.
* Heatmaps\
    Visualizing data across two dimensions.
* Box plots\
    Comparing distributions of data.
##### 2.Seaborn
## 2.FEATURE ENGINEERING
* Feature Orthogonality\
   When features are orthogonal, they provide unique information to a model, which can improve its predictive power.
  -> Cosine Similarity\
    High cosine similarity : Indicates that the features are highly correlated, which can lead to multicollinearity issues.
    Low cosine similarity : Indicates that the features are less correlated, suggesting that they provide unique information.
* Feature Colinearity\
   Feature colinearity occurs when two or more predictor (independent) variables in a statistical model are highly correlated.
* Feature Slicing\
   Feature slicing involves creating new features by splitting an existing feature into multiple parts.
* Indicator Variable\
* Feature Binning
* Mathematical Transforms 
   * Logarithms
   * FFT & STFT 
