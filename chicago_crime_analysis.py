import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use('fivethirtyeight')

path = 'Crimes_-_2001_to_Present.csv'
df = pd.read_csv(path)
df.dropna(subset=['Date', 'Primary Type', 'District'], inplace=True)

df['Timestamp'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
df.dropna(subset=['Timestamp'], inplace=True)
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month_name()
df['DayOfWeek'] = df['Timestamp'].dt.day_name()
df['Hour'] = df['Timestamp'].dt.hour

# Top 10 Most Common Crimes
plt.figure(figsize=(10, 8))
top_crimes = df['Primary Type'].value_counts().nlargest(10).index
sns.countplot(y='Primary Type', data=df, order=top_crimes, palette='viridis')
plt.title('Top 10 Most Common Crime Types in Chicago')
plt.xlabel('Number of Incidents')
plt.ylabel('Crime Type')
plt.tight_layout()
plt.show()

# Crimes by Police District
plt.figure(figsize=(10, 8))
sns.countplot(y='District', data=df, order=df['District'].value_counts().index, palette='plasma')
plt.title('Crime Incidents by Police District')
plt.xlabel('Number of Incidents')
plt.ylabel('Police District')
plt.tight_layout()
plt.show()

# Crimes by Day of the Week
plt.figure(figsize=(10, 6))
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='DayOfWeek', data=df, order=day_order, palette='cividis')
plt.title('Crime Incidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Crimes by Hour of the Day
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='magma')
plt.title('Crime Incidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.show()
