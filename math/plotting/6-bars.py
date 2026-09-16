#!/usr/bin/env python3
"""Plot a stacked bar chart of fruit owned by each person."""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
fruits = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
bottom = np.zeros(3)

for fruit_type, color, amounts in zip(fruits, colors, fruit):
    plt.bar(people, amounts, bottom=bottom, width=0.5,
            color=color, label=fruit_type)
    bottom += amounts

plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
