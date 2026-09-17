import pytest
from selenium import webdriver

from ixigo.utilities.screenshot import take_screenshot


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()

    options.add_argument(
        r"--user-data-dir=C:\SeleniumProfiles\IxigoTestProfile"
    )
    options.add_argument("--profile-directory=Default")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # Open Ixigo and clear the previous Ixigo login session
    driver.get("https://www.ixigo.com/")
    driver.delete_all_cookies()

    driver.execute_script(
        "window.localStorage.clear();"
        "window.sessionStorage.clear();"
    )

    driver.get("https://www.ixigo.com/")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")

        if driver:
            take_screenshot(driver, item.name)