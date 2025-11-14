from logger import log_read
from ui import show_instructions
from function_expression import function_expression_main
from function_cash_flow import function_cash_flow_main
from function_time_value import function_time_value_main
from user_settings import get_user_settings

def show_temp():
    print("这是一个占位函数，后续会实现具体功能")

function_info = {
    "0": {
        "description": "使用说明",
        "function": show_instructions,
        "instruction_file": "data/instructions/instructions_overall.txt"
    },
    "1": {
        "description": "算式计算",
        "function": function_expression_main,
        "instruction_file": "data/instructions/instructions_expression.txt"
    },
    "2": {
        "description": "现金流量计算",
        "function": function_cash_flow_main,
        "instruction_file": "data/instructions/instructions_cash_flow.txt"
    },
    "3": {
        "description": "时间价值计算",
        "function": function_time_value_main,
        "instruction_file": "data/instructions/instructions_time_value.txt"
    },
    "l": {
        "description": "查看计算历史",
        "function": log_read
    },
    "s": {
        "description": "用户设置",
        "function": get_user_settings
    }
}