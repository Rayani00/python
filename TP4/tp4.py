import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("company_sales_data.csv", sep=",")

""" uncomment this for q1 and q2 """
# fig = plt.figure()

#Q1
ax = fig.add_subplot(1, 1, 1)
ax.bar(data["month_number"], data["total_profit"])
ax.set_xticks([i for i in range(13)])
ax.set_title('total profit per month')
ax.set_xlabel('Month')
ax.set_ylabel('Profit')

#Q2
ax = fig.add_subplot(1, 1, 1)
ax.plot(data["month_number"], data["facewash"])
ax.plot(data["month_number"], data["facecream"])
ax.plot(data["month_number"], data["toothpaste"])
ax.plot(data["month_number"], data["bathingsoap"])
ax.plot(data["month_number"], data["shampoo"])
ax.plot(data["month_number"], data["moisturizer"])
plt.legend(['facewash', 'facecream', 'toothpaste', 'bathingsoap',
           'shampoo', 'moisturizer'], loc="upper left")
ax.set_xticks([i for i in range(13)])
ax.set_title('Evolution of sales per product over months')
ax.set_xlabel('Month')
ax.set_ylabel('sales')

#Q3
data.plot(x='month_number', y=['facecream',
          'toothpaste'], kind='bar', rot=45, stacked=False)

#Q4
data.plot(x='month_number', y='total_profit', kind='pie', rot=45)

#Q5
frame = data.sum(axis=0, skipna=True)
df = pd.DataFrame({'facecream': [frame['facecream']],
 'facewash': [frame['facewash']],
 'toothpaste': [frame['toothpaste']],
 'bathingsoap': [frame['bathingsoap']],
 'shampoo': [frame['shampoo']],
 'moisturizer': [frame['moisturizer']]})
df.plot(y=["facecream", "facewash", "toothpaste", "bathingsoap", "sham
