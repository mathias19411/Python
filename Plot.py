import pandas as pd
import matplotlib.pyplot as plt

data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Sales': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df.plot(kind='bar', title='Sales by Year')

plt.show()
