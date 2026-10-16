#测试文件，变更项目时，只需变更config.py和date目录下的xlsx，执行此run文件即可

# run.py
import os
import pytest

# --alluredir ./report/json_report 指定一个目录，并生成中间结果
# --clean-alluredir 每次运行会清空中间结果

# os.system(命令) 相当于在 cmd 中执行命令
# allure generate 中间结果目录 -o 目标 html 报告目录 --clean

if __name__ == "__main__":
    pytest.main(["-vs", "./testcases/test_runner.py", "--alluredir", "./report/json_report", "--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")
