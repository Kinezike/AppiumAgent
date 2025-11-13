🛠️ 快速开始
1. 环境准备
# 安装依赖
pip install appium-python-client openai

# 启动 Appium Server
appium --port 4723
2. 配置设备与应用
编辑 config/appium_config.py：
DESIRED_CAPS = {
    "deviceName": "YOUR_DEVICE_ID",      # adb devices 查看
    "appPackage": "com.jingyao.easybike",
    "appActivity": "com.hellobike.atlas.business.portal.MainActivityDefaultIcon",
    # ...
}
3. 配置大模型（可选）
编辑 config/llm_config.py（支持任何兼容 OpenAI API 的模型）：
    LLM_CLIENT = OpenAI(
    base_url="https://api.your-llm-provider.com/v1",
    api_key="your-api-key"
)
4. 定义元素定位
在 elements/element_core.py 中维护按钮映射：
element_core_map = {
    "全部按钮": {
        "locator": "XPath",
        "value": "(//android.widget.ImageView[@resource-id='...'])[20]"
    },
    "广告关闭按钮": {
        "locator": "XPath",
        "value": "//android.widget.Image[@resource-id='_JK']"
    }
}
5. 运行测试
# main.py 中修改测试步骤
test_steps = """
1.点击“全部“按钮
2.点击小哈服务站按钮
"""

python main.py
🧠 工作原理
SVG content

安全执行：exec() 在干净命名空间运行，避免变量冲突
健壮异常处理：每个操作独立 try-catch，失败不影响后续步骤
广告自适应：广告关闭逻辑独立，无广告时自动跳过
