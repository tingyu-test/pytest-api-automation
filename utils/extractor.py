#该文件的作用是封装json提取和jdbc提取，便于test_runner.py调用

import logging
import allure
import jsonpath
from utils.send_request import send_jdbc_request

def json_extractor(case, all, res):
    if case["jsonExData"]:
        with allure.step("4. JSON 提取"):
            # 首先要把 jsonExData 的 key，value 拆开
            for key, value in eval(case["jsonExData"]).items():
                value = jsonpath.jsonpath(res.json(), value)[0]
                # print(key)
                # print(value)
                all[key] = value
                # print(all)
            #添加提取数据的日志
            logging.info(f"4. JSON 提取，根据{case['jsonExData']}提取数据，此时全局变量为：{all}")

def jdbc_extractor(case, all):
    if case["sqlExData"]:
        with allure.step("4. JDBC 提取"):
            for key, value in eval(case["sqlExData"]).items():
                # print(key)
                # print(value)
                value = send_jdbc_request(value)
                # print(value)
                all[key] = value
                # print(all)
            #添加jdbc提取数据的日志
            logging.info(f"4. JDBC 提取，根据{case['sqlExData']}提取数据，此时全局变量为:{all}")