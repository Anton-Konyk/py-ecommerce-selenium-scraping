from dataclasses import dataclass
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common import (
    NoSuchElementException,
    ElementClickInterceptedException,
    TimeoutException
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


BASE_URL = "https://webscraper.io/"
HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/more")
COMPUTERS = urljoin(BASE_URL, "test-sites/e-commerce/more/computers")
LAPTOPS = urljoin(BASE_URL, "test-sites/e-commerce/more/computers/laptops")
TABLETS = urljoin(BASE_URL, "test-sites/e-commerce/more/computers/tablets")
PHONES = urljoin(BASE_URL, "test-sites/e-commerce/more/phones")
TOUCH = urljoin(BASE_URL, "test-sites/e-commerce/more/phones/touch")
ALL_PAGES = [HOME_URL, COMPUTERS, LAPTOPS, TABLETS, PHONES, TOUCH]


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


def check_more_button(driver: WebDriver) -> None:
    try:
        wait = WebDriverWait(driver, 1)
        button = wait.until(
            ec.presence_of_element_located((By.CLASS_NAME,
                                            "ecomerce-items-scroll-more")))
        while button.is_displayed():
            try:
                button = wait.until(
                    ec.element_to_be_clickable((By.CLASS_NAME,
                                                "ecomerce-items-scroll-more")))
                button.click()
                time.sleep(0.5)
            except ElementClickInterceptedException:
                pass
    except TimeoutException:
        pass
    except NoSuchElementException:
        pass

def check_cookies(driver: WebDriver) -> None:
    try:
        button = driver.find_element(By.CLASS_NAME, "acceptCookies")
        while button.is_displayed():
            button.click()
            time.sleep(0.5)
    except NoSuchElementException:
        pass


def parse_single_product(driver: WebDriver) -> Product:

    return Product(
        title=driver.find_element(By.CLASS_NAME, "title").
        get_attribute("title"),
        description=driver.find_element(By.CLASS_NAME, "description").text,
        price=float(driver.find_element(By.CLASS_NAME, "price").
                    text.replace("$", "")),
        rating=len((driver.find_element(By.CLASS_NAME, "ratings")).
                   find_elements(By.TAG_NAME, "span")),
        num_of_reviews=int(
            driver.find_element(By.CLASS_NAME, "review-count").
            text.split()[0])
    )

def get_all_products() -> None:
    pass


if __name__ == "__main__":
    get_all_products()
