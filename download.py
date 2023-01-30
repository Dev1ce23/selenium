from pytube import YouTube
from selenium import webdriver

# Use Selenium to access the video page
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=Rumya2V8fR4")

# Use pytube to get the video URL
yt = YouTube(driver.current_url)
video = yt.streams.first()

# Download the video
video.download("/path/to/download/directory")

# Close the browser
driver.close()
