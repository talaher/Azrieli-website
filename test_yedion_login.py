import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

@pytest.fixture
def driver():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://yedion.jce.ac.il/yedion/fireflyweb.aspx?prgname=login")
    yield driver
    driver.quit()

def test_login_valid1(driver):
    wait = WebDriverWait(driver, 50)
    try:
        # Click on "כניסה למערכת" link
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        # Enter email
        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)

        # Click next
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        # Enter password
        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("ILOVEmyself213*")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
        time.sleep(3)

        # Wait for the specific element and click it
        target_element = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div')
            )
        )
        target_element.click()

        # Click the confirmation button
        confirm_button = wait.until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        confirm_button.click()

    except Exception as e:
        print("Test 1 Failed:", e)
        raise  # re-raise exception to mark the test as failed

# --- Test Case 2: Invalid Username ---
def test_invalid_username(driver):
    wait = WebDriverWait(driver, 50)
    try:

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("invalid_user@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        # Expect error message
        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="usernameError"]')))
        if error.is_displayed():
            print("Test 2 Passed: Invalid username error shown.")
        else:
            print("Test 2 Failed: Error message not shown.")
    except Exception as e:
        print("Test 2 Failed:", e)

# --- Test Case 3: Invalid password -
def test_invalid_password(driver):
    wait = WebDriverWait(driver, 50)
    try:

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()
        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("ILOVEmys*")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        # Expect error message
        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordError"]')))
        if error.is_displayed():
            print("Test 3 Passed: Invalid password error shown.")
        else:
            print("Test 3 Failed: Error message not shown.")
    except Exception as e:
        print("Test 3 Failed:", e)

# --- Test Case 4: forget password link -
def test_click_forgot_password(driver):
    wait = WebDriverWait(driver, 50)
    try:
        # Your existing test code

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()
        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("wrong pass")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="idA_PWD_ForgotPassword"]'))
        )
        element.click()
        print("Clicked on forgot password successfully.")
    except Exception as e:
        print("Test Failed:", e)

# --- Test Case 5: null user name -
def test_invalid_login(driver):
    wait = WebDriverWait(driver, 50)
    try:

        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת")))
        login_link.click()

        # By not entering anything, clicking login
        submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        submit_btn.click()



        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="usernameError"]')))
        if error.is_displayed():
            print("Test 5: Empty fields error shown.")
        else:
            print("Test 5: Validation not displayed.")
    except Exception as e:
        print("Test 5 Failed:", e)

# --- Test Case 6: valid login text
def test_login_valid2(driver):
    wait = WebDriverWait(driver, 50)
    try:

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()
        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("ILOVEmyself213*")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        # Wait for the specific calling element and click it

        target_element = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div'))
        )
        target_element.click()
        time.sleep(30)
        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

        button = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        button.click()

        print("Test 1 Passed: Logged in successfully.")
    except Exception as e:
        print("Test 1 Failed:", e)

# --- Test Case 7: invalid login text

def test_login_invalid2(driver):
    wait = WebDriverWait(driver, 5)
    try:

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()
        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("ILOVEmyself213*")
        time.sleep(3)


        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        # Wait for the specific calling element and click it

        target_element = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div'))
        )
        target_element.click()
        time.sleep(5)

        text_box = wait.until(EC.presence_of_element_located((By.ID, "idTxtBx_SAOTCC_OTC")))
        text_box.clear()
        text_box.send_keys("12345")

        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

        # Expect error message
        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSpan_SAOTCC_Error_OTC"]')))
        if error.is_displayed():
            print("Test 7 Passed: Invalid verification error shown.")
        else:
            print("Test 7 Failed: Error message not shown.")

    except Exception as e:
        print("Test 1 Failed:", e)

# --- Test Case 8: invalid login text null

def test_login_invalid3(driver):
    wait = WebDriverWait(driver, 5)
    try:
        driver.get("https://yedion.jce.ac.il/yedion/fireflyweb.aspx?prgname=login")
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()
        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("ILOVEmyself213*")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        # Wait for the specific calling element and click it

        target_element = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div/div/div[2]/div'))
        )
        target_element.click()
        time.sleep(3)
        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()

        # Expect error message
        error = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="idSpan_SAOTCC_Error_OTC"]')))
        if error.is_displayed():
            print("Test 8 Passed: null verification code error shown.")
        else:
            print("Test 8 Failed: Error message not shown.")

    except Exception as e:
        print("Test 1 Failed:", e)

# --- Test Case 9: new student login
def test_new_student_login_valid1(driver):
    try:

        driver.find_element(By.LINK_TEXT, "שכחתי סיסמה | סטודנט חדש").click()
    except Exception as e:
        print("Test 1 Failed:", e)

# --- Test Case 10: help page

def test_helping_page_valid1(driver):
    try:

        driver.find_element(By.LINK_TEXT, "כאן").click()
    except Exception as e:
        print("Test 1 Failed:", e)


# === LOGIN FIXTURE ===
@pytest.fixture
def logged_in_driver(driver):
    wait = WebDriverWait(driver, 50)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה למערכת"))).click()

        username = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        username.clear()
        username.send_keys("batoolab@post.jce.ac.il")
        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

        password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password.clear()
        password.send_keys("ILOVEmyself213*")
        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
        time.sleep(3)

        target_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div')))
        target_element.click()

        confirm_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        confirm_button.click()

        return driver
    except Exception as e:
        print("Login failed:", e)
        raise

# === MAIN TEST FUNCTION ===
def test_check_assignments(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)

    try:
        # Click "אתרי קורסים"
        courses = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='אתרי קורסים']/ancestor::button")))
        courses.click()

        # Click "הגשת עבודות"
        assignments = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="TMenu9"]/div/div[5]/button')))
        assignments.click()

        # Select semester 1
        semester_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="select2-R1C2-container"]')))
        semester_dropdown.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='1']"))).click()

        # Select year 2023
        year_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="select2-R1C5-container"]')))
        year_dropdown.click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(text(),'2023')]"))).click()

        # Click "מעבר שנה"
        year_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="main-content"]/article/form/div[2]/input[1]')))
        year_button.click()

        # Expand assignment section
        expand_section = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="H3_1"]')))
        expand_section.click()

    except Exception as e:
        print("Assignment check failed:", e)
        raise


def test_open_Model_site(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)

    try:
        # Click "אתרי קורסים"
        courses = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='אתרי קורסים']/ancestor::button")))
        courses.click()
        time.sleep(1)

        # Click "מעבר למודל" (first item in the dropdown)
        model_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="TMenu9"]/div/div[1]/button')))
        model_button.click()
        time.sleep(2)

        # Optionally, assert that Moodle page has opened
        # For example:
        assert "moodle" in driver.current_url.lower() or "מודל" in driver.page_source

    except Exception as e:
        print("Opening Moodle site failed:", e)
        raise


def test_open_course_sites(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)

    try:
        # Click "אתרי קורסים"
        courses = driver.find_element(By.XPATH, "//span[text()='אתרי קורסים']/ancestor::button")
        courses.click()
        time.sleep(1)

        # Click "כניסה לאתרי קורסים"
        course_sites = driver.find_element(By.XPATH, '//*[@id="TMenu9"]/div/div[2]/button')
        course_sites.click()
        time.sleep(1)

        # Select Semester (1)
        semester_dropdown = driver.find_element(By.XPATH, '//*[@id="select2-R1C2-container"]')
        semester_dropdown.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[text()='1']").click()
        time.sleep(1)

        # Select Year (e.g., 2023)
        year_dropdown = driver.find_element(By.XPATH, '//*[@id="select2-R1C1-container"]')
        year_dropdown.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[contains(text(), '2023')]").click()
        time.sleep(1)

        # Click רענון תצוגה (refresh)
        refresh_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/form/div[1]/div[4]/a')
        refresh_button.click()
        time.sleep(5)

        # Click the + to expand course list
        driver.find_element(By.XPATH, '//*[@id="ID_20241"]').click()
        time.sleep(2)


    except Exception as e:
        print("Opening course sites failed:", e)
        raise
      
