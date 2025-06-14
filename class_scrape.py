from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_class_names(driver, wait, tab_index, element_ids):
    tab_nav_tabs[tab_index].click()
    all_classes = []
    for element_id in element_ids:
        wait.until(EC.visibility_of_element_located((By.ID, element_id)))
        wrapper = driver.find_element(By.ID, element_id)
        div = wrapper.find_element(By.CLASS_NAME, "fsElementContent")
        classes = div.find_elements(By.TAG_NAME, "h4")
        all_classes.extend([class_element.text for class_element in classes])
    return all_classes

driver.get('https://www.dextersouthfield.org/course-catalog-welcome/course-catalog-25')
print(driver.title)

wait = WebDriverWait(driver, timeout=2)

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "fsTabsNav")))
tab_nav_wrapper = driver.find_element(By.CLASS_NAME, "fsTabsNav")
tab_nav_li = tab_nav_wrapper.find_elements(By.TAG_NAME, "li")
tab_nav_tabs = [li.find_element(By.TAG_NAME, "a") for li in tab_nav_li]

subject_elements = {
    0: ["fsEl_22111", "fsEl_22113"],  # English
    1: ["fsEl_22114", "fsEl_22115"],  # Math
    2: ["fsEl_22117", "fsEl_22118"],  # Science
    3: ["fsEl_22121", "fsEl_22125"],  # History
    5: ["fsEl_22133", "fsEl_22145", "fsEl_22144"]   # Language
}

# Collect all class names
all_classes = {}
for tab_index, element_ids in subject_elements.items():
    subject_name = tab_nav_tabs[tab_index].text
    all_classes[subject_name] = get_class_names(driver, wait, tab_index, element_ids)
    print(f"\n{subject_name} Classes:")
    print(all_classes[subject_name])

driver.quit()
