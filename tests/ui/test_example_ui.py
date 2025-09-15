import pytest
from pytest import mark
from selenium.webdriver.common.by import By
from utils.ui_helpers import UIHelpers

@mark.ui
@mark.smoke
class TestExampleUI:
    """Example UI test class with pytestomatio integration"""

    @pytest.mark.testomatio("@T95211c7f")
    def test_example_com_title(self, driver, config):
        """Test that example.com has correct title"""
        driver.get("https://example.com")
        assert "Example Domain" in driver.title

    @pytest.mark.testomatio("@T4f937190")
    def test_example_com_heading(self, driver, config):
        """Test that example.com has correct heading"""
        ui_helper = UIHelpers(driver)
        driver.get("https://example.com")

        heading_locator = (By.TAG_NAME, "h1")
        heading_text = ui_helper.get_text(heading_locator)
        assert "Example Domain" in heading_text

    @pytest.mark.testomatio("@T00cde932")
    def test_example_com_paragraph(self, driver, config):
        """
        Test that example.com has informational paragraph
        Steps:
        1. Navigate to example.com
        2. Verify the presence of a paragraph element
        3. Check that the paragraph contains expected text
        """

        ui_helper = UIHelpers(driver)
        driver.get("https://example.com")

        paragraph_locator = (By.TAG_NAME, "p")
        paragraphs = ui_helper.find_elements(paragraph_locator)
        assert len(paragraphs) > 0

        first_paragraph = paragraphs[0].text
        assert "illustrative examples" in first_paragraph.lower()

    @pytest.mark.testomatio("@T55eef41a")
    @mark.regression
    def test_example_com_link_present(self, driver, config):
        """Test that example.com has a link to more information"""
        ui_helper = UIHelpers(driver)
        driver.get("https://example.com")

        link_locator = (By.TAG_NAME, "a")
        assert ui_helper.is_element_present(link_locator), "Link should be present on the page"

        link = ui_helper.find_element(link_locator)
        assert "iana.org" in link.get_attribute("href")