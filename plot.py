import pandas as pd
import matplotlib.pyplot as plt


# load csv file
df = pd.read_csv('data.csv')

# generate plot
df.boxplot(column='latency_seconds', by='test_case')
plt.title('Latency by Test Case')
plt.xlabel('Test Case')
plt.ylabel('Latency (s)')
plt.savefig('latency_plot.png')
plt.show()

average_performance = df.groupby('test_case')['latency_seconds'].mean()
print(f"Average performance: {average_performance} seconds")