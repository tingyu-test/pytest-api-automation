##该文件的作用是封装从excel_utils中解析数据，便于test_runner.py调用

# ./utils/analyse_case.py
import logging
import allure
from config.config import BASE_URL

@allure.step("1. 解析请求数据")
def analyse_case(case):
    method = case["method"]
    url = BASE_URL + case["path"]
    headers = eval(case["headers"]) if isinstance(case["headers"], str) else None
    params = eval(case["params"]) if isinstance(case["params"], str) else None
    data = eval(case["data"]) if isinstance(case["data"], str) else None
    json = eval(case["json"]) if isinstance(case["json"], str) else None
    files = eval(case["files"]) if isinstance(case["files"], str) else None

    request_data = {
        "method": method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data,
        "json": json,
        "files": files,
    }
    #添加解析数据的日志
    logging.info(f"1. 解析请求数据，请求数据为:{request_data}")
    return request_data