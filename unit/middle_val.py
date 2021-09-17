from setupMain import project_path
from config.confManage import dir_manage
from unit.initializeCase import ini_case
from unit.initializePremise import ini_request


# PATH = project_path + dir_manage('${page_dir}$') + "home"
PATH = project_path + dir_manage('${page_dir}$')

case_dict = ini_case(PATH, "api")


def famous():
    init_relevance = ini_request(case_dict, PATH)
    return init_relevance

