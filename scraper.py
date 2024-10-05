import urllib.parse
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import undetected_chromedriver as uc
from utils import random_delay
from utils import infinite_scroll

def keyword_scrape(driver: WebDriver, search_term):
    random_delay()

    url = f"https://www.tiktok.com/search/video?q={search_term}"

    # encoding the url so that hashtag and spaces converts into proper format
    encoded_url = urllib.parse.quote(url, safe=':/?=&')

    driver.get(encoded_url)

    random_delay()

    infinite_scroll(driver)

    random_delay()

    video_url_tags = driver.find_elements(By.XPATH, "//div[@class=' css-13fa1gi-DivWrapper e1cg0wnj1']/a")

    video_urls = [video_url_tag.get_attribute("href") for video_url_tag in video_url_tags]

    # author_usernames = [url.split("/")[3].replace("@", "") for url in video_urls]

    print(video_urls)
    print(len(video_urls))

    return video_urls

def scrape_single_video_caption(driver: WebDriver, url: str):
    random_delay()

    driver.get(url)

    random_delay()

    try:
        post_description = driver.find_element(By.XPATH, "//h1[@data-e2e='browse-video-desc']/span").text

        post_hashtags = driver.find_elements(By.XPATH, "//h1[@data-e2e='browse-video-desc']/a/strong")

        post_hashtag_texts = [tag.text for tag in post_hashtags]

        caption = post_description + " ".join(post_hashtag_texts)

        return caption
        
    except Exception as e:
        print("Error scraping profile:", e)

    random_delay()

# scrape_single_video_caption("https://www.tiktok.com/@foodiemeetsfood_/video/7270114952407485698?q=places%20to%20visit&t=1728109486143")


def scrape_author_information(driver: WebDriver, username):
    url = f"https://www.tiktok.com/@{username}"

    driver.get(url)

    random_delay()

    try:
        username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[@data-e2e='user-title']"))
        ).text

        following_count = driver.find_element(By.XPATH, "//strong[@title='Following']").text
        follower_count = driver.find_element(By.XPATH, "//strong[@title='Followers']").text
        like_count = driver.find_element(By.XPATH, "//strong[@title='Likes']").text

        # Store the scraped data in a dictionary
        author_information = {
            "username": username,
            "following_count": following_count,
            "follower_count": follower_count,
            "like_count": like_count
        }

    except Exception as e:
        print("Error scraping profile:", e)

    random_delay()

    return author_information

# scrape_profile_data("foodiemeetsfood_")

def tag_scrape(driver: WebDriver, tag_term: str):
    random_delay()

    tag = tag_term.replace("#", "")

    driver.get(f"https://www.tiktok.com/tag/{tag}")

    random_delay()

    infinite_scroll(driver)

    random_delay()

    video_tags = driver.find_elements(By.XPATH, "//div[@class=' css-13fa1gi-DivWrapper e1cg0wnj1']/a")

    video_urls = [video_tag.get_attribute("href") for video_tag in video_tags]

    print(video_urls)
    print(len(video_urls))

    random_delay()

    return video_urls

