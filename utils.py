import time
import random

def random_delay(low=2, high=5):
    time.sleep(random.uniform(low, high))


def infinite_scroll(driver):
    """
        Takes the selenium driver as an input and scrolls infinitely to the end of the page.
    """
    while True:
        initial_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
        random_delay()
        
        newHeight = driver.execute_script("return document.body.scrollHeight")
        
        if (newHeight == initial_height):
            break