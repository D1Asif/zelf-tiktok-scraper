import argparse
from config import keywords, hashtags
from scraper import keyword_scrape, tag_scrape, scrape_single_video_caption, scrape_author_information
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import random_delay
import undetected_chromedriver as uc
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="""
        Provide args for scraping
        """)
    
    # parser.add_argument('--username', type=str, nargs="?", help="add the username of the profile you want to scrape")

    # parser.add_argument('--keyword', type=str, default=config["keyword"], nargs="?", help="add the search keyword")

    return vars(parser.parse_args()) # returns the args in dictionary format

if __name__ == "__main__":

    driver = uc.Chrome()
    driver.get("https://www.tiktok.com/")

    random_delay()

    video_urls = []

    # loop through the keywords and scrape
    for keyword in keywords:
        try:
            print(f"called {keyword}")
            result = tag_scrape(driver, keyword)
            video_urls.extend(result)
        except:
            pass

        random_delay()

    random_delay()
    
    # loop through the hashtags and scrape
    for hashtag in hashtags:
        try:
            result = tag_scrape(driver, hashtag)
            video_urls.extend(result)
        except:
            pass

        random_delay()

    print(video_urls)
    print(len(video_urls))

    unique_video_urls = list(set(video_urls))
    author_usernames = [url.split("/")[3].replace("@", "") for url in unique_video_urls]
    captions = []

    # taking captions in the unique list to save from duplicate requests
    for video_url in unique_video_urls:
        result = scrape_single_video_caption(driver, video_url)
        if result:
            captions.append(result)
        else:
            captions.append("")

    data = {
        'Video URL': unique_video_urls,
        'Author Username': author_usernames,
        'Caption': captions
    }

    df = pd.DataFrame(data)    
    df.to_csv('video_data.csv', index=False)

    author_data = {
        "username": [],
        "following_count": [],
        "follower_count": [],
        "like_count": []
    }

    for username in author_usernames:
        result = scrape_author_information()
        author_data["username"].append(result.username)
        author_data["following_count"].append(result.following_count)
        author_data["follower_count"].append(result.like_count)
        author_data["like_count"].append(result.like_count)

    df = pd.DataFrame(author_data)    
    df.to_csv('author_data.csv', index=False)
    
    driver.quit()
