from pandas import pd

df = pd.read_csv('path_to_your_file.csv')

def convert_to_number(value):
    if 'K' in value:
        return float(value.replace('K', '')) * 1000
    elif 'M' in value:
        return float(value.replace('M', '')) * 1000000
    else:
        return float(value)

df['follower_count_numeric'] = df['follower_count'].apply(convert_to_number)
df['like_count_numeric'] = df['like_count'].apply(convert_to_number)

# Filter the data where follower_count > 100K and like_count > 1M
filtered_df = df[(df['follower_count_numeric'] > 100000) & (df['like_count_numeric'] > 1000000)]

# Display the filtered data
print(filtered_df)