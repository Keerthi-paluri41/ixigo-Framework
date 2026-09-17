from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage



class FlightSearchPage(BasePage):

    CLOSE_POPUP = (
        By.XPATH,
        "//button[@id='closeButton']"
    )

    FROM_FIELD = (
        By.XPATH,
        "//p[@data-testid='originId']/ancestor::div[contains(@class,'flex-1')][1]"
    )

    FROM_INPUT = (
        By.XPATH,
        "//input[contains(@class,'outline-none')]"
    )

    TO_INPUT = (
        By.XPATH,
        "//label[normalize-space()='To']/following-sibling::input"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    DEPARTURE_DATE = (
        By.XPATH,
        "//p[@data-testid='departureDate']"
    )

    SEARCH_RESULTS = (
        By.XPATH,
        "//p[normalize-space()='Sort by']"
    )

    # def close_popup_if_present(self):
    #     elements = self.driver.find_elements(*self.POPUP_CLOSE)
    #
    #     if elements:
    #         try:
    #             elements[0].click()
    #         except Exception:
    #             pass
    # def close_popup_if_present(self):
    #     try:
    #         popup = WebDriverWait(self.driver, 3).until(
    #             lambda driver: driver.find_element(*self.CLOSE_POPUP)
    #         )
    #
    #         if popup.is_displayed():
    #             popup.click()
    #
    #     except Exception:
    #         pass
    def close_popup_if_present(self):
        try:
            popup = self.driver.find_element(
                By.XPATH,
                "//button[@id='closeButton']"
            )

            if popup.is_displayed():
                self.driver.execute_script(
                    "arguments[0].click();",
                    popup
                )

        except Exception:
            pass

    def click_from_field(self):
        self.click(self.FROM_FIELD)


    def enter_from_city(self, city):
        self.send_keys(self.FROM_INPUT, city)


    # def select_from_city(self, city):
    #     city_suggestion = (
    #         By.XPATH,
    #         f"//p[contains(normalize-space(),'{city}')]"
    #     )
    #     self.click(city_suggestion)
    def select_from_city(self, city):
        city_suggestion = (
            By.XPATH,
            f"//div[@role='listitem'][.//span[contains(normalize-space(), '{city},')]]"
        )
        self.click(city_suggestion)
    # def select_from_city(self, city):
    #     city_suggestion = (
    #         By.XPATH,
    #         f"//p[.//span[contains(normalize-space(),'{city}')]]/ancestor::div[@role='listitem'][1]"
    #     )
    #     self.click(city_suggestion)


    # def enter_to_city(self, city):
    #     self.send_keys(self.FROM_INPUT, city)

    def enter_to_city(self, city):
        self.send_keys(self.TO_INPUT, city)


    # def select_to_city(self, city):
    #     city_suggestion = (
    #         By.XPATH,
    #         f"//p[contains(normalize-space(),'{city}')]"
    #     )
    #     self.click(city_suggestion)
    # def select_to_city(self, city):
    #     city_suggestion = (
    #         By.XPATH,
    #         f"//p[contains(normalize-space(), '{city},')]"
    #     )
    #
    #     self.click(city_suggestion)
    def select_to_city(self, city):
        city_suggestion = (
            By.XPATH,
            f"//div[@role='listitem'][.//span[contains(normalize-space(), '{city},')]]"
        )
        self.click(city_suggestion)
    # def select_to_city(self, city):
    #     city_suggestion = (
    #         By.XPATH,
    #         f"//p[.//span[contains(normalize-space(),'{city}')]]/ancestor::div[@role='listitem'][1]"
    #     )
    #     self.click(city_suggestion)


    def select_departure_date(self, departure_date):
        date_locator = (
            By.XPATH,
            f"//abbr[@aria-label='{departure_date}']"
        )
        self.click(date_locator)

    def click_departure_date(self):
        self.click(self.DEPARTURE_DATE)


    def click_search(self):
        self.click(self.SEARCH_BUTTON)


    # main method which connects all small methods
    def search_flight(self, from_city, to_city, departure_date):

        self.close_popup_if_present()

        self.click_from_field()

        self.enter_from_city(from_city)
        self.select_from_city(from_city)

        self.close_popup_if_present()

        self.enter_to_city(to_city)

        self.close_popup_if_present()

        self.select_to_city(to_city)

        self.close_popup_if_present()

        self.select_departure_date(departure_date)

        self.close_popup_if_present()

        self.click_search()


    def is_search_results_displayed(self):
        return self.wait_for_element(
            self.SEARCH_RESULTS
        ).is_displayed()