from unit import checkResult, apiSend
from unit.readResultRelevance import get_relevance
import time,json,os,logging
from write_check_data import checkeout_yaml
from check_out import check_out_api


def api_send_check(case, project_dict,relevance,_path):
    # print('case----',case)
    # print('prodict-----',project_dict)
    # print('rele-----',relevance)
    # print('path-----', _path)
    # relevance = {'doubanID'：'123331'}
    """
    接口请求并校验结果
    :param case: 单条用例
    :param project_dict: 用例文件对象
    :param relevance: 关键值实例对象
    :param rel: 关联值类对象
    :param _path: case目录
    :return:
    """
    # print('1------',data)
    # print('2------',code)
    # print('case------', case)
    # print('project_dict------', project_dict)
    # # print('5------', project_dict["test_info"].get("address"))
    # print('relevance-------', relevance)
    # print('_path-------', _path)
    # print('rel-------', rel)



    code, data_url = apiSend.send_request(case, project_dict["test_info"].get("host"),
                                       project_dict["test_info"].get("address"), _path, relevance)
    print(data_url)
    if code == 200:
        dic = {
            "test_name": case["test_name"],
            "json":data_url
        }
        lis = []
        lis.append(dic)
        data = json.dumps(lis,ensure_ascii=False,indent=1)
        checkeout_yaml(data,case)
        check_out_api(code,data_url,case, project_dict,relevance,_path)
    else:
        logging.info(code!=200,'code不等于200,无法进行返回值的检验！')