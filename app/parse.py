from dataclasses import dataclass
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


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
