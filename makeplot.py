import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('brudiff.csv')
print(df)


import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path, zoom=1):
    return OffsetImage(plt.imread(path), zoom=zoom)

# paths = [
# 'logos/Bruins.png',
# 'logos/Bruins.png',
# 'logos/Bruins.png',
# 'logos/Bruins.png',
# 'logos/Bruins.png',
#     ]
    
#x = [0,1,2,3,4]
#y = [0,1,2,3,4]


# xlabel = 'Goal Differential'
# xframe = 'Diff'
# yframe = 'Points'
# ylabel = 'Points'

ylabel = 'Goals For'
yframe = 'GoalsFor'
xlabel = 'Goals Against'
xframe = 'GoalsAgainst'


# xlabel = 'Points'
# xframe = 'Points'
# ylabel = 'Goals Against'
# yframe = 'GoalsAgainst'


x = df[xframe]
y = df[yframe]


paths = ['logos/{}.png'.format(df['Team'][i])for i in range(len(df['Team']))]

plt.rcParams["font.size"] = "30"


fig, ax = plt.subplots(figsize =(10,10)) 
ax.scatter(x, y) 

for x0, y0, path in zip(x, y,paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)

plt.title('{} vs. {}, 2/21/23'.format(xlabel, ylabel)) 
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

#plt.show()
plt.savefig('{}vs{}.png'.format(xframe, yframe))

# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# # from matplotlib.cbook import get_sample_data

# # def main():
# #     x = np.linspace(0, 10, 20)
# #     y = np.cos(x)
# #     image_path = 'logos/Bruins.png'
# #     fig, ax = plt.subplots()
# #     imscatter(x, y, image_path, zoom=0.1, ax=ax)
# #     ax.plot(x, y)
# #     plt.show()

# # def imscatter(x, y, image, ax=None, zoom=1):
# #     if ax is None:
# #         ax = plt.gca()
# #     try:
# #         image = plt.imread(image)
# #     except TypeError:
# #         # Likely already an array...
# #         pass
# #     im = OffsetImage(image, zoom=zoom)
# #     x, y = np.atleast_1d(x, y)
# #     artists = []
# #     for x0, y0 in zip(x, y):
# #         ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
# #         artists.append(ax.add_artist(ab))
# #     ax.update_datalim(np.column_stack([x, y]))
# #     ax.autoscale()
# #     return artists

# # main()



# # # #Make a 2d scatter plot of the first and second columns
# # # plt.scatter(df['Points'], df['Diff'])

# # # plt.show()
