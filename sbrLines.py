from selenium import webdriver
import csv

with open("testResultsSelenium.csv", "w") as f:
    f.write("Team, Heritage, Bovada, Pinnacle \n")

driver = webdriver.Firefox()

driver.get("https://classic.sportsbookreview.com/betting-odds/mlb-baseball/")

teams = driver.find_elements_by_xpath('//span[@class="team-name"]')
heritage = driver.find_elements_by_xpath('//div[@rel="169"]')
bovada = driver.find_elements_by_xpath('//div[@rel="999996"]')
pinnacle = driver.find_elements_by_xpath('//div[@rel="238"]')

second = "placeholder"
num_items = len(teams)
j = 1
with open("testResultsSelenium.csv", "a") as f:
    for i in range(30):
        hLines = heritage[j].text
        hLine1 = hLines.split("\n")[0]
        hLine2 = hLines.split("\n")[1]
        bLines = bovada[j].text
        bLine1 = bLines.split("\n")[0]
        bLine2 = bLines.split("\n")[1]
        pLines = pinnacle[j].text
        pLine1 = pLines.split("\n")[0]
        pLine2 = pLines.split("\n")[1]
        teamAndPitcher = teams[i].text
        team = teamAndPitcher.split(" ")[0]
        print(team)
        if i == 0:
            f.write(team + "," + hLine1 + "," + bLine1 + "," + pLine1 + "\n")
        elif i % 2 == 1:
            f.write(team + "," + hLine2 + "," + bLine2 + "," + pLine2 + "\n")
        else:
            f.write(team + "," + hLine1 + "," + bLine1 + "," + pLine1 + "\n")
        if i % 2 ==1:
            j = j + 1

driver.close()
