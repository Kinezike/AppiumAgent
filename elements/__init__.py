# 从当前模块导入核心元素字典，供外部直接引用
from .element_core import element_core_map

# 定义模块公开接口，明确可导出的对象
__all__ = ["element_core_map"]