from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Optional, Tuple

class UIHelpers:
    """Helper methods for UI testing"""

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """Find element with wait"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Find multiple elements with wait"""
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator: Tuple[str, str]) -> None:
        """Click element when clickable"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator: Tuple[str, str], text: str) -> None:
        """Send keys to element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Get text from element"""
        element = self.find_element(locator)
        return element.text

    def wait_for_element_visible(self, locator: Tuple[str, str]) -> WebElement:
        """Wait for element to be visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator: Tuple[str, str]) -> bool:
        """Wait for element to be invisible"""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def is_element_present(self, locator: Tuple[str, str]) -> bool:
        """Check if element is present"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def scroll_to_element(self, locator: Tuple[str, str]) -> None:
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)