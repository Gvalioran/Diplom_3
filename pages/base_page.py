from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        driver.implicitly_wait(10)
        self.driver = driver

    def transition_site(self, url):
        return self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def expectation_url(self, url, time=30):
        return WebDriverWait(self.driver, time).until(ec.url_to_be(url))

    def find_element_located(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))

    def find_element_located_click(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).click()

    def find_element_located_input(self, locator, text, time=30):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).send_keys(text)

    def find_elements_located(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator))

    def get_attribute(self, locator, attribute, time=30):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).get_attribute(attribute)

    def get_element_text(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).text

    def drag_and_drop(self, what, where):
        return ActionChains(self.driver).drag_and_drop(what, where).perform()
