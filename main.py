from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def open_whatsappweb():
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    wait.until(EC.presence_of_element_located((By.ID, "side")))
    driver.implicitly_wait(2)


def open_contact(contact_name):
    searchbox = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    searchbox.send_keys(Keys.CONTROL + "a")
    searchbox.send_keys(Keys.DELETE)
    searchbox.send_keys(contact_name)

    wait = WebDriverWait(driver, timeout=2)
    side_contact = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]')))
    side_contact.click()


def unselectcontact():
    searchbox = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    searchbox.send_keys(Keys.CONTROL + "a")
    searchbox.send_keys(Keys.DELETE)
    searchbox.send_keys(Keys.ESCAPE)


def send_message(message):
    conversation_input = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
    conversation_input.send_keys(Keys.CONTROL + "a")
    conversation_input.send_keys(Keys.DELETE)
    conversation_input.send_keys(message)
    conversation_input.send_keys(Keys.ENTER)


def send_file(file_path):
    attachment_button = driver.find_element(By.XPATH, '//div[@title="Attach" or @title="Anexar"]')
    attachment_button.click()

    document_option = driver.find_element(By.XPATH, '//input[@type="file" and @accept="*"]')
    document_option.send_keys(file_path)

    send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_button.click()


def send_image(image_path):
    attachment_button = driver.find_element(By.XPATH, '//div[@title="Attach" or @title="Anexar"]')
    attachment_button.click()

    image_option = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_option.send_keys(image_path)

    send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_button.click()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    contacts = ["Marcello Alves", "Ana Clara"]

    message = """ 
    
        Olá {}, tudo bem?
    
        Este é um teste de envio de mensagem via Whatsapp Web.
        
        Segue foto:
        
    """

    open_whatsappweb()

    for contact in contacts:
        open_contact(contact)
        sleep(1)
        send_message(message.format(contact))
        sleep(1)
        send_image("C:\\Users\\Marcello\\Desktop\\1.heic")
        sleep(1)
        unselectcontact()
        sleep(1)

    sleep(200)