#该文件是主测试文件，将所有执行的步骤都封装在这里
#每个具体的功能又分别封装入utils目录

import logging
import pytest
from jinja2 import Template
from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import read_excel
from utils.extractor import json_extractor, jdbc_extractor
from utils.send_request import send_http_request

class TestRunner:
    # 读测试用例文件中的全部数据，用属性保存即可
    data = read_excel()

    # 提取后的数据需要初始化一个全局的属性来保存，可以使用空字典
    all = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        # 引用全局的 all（建立测试函数内外 all 变量的对应关系）
        all = self.all

        # 根据 all 的值，渲染 case
        case = eval(Template(str(case)).render(all))

        # 初始化 allure 报告
        allure_init(case)

        # 0. 测试用例的描述信息日志
        logging.info(f"0. 用例ID:{case['id']} 模块:{case['feature']} 场景:{case['story']} 标题:{case['title']}")

        # 核心步骤 1：解析请求数据
        request_data = analyse_case(case)

        # 核心步骤 2：发起请求，得到响应结果
        res = send_http_request(**request_data)

        # 核心步骤 3：处理断言
        # HTTP 响应断言
        http_assert(case, res)
        # 数据库断言
        jdbc_assert(case)

        # 核心步骤 4：提取
        # JSON 提取
        json_extractor(case, all, res)
        # 数据库提取
        jdbc_extractor(case, all)