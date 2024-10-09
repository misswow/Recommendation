import mysql.connector
import pandas as pd

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    database='playlist_recommendation',
    user='root',
    password='$qlMatch'
)

# Query the data
query = "SELECT * FROM playlist_info;"
df = pd.read_sql(query, conn)

# Remove duplicates
df.drop_duplicates(subset=['Track', 'Artist'], inplace=True)

# Fill or drop missing values
df.fillna(0, inplace=True)  # Example: Fill NaNs with 0

# Ensure correct data types
df['Release_Year'] = df['Release_Year'].astype(int)


# Summary statistics
print(df.describe())




df.to_csv('cleaned_tracks.csv', index=False)

# Close the connection
conn.close()
