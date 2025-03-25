from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Streamlit app URL
STREAMLIT_APPS = [
    "https://app-demogit-mybvkhnzd5ux26xaqhu2na.streamlit.app/",
]

def wake_up_streamlit():
    print("Starting wake up process...")
    
    # 設置Chrome選項
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # 使用系統安裝的ChromeDriver
    chrome_driver_path = "/usr/bin/chromedriver"
    print(f"Using ChromeDriver at: {chrome_driver_path}")
    
    try:
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Chrome WebDriver initialized successfully")
        
        for app_url in STREAMLIT_APPS:
            try:
                print(f"\nAttempting to wake up: {app_url}")
                driver.get(app_url)
                print("Initial page load complete")
                
                # 等待頁面加載
                print("Waiting for page to be fully loaded...")
                WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                
                # 額外等待確保頁面完全加載
                print("Waiting additional time for full page load...")
                time.sleep(30)
                
                print(f"Page title: {driver.title}")
                print(f"Current URL: {driver.current_url}")
                print("Successfully loaded and waited for the page")
                
            except Exception as e:
                print(f"Error while processing {app_url}: {str(e)}")
                print("Page source at error:", driver.page_source)
        
        driver.quit()
        print("\nChrome WebDriver closed successfully")
        
    except Exception as e:
        print(f"Critical error in wake_up_streamlit: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        wake_up_streamlit()
    except Exception as e:
        print(f"Script failed: {str(e)}")
        exit(1)
