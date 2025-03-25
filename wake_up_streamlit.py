from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Add your Streamlit app URLs here
STREAMLIT_APPS = [
    "https://app-demogit-mybvkhnzd5ux26xaqhu2na.streamlit.app/",
]

def wake_up_streamlit():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    for app_url in STREAMLIT_APPS:
        try:
            print(f"Attempting to wake up: {app_url}")
            driver.get(app_url)
            
            # 等待頁面加載（最多等待60秒）
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            print(f"Successfully loaded: {app_url}")
            time.sleep(5)  # 等待5秒確保頁面完全加載
            
        except Exception as e:
            print(f"Error waking up {app_url}: {str(e)}")
    
    driver.quit()

if __name__ == "__main__":
    wake_up_streamlit()
