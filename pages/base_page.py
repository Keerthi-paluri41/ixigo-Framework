from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        self.wait_for_element(locator).clear()

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def select_by_visible_text(self, locator, text):
        element = self.wait_for_element(locator)
        Select(element).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        element = self.wait_for_element(locator)
        Select(element).select_by_value(value)

    def switch_to_frame(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def switch_to_new_window(self, old_windows, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len(old_windows)
        )

        for window in self.driver.window_handles:
            if window not in old_windows:
                self.driver.switch_to.window(window)
                break