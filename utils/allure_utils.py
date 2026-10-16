#该文件的作用是封装allure方法，便于test_runner.py调用

# ./utils/allure_utils.py
import allure

def allure_init(case):
    allure.dynamic.feature(case["feature"])     #使用allure.dynamic，会在allure报告中显示模块/场景/标题等
    allure.dynamic.story(case["story"])
    # allure.dynamic.title(case["title"])
    allure.dynamic.title(f"ID:{case['id']}-{case['title']}")

