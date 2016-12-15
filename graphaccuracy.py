# graphs the accuracy of the predictions using
# the different combinations of attributes

import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('All', 'Artist Hotness', 'Duration', 'End of Fade in', 'Key', 'Key Confidence', 'Loudness', 'Mode', 'Mode Confidence', 'Tempo', 'Start of Fade out', 'Time Signature', 'Time Signature Confidence', 'Year')
y_pos = np.arange(len(objects))
#performance = [97.27,95.74,97.06,96.46,96.9,97.03,97.14,96.31,95.77,97.25,97.1,97.06,97.1,96.65]
performance = [98.6,98.04,98.08,98.24,97.5,98.47,98.27,97.27,98.54,98.23,98.54,98.16,98.61,98.35]

plt.bar(y_pos, performance, align='center', alpha=0.75)
plt.xticks(rotation=90)
plt.xticks(y_pos, objects)
plt.ylabel('Percentage of Accuracy')
plt.xlabel('Attributes')
plt.title('Prediction Accuracy for Attributes')

rects = plt.bar(y_pos, performance, align='center', alpha=0.75)
for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., height,
                float(height),
                ha='center', va='bottom')

plt.show()