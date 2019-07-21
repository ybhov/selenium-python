from selenium import webdriver
import pandas as pd
import csv
import datetime
#with open("mlbLineups.csv", "w") as f:
#    f.write("players \n")
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

driver = webdriver.Firefox()

driver.get("https://www.baseballpress.com/lineups/" + date)

team = driver.find_elements_by_xpath('//a[@class="mlb-team-logo bc"]')
players = driver.find_elements_by_xpath('//a[@class="player-link"]')
#team = driver.find_elements_by_xpath('//div[@class="col col--min c"]')

numOfTeams=len(team)
firstTeam = 1
start = 0
flip = 0
for i in range(28):
    if flip == 0:
        tempDf = {team[i].text: [players[start].text, players[start+2].text, players[start+3].text, players[start+4].text, players[start+5].text, players[start+6].text, players[start+7].text, players[start+8].text, players[start+9].text, players[start+10].text]}
        flip = 1
        df = pd.DataFrame(tempDf)
    else:
        tempDf = {team[i].text: [players[start+1].text, players[start+11].text, players[start+12].text, players[start+13].text, players[start+14].text, players[start+15].text, players[start+16].text, players[start+17].text, players[start+18].text, players[start+19].text]}
        flip = 0
        df = pd.DataFrame(tempDf)
        start = start + 20
    
    if firstTeam == 1:
        lineups = df
        firstTeam = 0
    else:
        lineups = pd.concat([lineups, df], axis=1)

#test = pd.DataFrame(lineups)
lineups.to_csv('/home/ihovde/Documents/public_html/webScrapingSelenium/todaylineup.csv')

driver.close()
