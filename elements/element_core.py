# element_core.py
# 哈啰App元素核心字典（服务列表页+广告弹窗）
element_core_map = {
    "全部按钮": {
        "locator": "XPath",
        "value": "(//android.widget.ImageView[@resource-id='com.jingyao.easybike:id/topIv'])[20]",
        "page": "服务列表页",
        "remark": "对应“全部”功能按钮，通过XPath索引定位"
    },
    "小哈服务站按钮": {
        "locator": "XPath",
        "value": "(//android.widget.ImageView[@resource-id='com.jingyao.easybike:id/imgMain'])[21]",
        "page": "服务列表页",
        "remark": "小哈服务站入口按钮，通过XPath索引定位"
    },
    "广告关闭按钮": {
        "locator": "XPath",
        "value": "(//android.widget.Image[@resource-id='_JK']",
        "page": "广告弹窗",
        "remark": "广告弹窗的关闭按钮，有时不显示，需先判断存在性再操作"
    }
}