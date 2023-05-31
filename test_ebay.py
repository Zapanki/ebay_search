import pytest
from selenium.webdriver.common.by import By

base_url="https://www.ebay.com/"

@pytest.mark.parametrize("item",
                         [
                             "Mercedes"
                         ])
@pytest.mark.ebay
def test_ebay_search(browser, item):
    browser.get(base_url)
    #browser.find_element(By.ID, "gdpr-banner-accept").click()
    browser.find_element(By.ID, "gh-shop-a").click()
    browser.find_element(By.CSS_SELECTOR, "[_sp='m570\.l3416']").click()
    browser.find_element(By.CSS_SELECTOR, "div#ebay-motors > div > div:nth-of-type(1) > .cat-wrapper > .sub-cats > .view-more-link > a").click()
    browser.find_element(By.ID, "gh-la").click()
    browser.find_element(By.ID, "gh-ac").send_keys(item)
    browser.find_element(By.ID, "gh-btn").click()
    assert item in browser.title