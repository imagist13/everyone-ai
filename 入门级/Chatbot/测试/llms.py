import os
from langchain_openai import ChatOpenAIOpenAI
import logging

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 模型配置字典

MODEL_CONFIGS = {
    "openai": {
        "base_url": "https://api.deepseek.com",
        "api_key": os.getenv(""),
        "model": "deepseek-chat"
    },
    "qwen": {
        "base_url": "https://api.qwen.aliyun.com/v1",
        "api_key": os.getenv("QWEN_API_KEY"),
        "model": "qwen-plus"
    }
}

def get_llm(llm_type: str = DEFAULT_LLM_TYPE) -> ChatOpenAI:
    """
    获取LLM实例的封装函数，提供默认值和错误处理

    Args:
        llm_type (str): LLM类型

    Returns:
        ChatOpenAI: LLM实例
    """
    try:
        return initialize_llm(llm_type)
    except LLMInitializationError as e:
        logger.warning(f"使用默认配置重试: {str(e)}")
        if llm_type != DEFAULT_LLM_TYPE:
            return initialize_llm(DEFAULT_LLM_TYPE)
        raise  # 如果默认配置也失败，则抛出异常
