# core/code_generator.py

import re
from config.llm_config import client,MODEL

def get_appium_code(test_case, element_core_map):
    # 关键：Prompt严格限定输出格式，要求和你的示例完全一致
    prompt = f"""
    请将以下测试用例转换为Appium Python代码，必须严格遵循以下格式和规则：
    1. 代码必须被包裹在 `def test_case(driver):` 函数中（参数固定为driver）。
    2. 函数内必须包含 `try-except` 块：
       - try块：执行元素定位（用AppiumBy）和操作（如click()），操作后加time.sleep(1)。
       - except块：捕获Exception，打印错误信息：`print(f"操作失败")`。
    3. 成功时必须打印：`print("具体操作成功")`（如“点击全部按钮成功”）。
    4. 元素定位必须使用元素核心表中的值：{element_core_map}，定位方式映射：XPath→AppiumBy.XPATH。
    5. 仅返回函数代码，无任何额外解释、注释或markdown格式（如```python）。
    6.如果操作执行之后出现了广告关闭按钮，点击广告关闭按钮。
    7.每个操作之后预留2秒钟的缓冲时间

    测试用例：{test_case}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "你是专业的Appium测试工程师，只生成简洁可执行的代码"},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=512
    )
    # 清理代码（去除markdown格式）
    generated_code = response.choices[0].message.content.strip()
    return re.sub(r"```python|```", "", generated_code)