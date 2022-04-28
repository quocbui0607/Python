import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ShopeeCrawler:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="browser_dir\chromedriver.exe")

    def scroll_down(self):
        SCROLL_PAUSE_TIME = 5
        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # try again (can be removed)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)
                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                # check if the page height has remained the same
                if new_height == last_height:
                    # if so, you are done
                    break
                # if not, move on to the next loop
                else:
                    last_height = new_height
                    continue

    def get_items_on_page(self):
        time.sleep(10)
        self.scroll_down()

        products = self.driver.find_elements_by_xpath("//*[contains(@data-sqe, 'item')]")
        # TODO: return the list of products
        list_item = []
        for item in products:
            name = item.find_element_by_class_name('O6wiAW').text
            price = item.find_element_by_class_name('_2lBkmX').text
            list_item.append([name, price])
        pass

    def get_next_page_search(self):
        try:
            page_controller = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopee-page-controller")))
            last_button = page_controller.find_elements_by_xpath(".//button")[-1]
            if last_button:
                last_button.click()
        except NameError:
            print("Error occurred while click to the next page")

    def do_crawl(self):
        self.driver.get("https://shopee.vn/")
        time.sleep(5)

        popup_close_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'shopee-popup__close-btn')]")))
        if popup_close_button:
            popup_close_button.click()

        self.driver.execute_script("window.stop();")
        self.driver.maximize_window()
        time.sleep(1)

        search_input = self.driver.find_element_by_xpath(
            "//input[contains(@class, 'shopee-searchbar-input__input')]")
        # TODO: Đọc từ file csv từ khóa cần tìm kiếm, loop tìm kiếm
        search_input.send_keys("Nội thất kiểu Hàn")
        time.sleep(3)
        search_button = self.driver.find_element_by_class_name("btn--s")
        # search_button = self.driver.find_element_by_xpath("//button[contains(@class, 'btn--s')]")
        search_button.click()


        while True:
            # TODO: nhớ xác định số trang để stop loop nhé các bạn
            self.get_items_on_page()
            # self.get_next_page_search()
            time.sleep(5)
            # TODO: thêm vòng lặp để click next page sau khi get products
            # total = self.driver.find_element_by_class_name("shopee-mini-page-controller__total")
            # next_button = self.driver.find_element_by_class_name("shopee-icon-button shopee-icon-button--right")
            # next_button.click()
        # END LOOP

        time.sleep(10)
        self.driver.close()


if __name__ == '__main__':
    crawler = ShopeeCrawler()
    crawler.do_crawl()
