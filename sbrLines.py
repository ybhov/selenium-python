from selenium import webdriver
import csv

with open("testResultsSelenium.csv", "w") as f:
    f.write("team, Line \n")

driver = webdriver.Firefox()

driver.get("https://classic.sportsbookreview.com/betting-odds/mlb-baseball/")

teams = driver.find_elements_by_xpath('//span[@class="team-name"]')
#lines = driver.find_elements_by_xpath('//div[@class="eventLine-book-value"]')
#team = driver.find_elements_by_xpath('//span[@rel="635"]')
book = driver.find_elements_by_xpath('//div[@rel="169"]')

second = "placeholder"
num_items = len(teams)
with open("testResultsSelenium.csv", "a") as f:
    for i in range(5):
        lines = book[i+1].text
        line1 = lines.split("\n")[0]
        line2 = lines.split("\n")[1]
        if i == 0:
            f.write(teams[i].text + "," + line1 + "\n")
        elif i % 2 == 1:
            f.write(teams[i].text + "," + line1 + "\n")
        else:
            f.write(teams[i].text + "," + second + "\n")
        second = line2
#        print(team[i].text + " : " + book[i+1].text[0:3])
#       print(book[i].text + " : " + teams[i-1].text)

driver.close()
