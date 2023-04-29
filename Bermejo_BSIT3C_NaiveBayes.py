import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the mushroom dataset
mushrooms = pd.read_csv('MushroomCSV.csv')

# Encode categorical variables as numerical
encoder = LabelEncoder()
for col in mushrooms.columns:
    mushrooms[col] = encoder.fit_transform(mushrooms[col])

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    mushrooms.drop('CLASS', axis=1), mushrooms['CLASS'], test_size=0.3, random_state=42)

# Train the Naive Bayes classifier
clf = GaussianNB()
clf.fit(X_train, y_train)

# Plot a histogram for the columns
mushrooms['CAPSHAPE'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Cap Shapes")
plt.show()
mushrooms['SURFACE'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Cap Surfaces")
plt.show()
mushrooms['COLOR'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Cap Colors")
plt.show()
mushrooms['BRUISES'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Bruises")
plt.show()
mushrooms['ODOR'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Odors")
plt.show()
mushrooms['GILL-ATTACHMENT'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Gill Attatchments")
plt.show()
mushrooms['GILL-SPACING'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Gill Spacings")
plt.show()
mushrooms['GILL-SIZE'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Gill Sizes")
plt.show()
mushrooms['GILL-COLOR'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Gill Colors")
plt.show()
mushrooms['STALK-SHAPE'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Stalk Shapes")
plt.show()
mushrooms['STALK-ROOT'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Stalk Roots")
plt.show()
mushrooms['STALK-SURFACE-ABOVE-RING'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Stalk Surfaces Above Ring")
plt.show()
mushrooms['STALK-SURFACE-BELOW-RING'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Stalk Surfaces Below Ring")
plt.show()
mushrooms['STALK-COLOR ABOVE-RING'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Stalk Colors Above Ring")
plt.show()
mushrooms['STALK-COLOR-BELOW-RING'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Stalk Colors Below Ring")
plt.show()
mushrooms['VEIL-TYPE'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Veil Types")
plt.show()
mushrooms['VEIL-COLOR'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Veil Colors")
plt.show()
mushrooms['RING-NUMBER'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Ring Numbers")
plt.show()
mushrooms['RING-TYPE'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Ring Types")
plt.show()
mushrooms['SPORE-PRINT-COLOR'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Spore Print Colors")
plt.show()
mushrooms['POPULATION'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Populations")
plt.show()
mushrooms['HABITAT'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Habitats")
plt.show()
mushrooms['CLASS'].hist(bins=10, color='blue')
plt.title("Histogram of Mushroom Classes")
plt.show()


# Capshape == bell(0) , conical(1) , convex(2) , flat(3) , knobbed(4) , sunken (5) 
# Surface == fibrous(0) , grooves(1) , scaly (2) , smooth (3)
# Color == brown(0) , buff(1) , cinnamo(2) , gray(3) , green(4) , pink(5) , purple(6) , red(7) , white(8) , yellow(9)
# Bruises == no(0) , yes(1)
# Odor == almond(0) , anise(1) , creosote(2) , fishy(3) , foul(4) , musty(5) , none(6) , pungent(7) , spicy(8)
# Gill-Attatchment == attatched(0) , free(1)
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


# Accept user input of categorical variables
print('\nEnter the attributes of the mushroom you want to classify:\n')
cap_shape = int(input('Enter Cap Shape:\nbell == 0\nconical == 1\nconvex == 2\nflat == 3\nknobbed == 4\nsunken == 5\nINPUT --> '))
cap_surface = int(input('\nEnter Cap Surface:\nfibrous == 0\ngrooves == 1\nscaly == 2\nsmooth == 3\nINPUT --> '))
cap_color = int(input('\nEnter cap Color:\nbrown == 0\nbuff == 1\ncinnamon == 2\ngray == 3\ngreen == 4\npink == 5\npurple == 6\nred == 7\nwhite == 8\nyellow == 9\nINPUT --> '))
bruises = int(input('\nAre there Bruises?\nno == 0\nyes == 1\nINPUT --> '))
odor = int(input('\nWhat is the Odor?\nalmond == 0\nanise == 1\ncreosote == 2\nfishy == 3\nfoul == 4\nmusty == 5\nnone == 6\npungent == 7\nspicy == 8\nINPUT --> '))
gill_attatchment = int(input('\nWhat is the Gill Attatchment?\nattatched == 0\nfree == 1\nINPUT --> '))
gill_spacing = int(input('\nWhat is the Gill Spacing?\nclose == 0\ncrowded == 1\nINPUT --> '))
gill_size = int(input('\nWhat is the Gill Size?\nbroad == 0\nnarrow == 1\nINPUT --> '))
gill_color = int(input('\nWhat is the Gill Color?\nb"w" == 0\nb"y" == 1\nblack == 2\nbrown == 3\nbuff == 4\nchocolate == 5\ngray == 6\ngreen == 7\norange == 8\npink == 9\npurple == 10\nred == 11\nINPUT --> '))
stalk_shape = int(input('\nWhat is the Stalk Shape?\nenlarging == 0\ntapering ==1\nINPUT --> '))
stalk_root = int(input('\nWhat is the Stak Root?\nbulbous == 0\nclub == 1\nequal == 2\nmissing == 3\nrooted == 4\nINPUT --> '))
stalk_surface_above_ring = int(input('\nWhat is the Stalk Surface Above Ring?\nfibrous == 0\nscaly == 1\nsilky == 2\nsmooth == 3\nINPUT --> '))
stalk_surface_below_ring = int(input('\nWhat is the Stalk Surface Below Ring?\nfibrous == 0\nscaly == 1\nsilky == 2\nsmooth == 3\nINPUT --> '))
stalk_color_above_ring = int(input('\nWhat is the Stalk Color Above Ring?\nbrown == 0\nbuff == 1\ncinnamo == 2\ngray == 3\norange == 4\npink == 5\nred == 6\nwhite == 7\nyellow == 8\nINPUT --> '))
stalk_color_below_ring = int(input('\nWhat is the Stalk Color Below Ring?\nbrown == 0\nbuff == 1\ncinnamo == 2\ngray == 3\norange == 4\npink == 5\nred == 6\nwhite == 7\nyellow == 8\nINPUT --> '))
veil_type = int(input('\nWhat is the Veil Type?\npartial == 0\nINPUT --> '))
veil_color = int(input('\nWhat is the Veil Color?\nbrown == 0\norange == 1\nwhite == 2\nyellow == 3\nINPUT --> '))
ring_number = int(input('\nHow many is the Ring Number?\nnone == 0\none == 1\ntwo ==2\nINPUT --> '))
ring_type = int(input('\nWhat is the Ring Type?\nevanescent == 0\nflaring == 1\nlarge == 2\nnone == 3\npendant == 4\nINPUT --> '))
spore_print_color = int(input('\nWhat is is the Spore Print Color?\nblack == 0\nbrown == 1\nbuff == 2\nchocolate == 3\ngreen == 4\norange == 5\npurple == 6\nwhite == 7\nyellow == 8\nINPUT --> '))
population = int(input('\nWhat is the Population?\nabundant == 0\nclustered == 1\nnumerous == 2\nscattered == 3\nseveral == 4\nsolitary == 5\nINPUT --> '))
habitat = int(input('\nWhat is its Habitat?\ngrasses == 0\nleaves == 1\nmeadows == 2\npath == 3\nurban == 4\nwaste == 5\nwood == 6\nINPUT --> '))

# Make a prediction
input_data = [[cap_shape, cap_surface, cap_color, bruises, odor, gill_attatchment, gill_spacing, gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat]]
predicted_class = clf.predict(input_data)

# Print the predicted class
if predicted_class[0] == 0:
    print('\nThe mushroom is EDIBLE.')
else:
    print('\nThe mushroom is POISONOUS.')
    

