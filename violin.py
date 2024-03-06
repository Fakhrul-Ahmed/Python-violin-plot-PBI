# for this code we need to install seaborn (py -m install seaborn)

import matplotlib as mb
mb.rcParams['font.size']=25

import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(x=dataset["Particulate"], y=dataset["DailyRainfall"], palette="Blues")
plt.show()