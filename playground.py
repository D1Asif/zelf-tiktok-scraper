# url = "https://www.tiktok.com/@monsieur_arefin/video/7061436382807461147"

# print(url.split("/")[3].replace("@", ""))

# x = list(set(["abc", "abc", "xyz", "xyz"]))

# y = "hello"
# z = " ".join(x)
# print(z)



To export unique_video_urls, author_usernames, and captions to a CSV file using Python and pandas, you can first create a DataFrame with these lists, and then use the to_csv function. Here's how you can do it:

python
Copy code
import pandas as pd

# Assuming unique_video_urls, author_usernames, and captions are defined
unique_video_urls = list(set(video_urls))  # Ensure unique URLs
author_usernames = [url.split("/")[3].replace("@", "") for url in unique_video_urls]
captions = []  # Add your captions list here

# Create a DataFrame
data = {
    'Video URL': unique_video_urls,
    'Author Username': author_usernames,
    'Caption': captions
}

df = pd.DataFrame(data)

# Export to CSV
df.to_csv('video_data.csv', index=False)

print("Data exported to video_data.csv")


