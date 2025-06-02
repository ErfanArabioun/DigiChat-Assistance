from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Chrome Settings
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
options.add_argument("--start-maximized")

# Links list for processing
URLS = [
        "https://www.digikala.com/faq/category/1/",
        "https://www.digikala.com/faq/category/2/",
        "https://www.digikala.com/faq/category/3/",
        "https://www.digikala.com/faq/category/4/",
        "https://www.digikala.com/faq/category/5/",
        "https://www.digikala.com/faq/category/6/",
        "https://www.digikala.com/faq/category/8/",
        "https://www.digikala.com/faq/category/10/",
        "https://www.digikala.com/faq/category/16/",
        "https://www.digikala.com/faq/category/22/",
        "https://www.digikala.com/faq/category/38/",
        "https://www.digikala.com/faq/category/39/",
        "https://www.digikala.com/faq/category/40/",
        "https://www.digikala.com/faq/category/44/",
        "https://www.digikala.com/faq/category/325/",
        "https://www.digikala.com/faq/category/339/",
        "https://www.digikala.com/faq/category/341/",
        "https://www.digikala.com/faq/category/342/",
        "https://www.digikala.com/faq/category/346/",
        "https://www.digikala.com/faq/category/350/",
        "https://www.digikala.com/faq/category/351/",
        "https://www.digikala.com/faq/category/353/",
        "https://www.digikala.com/faq/category/354/",
        "https://www.digikala.com/faq/category/356/",
        "https://www.digikala.com/faq/category/357/",
        "https://www.digikala.com/faq/category/359/"  
]     # "https://www.digikala.com/faq/category/358/" ---> Link Not work!


# Saving the data
categories = []
questions = []
answers = []
links = []

try:
    # Driver runing
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 30)

    for url in URLS:
        driver.get(url)
        time.sleep(3)

        # # Closing Pop-ups
        # try:
        #     close_button = wait.until(EC.element_to_be_clickable(
        #         (By.XPATH, '//*[@id="modal-root"]/div/div/div/div/div[2]/div/div/button[2]/div')))
        #     close_button.click()
        # except:
        #     print("No pop-up found, continuing...")

        # Finding the category's name
        try:
            category_name = driver.find_element(By.CSS_SELECTOR, 'div.flex > p.grow > span.relative').text.strip()
        except:
            category_name = "Unknown Category"

        # Finding the Q&A element
        faq_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.pb-11 > div")))
        print(f"Processing {len(faq_items)} questions in category '{category_name}'.")

        for index, item in enumerate(faq_items):
            try:
                # Scroll to each question
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", item)
                time.sleep(1)

                # Extracting the questions
                question_text = item.find_element(By.TAG_NAME, "div").text
                questions.append(question_text)
                item.click()
                time.sleep(2)

                # Extracting the answers
                answer_elements = item.find_elements(By.CSS_SELECTOR, "div.text-body-1 p")
                full_answer = " ".join([a.text.strip() for a in answer_elements])
                answers.append(full_answer if full_answer else "The Answer Not Found!")

                # Extracting the links
                try:
                    link_elements = item.find_elements(By.TAG_NAME, 'a')
                    extracted_links = [link.get_attribute('href') for link in link_elements if link.get_attribute('href')] # if link_element else ""
                except:
                    link_href = ""
                links.append("\n".join(extracted_links) if extracted_links else "")

                # Saving the category
                categories.append(category_name)

                print(f"Processed Q{index + 1}: {question_text[:30]}...")

            except Exception as ERR:
                print(f"Error processing Q{index + 1}: {ERR}")
                categories.append(category_name)
                questions.append("Error extracting question")
                answers.append("Error extracting answer")
                links.append("")
                continue

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    # Storing the data in CSV format
    data = pd.DataFrame({
        "Category": categories,
        "Question": questions,
        "Answer": answers,
        "Link": links
    })
    data.to_csv("DIGIKALA_FAQ_ALL.csv", index=False, encoding='utf-8-sig')
    print("Data saved successfully in 'DIGIKALA_FAQ_ALL.csv'.")

    driver.quit()