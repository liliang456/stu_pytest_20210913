import logging
import time
import allure

from unit.readResultRelevance import get_relevance
from unit.apiSend import send_request


def ini_request(case_dict, _path, relevance=None):
    """
    用例前提条件执行，提取关键值c
    :param case_dict: 用例对象
    :param relevance: 关联对象
    :param _path: case路径
    :return:
    """
    if isinstance(case_dict["premise"], list):
        logging.info("执行测试用例前置接口")
        with allure.step("接口关联请求"):
            for i in case_dict["premise"]:
                relevance_list = {}
                for j in range(0, 1):
                    code, data = send_request(i, case_dict["test_info"].get("host"),
                                              i["address"], _path,relevance_list)
                    # print('111data----',data)
                    if not data:
                        with allure.step("接口请求失败！等待三秒后重试！"):
                            pass
                    if i["relevance"]:
                        if len(i["relevance"]):
                            relevance = get_relevance(data, i["relevance"], relevance={})
                            if isinstance(relevance, bool):
                                with allure.step("从结果中提取关联键的值失败！等待3秒后重试！"):
                                    pass
                                logging.info("从结果中提取关联键的值失败！等待3秒后重试！")
                                time.sleep(3)
                                continue
                            else:
                                break
                        else:
                            break
                    else:
                        break
                if isinstance(relevance, bool):
                    logging.info("从结果中提取关联键的值失败！重试三次失败")
                    raise Exception("获取前置接口关联数据失败")
    else:
        pass
    return relevance


# if __name__ == '__main__':
#     case_dict = {'test_info': {'id': 'test_famous_list_01', 'title': 'home', 'host': 'api.652615.com', 'address': '/liuyi/rest72/home/famous_list'}, 'premise': [{'address': '/liuyi/rest79/user/first_in', 'cookies': True, 'file': False, 'headers': None, 'http_type': 'http', 'info': 'famous_list', 'parameter': None, 'parameter_type': 'application/x-www-form-urlencoded', 'relevance': ['data'], 'request_type': 'GET', 'test_name': 'famous_list', 'timeout': 20}], 'test_case': [{'test_name': 'famous_list', 'info': 'famous_list', 'http_type': 'http', 'request_type': 'GET', 'parameter_type': 'application/x-www-form-urlencoded', 'address': '/liuyi/rest72/home/famous_list', 'headers': {'X-Liuyi-App-Key': '56a4e68905234a46f413f7011376d2e0', 'Authorization\\tBearer': 'a60a04efa3cc08b77a6a63e36148d481', 'X-Liuyi-Device-ID': '1B71FD42-A458-4E9A-9A0D-94AE0827AE7A'}, 'cookies': True, 'timeout': 20, 'parameter': {'pageNo': '1', 'pageSize': '5'}, 'file': False, 'check': {'check_type': 'json', 'expected_code': 200, 'expected_request': 'result_famous_list.json'}, 'relevance': 'aaa'}]}
#     path = r'F:/pythoncode/learn_pytest_20200720/page/home'
#     print(ini_request(case_dict, path))
