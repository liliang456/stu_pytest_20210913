import yaml


def ini_case(_path, case_file):
    """
    case初始化.yml测试用例
    :param _path: case路径
    :param case_file: case名称
    :return:
    """
    try:
        with open(_path + '/' + case_file + '.yml', 'r', encoding="utf-8") as f:
            project_dict = yaml.load(f,Loader=yaml.FullLoader)
    except FileNotFoundError:
        with open(_path + '/' + case_file + '.yaml', 'r', encoding="utf-8") as f:
            project_dict = yaml.load(f,Loader=yaml.FullLoader)
    return project_dict


# if __name__ == '__main__':
#     path = r'F:/pythoncode/learn_pytest_20200720/page/home'
#     case_file = 'famous_list'
#     print(ini_case(path, case_file))