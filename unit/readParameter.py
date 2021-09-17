import json
from json import JSONDecodeError
from unit.replaceRelevance import replace


def read_param(test_name, param, _path, relevance=None):
    """
    读取用例中参数parameter
    :param test_name: 用例名称
    :param param: parameter
    :param relevance: 关联对象
    :param _path: case路径
    :param result: 全局结果
    :return:
    """
    if isinstance(param, dict):
        param = replace(param, relevance)
    elif isinstance(param, list):
        param = replace(param, relevance)
    elif param is None:
        pass
    else:
        try:
            with open(_path + "/" + param, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    if i["test_name"] == test_name:
                        param = i["parameter"]
                        break
                if not isinstance(param, dict):
                    raise Exception("未能找到用例关联的参数\n文件路径：%s\n索引：%s" % (param, _path))
                else:
                    param = replace(param, relevance)
        except FileNotFoundError:
            raise Exception("用例关联文件不存在\n文件路径： %s" % param)
        except JSONDecodeError:
            raise Exception("用例关联的参数文件有误\n文件路径： %s" % param)
    return param


# def set_state(value):
#     file_name = r"F:\pythoncode\API_service-master\crm\page\home\famous_list.yml"
#     import yaml
#     with open(file_name, 'r', encoding="utf-8") as f:
#         doc = list(yaml.safe_load_all(f))
#         # print(doc[0]['test_case'][0]['parameter'])
#         # print(list(doc))
#     # doc[docNumber][key] = value
#     doc[0]['test_case'][0]['parameter'] = value
#     with open(file_name, 'w', encoding="utf-8") as f:
#         yaml.safe_dump_all(doc, f, default_flow_style=False)
#     with open(file_name, 'r', encoding='utf-8') as f:
#         file_content = f.read()
#         yamlvalue = yaml.load(file_content, Loader=yaml.FullLoader)
#         return yamlvalue










