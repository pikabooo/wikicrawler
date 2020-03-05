import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Philosophy(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_wikipedia_org(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/wiki/Special:Random")
        count = 0
        visited = []
        while driver.title != "Philosophy - Wikipedia":
            count += 1
            i = 0
            elems = driver.find_elements_by_xpath("//div[@class='mw-parser-output']/p/a")
            while i < len(elems):
                el = elems[i]
                link = el.get_attribute('href')
                i += 1
                print(link)
                if link not in visited:
                    break
            visited.append(link)
            el.click()
        print("I have found Philosphy after {} clicks.".format(count))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()