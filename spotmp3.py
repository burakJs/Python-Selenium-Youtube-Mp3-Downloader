from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os



PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path = DRIVER_BIN)

link = input("Youtube link or song name : ")
link2 = "https://yt1s.com/youtube-to-mp3/tr"


# def spotify():
# 	def openLink(givenLink):
# 		driver.get(givenLink)
# 		html = driver.page_source
# 		time.sleep(8)
# 		return html

# 	htmlsource = openLink(link)
# 	soup = BeautifulSoup(htmlsource, 'html.parser')
# 	tracknames = soup.find_all("div",{"class":"tracklist-name ellipsis-one-line"})
# 	songs = set()

# 	for trackname in tracknames:
# 		songs.add(trackname.text)

# 	songlist = list(songs)

# 	openDownloader(songlist)
# Spotify isnt working because i cant reach spotify playlist via playlist link

def openDownloader(givensonglist):
	driver.get(link2)
	time.sleep(4)
	if type(givensonglist)==list:
		for song in givensonglist:	
			input = driver.find_element_by_xpath("//*[@id='s_input']")
			button = driver.find_element_by_xpath("//*[@id='search-form']/button")
			input.send_keys(song)
			button.click()
			time.sleep(5)
			tempButton = driver.find_element_by_xpath("//*[@id='search-result']/ul/li[1]/a");
			tempButton.click()
			time.sleep(5)

			dbutton = driver.find_element_by_xpath("//*[@id='asuccess']")
			dbutton.click()
			input.clear()
			print(" {adet} songs is downloading".format(adet=len(givensonglist)))
			time.sleep(5)
	if type(givensonglist)==str:
			input = driver.find_element_by_xpath("//*[@id='s_input']")
			button = driver.find_element_by_xpath("//*[@id='search-form']/button")
			input.send_keys(givensonglist)
			button.click()
			time.sleep(5)
			
			if(givensonglist.startswith('http')==False):
				tempButton = driver.find_element_by_xpath("//*[@id='search-result']/ul/li[1]/a");
				tempButton.click()
				time.sleep(5)
				print('False')
				driver.switch_to.window(driver.window_handles[1])

			dbutton = driver.find_element_by_xpath("//*[@id='asuccess']")
			dbutton.click()
			input.clear()
			time.sleep(5)
	else:
		print("empty list error")
	print('Downloading is finished')

if "open.spotify" in link:
	spotify()
else:
	openDownloader(link)