from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://classic.sportsbookreview.com/betting-odds/mlb-baseball/")

#teams = driver.find_elements_by_xpath('//span[@class="team-name"]')
#lines = driver.find_elements_by_xpath('//div[@class="eventLine-book-value"]')
team = driver.find_elements_by_xpath('//span[@rel="635"]')
book = driver.find_elements_by_xpath('//div[@rel="169"]')


num_items = len(team)
for i in range(1):
    print(team[i].text + " : " + book[i+1].text[0:3])
#    print(book[i].text + " : " + teams[i-1].text)

driver.close()
