import logging
import allure

from unit import apiMethod, replaceRelevance
# from unit import initializeCookie
from config import confManage
from unit import readParameter



def send_request(data, host, address, _path, relevance=None):
    """
    封装请求
    :param data: 测试用例
    :param host: 测试host
    :param address: 接口地址
    :param relevance: 关联对象
    :param _path: case路径
    :return:
    """
    logging.info("="*80)
    header = readParameter.read_param(data["test_name"], data["headers"], _path, relevance)
    logging.debug("请求头处理结果：%s" % header)
    parameter = readParameter.read_param(data["test_name"], data["parameter"], _path, relevance)
    logging.debug("请求参数处理结果：%s" % parameter)
    try:
        host = data["host"]
    except KeyError:
        pass
    try:
        address = data["address"]
    except KeyError:
        pass
    host = confManage.host_manage(host)
    address = replaceRelevance.replace(address, relevance)
    logging.debug("host处理结果： %s" % host)
    if not host:
        raise Exception("接口请求地址为空 %s" % data["headers"])
    logging.info("请求接口：%s" % str(data["test_name"]))
    # logging.info("请求地址：%s" % data["http_type"] + "://" + host + address)
    logging.info("请求头: %s" % str(header))
    logging.info("请求参数: %s" % str(parameter))
    # if data["test_name"] == 'password正确':
    # if data["test_name"] == 'meirijingxuan':
    #     with allure.step("保存cookie信息"):
    #         allure.attach(name="请求接口", body=str(data["test_name"]))
    #         allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
    #         allure.attach(name="请求头", body=str(header))
    #         allure.attach(name="请求参数", body=str(parameter))
    #         apiMethod.save_cookie(header=header, address=data["http_type"] + "://" + host + address, data=parameter)

    if data["request_type"].lower() == 'post':
        logging.info("请求方法: POST")
        if data["file"]:
            with allure.step("POST上传文件"):
                allure.attach(name="请求接口", body=str(data["test_name"]))
                allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
                allure.attach(name="请求头", body=str(header))
                allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.post(header=header,
                                    address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"],
                                    files=parameter,
                                    timeout=data["timeout"])
        else:
            with allure.step("POST请求接口"):
                allure.attach(name="请求接口", body=str(data["test_name"]))
                allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
                allure.attach(name="请求头", body=str(header))
                allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.post(header=header,
                                    address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"],
                                    data=parameter,
                                    timeout=data["timeout"])
    elif data["request_type"].lower() == 'get':
        with allure.step("GET请求接口"):
            allure.attach(name="请求接口", body=str(data["test_name"]))
            allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
            allure.attach(name="请求头", body=str(header))
            allure.attach(name="请求参数", body=str(parameter))
            logging.info("请求方法: GET")
        result = apiMethod.get(header=header,
                               address=data["http_type"] + "://" + host + address,
                               data=parameter,
                               timeout=data["timeout"])
    else:
        result = {"code": False, "data": False}
    logging.info("请求接口结果：\n %s" % str(result))
    # print(result)
    return result

if __name__ == '__main__':
    data ={'address': '/liuyi/rest79/user/first_in', 'cookies': True, 'file': False, 'headers': None, 'http_type': 'http', 'info': 'famous_list', 'parameter': None, 'parameter_type': 'application/x-www-form-urlencoded', 'relevance': ['data'], 'request_type': 'GET', 'test_name': 'famous_list', 'timeout': 20}
    host = 'api.652615.com'
    address = '/liuyi/rest79/user/first_in'
    path = r'F:/pythoncode/learn_pytest_20200720/page/home'
    relevance = 'data'
    print(send_request(data, host, address, path, relevance))