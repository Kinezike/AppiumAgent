# main.py
from config.appium_config import APPIUM_SERVER_URL, DESIRED_CAPS
from elements.element_core import element_core_map
from core.code_generator import get_appium_code
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options

import time

if __name__ == "__main__":
    driver = webdriver.Remote(
        APPIUM_SERVER_URL,
        options=UiAutomator2Options().load_capabilities(DESIRED_CAPS)
    )
    driver.implicitly_wait(10)

    try:
        test_case = """
        1.点击“全部“按钮
        """
        # 生成代码（假设生成的是 def test_case(driver): ...）
        appium_code = get_appium_code(test_case, element_core_map)
        print(f"\n生成的代码：\n{appium_code}\n")

        # 1. 加载生成的函数（仅定义函数，不执行）
        exec(appium_code)

        # 2. 关键：调用生成的函数，传入driver
        test_case(driver)  # 假设生成的函数名为test_case

        print("测试执行完成！")
    except Exception as e:
        print(f"测试失败：{str(e)}")
    finally:
        time.sleep(3)
        driver.quit()