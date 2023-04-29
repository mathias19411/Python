import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import csv
import matplotlib.pyplot as plt

# First, we calculate the prior probability which is just the percentage of data points belonging to the mentioned class
# For example, if our training dataset has 60% edible mushrooms, then the prior probability will be 0.6 when calculating 
# in the testing side.

def prior(y_train, label):
    
    total_points = y_train.shape[0]
    class_points = np.sum(y_train == label)
    
    return class_points/float(total_points)

dataFrame = pd.read_csv('MushroomCSV.csv')

dataFrame.head()

## Next, we will define a function to calculate the conditional probability that we will use then to calculate the
## likelihood,

def cond_prob(X_train, y_train, feat_col, feat_val, label):
    """
    In this function, we will calculate the conditional probability which will be used to calculate likelihood.
    The value it returns is of the form 
        P(x_i | y = C)
    which is the probability of the current feature (given by feat_col x_i) having the current value (given by feat_val)
    given that it belongs to the target class C
    
    Effectively, it reduces to the form
        all points belongig to class C which have the given value for the feature column / all points belonging to class C
    """
    # Getting all the 
    X_filtered = X_train[y_train == label]
    
    numerator = np.sum(X_filtered[feat_col] == feat_val)
    denominator = np.sum(y_train == label)
    
    return numerator/float(denominator)

def predict(X_train, y_train, xtest):
    
    # Get the number of target classes
    classes = np.unique(y_train)
    
    # All the features for our dataset
    features = [x for x in X_train.columns]
    
    
    # Compute posterior probabilites for each class
    post_probs = []
    
    for label in classes:
        
        # Since, posterior = prior * likelihood
        # We'll calculate likelihood by calculating the product of the conditional probabilities for each of the features
        
        likelihood = 1.0
        
        for f in features:
            cond = cond_prob(X_train, y_train, f, xtest[f], label)
            likelihood *= cond
        
        prior_prob = prior(y_train, label)
        
        posterior = prior_prob * likelihood
        
        post_probs.append(posterior)
        
    # Return the label for which the posterior probability was the maximum
    prediction = np.argmax(post_probs)
    
    return prediction 

def accuracy_score(X_train, y_train, xtest, ytest):
    
    preds = []
    
    for i in range(xtest.shape[0]):
        pred_label = predict(X_train, y_train, xtest.iloc[i])
        preds.append(pred_label)
        
    preds = np.array(preds)
    
    accuracy = np.sum(preds == ytest)/ytest.shape[0]
    
    return accuracy

# #Printing the unique categories of appearance of muchrooms
# for column in dataFrame.columns:
#     # If the column has categorical data
#     if dataFrame[column].dtype == 'object':
#         # Print the column name
#         print(f"\n{column}:")
#         # Print the frequency of each unique value in the column
#         print(dataFrame[column].value_counts())
# row1 = dataFrame.iloc[28]
# print(row1)
encoder = LabelEncoder()

# Apply the encoder to each of the columns
dataFrame = dataFrame.apply(encoder.fit_transform)

dataFrame.head()
    # print(dataFrame)
    # row = dataFrame.iloc[28]
    # print(row)
    # dataFrame.set_index('CLASS', inplace=True)

    # dataFrame['CAPSHAPE'].plot(kind='hist')

    # plt.show()


# Seperating our target and features
X = dataFrame.drop(columns = ['CLASS'])
y = dataFrame['CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

# print("X_train = ", X_train.shape)
# print("y_train = ", y_train.shape)
# print("X_test = ", X_test.shape)
# print("y_test = ", y_test.shape)

#random example

cap_shape = input('Enter cap shape (bell=0,conical=1,convex=2,flat=3, knobbed=4,sunken=5): ')
cap_surface = input('Enter cap surface (fibrous=0,grooves=1,scaly=2,smooth=3): ')
cap_color = input('Enter cap color (brown=0,buff=1,cinnamon=2,gray=3,green=4,pink=5,purple=6,red=7,white=8,yellow=9): ')
bruises = input('Are there bruises? (no=0,yes=1): ')
odor = input('What is the odor? (almond=0,anise=1,creosote=2,fishy=3,foul=4,musty=5,none=6,pungent=7,spicy=8): ')

rand_example = 

output = predict(X_train, y_train, X_test.iloc[rand_example])

print("Naive Bayes Classifier predicts ", output)
print("Current Answer ", y_test.iloc[rand_example])
    
# Capshape == bell(0) , conical(1) , convex(2) , flat(3) , knobbed(4) , sunken (5) 
# Surface == fibrous(0) , grooves(1) , scaly (2) , smooth (3)
# Color == brown(0) , buff(1) , cinnamo(2) , gray(3) , green(4) , pink(5) , purple(6) , red(7) , white(8) , yellow(9)
# Bruises == no(0) , yes(1)
# Odor == almond(0) , anise(1) , creosote(2) , fishy(3) , foul(4) , musty(5) , none(6) , pungent(7) , spicy(8)
# Gill-Attaychment == attatched(0) , free(1)
# Gill-Spacing == close(0) , crowded(1)
# Gill-Size == broad(0) , narrow(1)
# Gill-Color == b'w'(0) , b'y'(1) , black(2) , brown(3) , buff(4) , chocolate(5) , gray(6) , green(7) , orange(8) , pink(9) , purple(10) , red(11)
# Stalk-Shape == enlarging(0) , tapering(1)
# Stalk-Root == bulbous(0) , club(1) , equal(2) , missing(3) , rooted(4)
# Stalk-Surface-Above-Ring == fibrous(0) , scaly(1) , silky(2) , smooth(3)
# Stalk-Surface-Below-Ring == fibrous(0) , scaly(1) , silky(2) , smooth(3)
# Stalk-Color-Above-Ring == brown(0) , buff(1) , cinnamo(2) , gray(3) , orange(4) , pink(5) , red(6)  , white(7) , yellow(8)
# Stalk-Color-Below-Ring == brown(0) , buff(1) , cinnamo(2) , gray(3) , orange(4) , pink(5) , red(6)  , white(7) , yellow(8)
# Veil-Type == partial(0)
# Veil-Color == brown(0) , orange(1) , white(2) , yellow(3)
# Ring-Number == none(0) , one(1) , two(2)
# Ring-Type == evanescent(0) , flaring(1) , large(2) , none(3) , pendant(4)
# Spore-Print-Color == black(0) , brown(1) , buff(2) , chocolate(3) , green(4) , orange(5) , purple(6) , white(7) , yellow(8)
# Population == abundant(0) , clustered(1) , numerous(2) , scattered(3) , several(4) , solitary(5)
# Habitat == grasses(0) , leaves(1) , meadows(2) , path(3) , urban(4) , waste(5) , wood(6)
