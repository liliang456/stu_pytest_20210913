import allure
import pytest
from setupMain import project_path
from config.confManage import dir_manage
from unit.initializeCase import ini_case
from unit.initializePremise import ini_request
from unit.apiSendCheck import api_send_check
from unit.write_yaml import set_state
from unit.load_yaml import load_yaml

# yaml的路径
PATH = project_path + dir_manage('${page_dir}$') + "user"

# 拼接上yaml文件的名称，获取yaml的文件内容
case_dict = ini_case(PATH, "check_movie")

# 获取premise的关联值，可以进行替换
def get_pre_value():
    init_relevance = ini_request(case_dict, PATH)
    return init_relevance

# 报告会显示feature
@allure.feature(case_dict["test_info"]["title"])
class TestCheckApi:
    # 参数
    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
    # 报告显示
    @allure.story("check_movie")
    # 重复执行
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_check_01(self, case_data):
        """

        :param case_data: 测试用例
        :return:
        """
        # 根据yaml文件中test_case下的depend的true跟false判断是否需要依赖值
        if case_dict['test_case'][0]['depend'] == True:
            param = case_dict['test_case'][0]['parameter']
            par = dict(param, **get_pre_value())
            testname = case_dict['test_case'][0]['test_name']
            if case_dict['test_case'][0]['rele_depend'] != False:
                par[case_dict['test_case'][0]['rele_depend']] = par.pop(case_dict['premise'][0]['relevance'])
                # 如需转换参数，可用premise中的relevance与testcase内的rele_depend替换
            set_state(par,PATH,testname)
            yamlvalue = load_yaml(case_dict['test_case'][0]['test_name'],PATH)
            if yamlvalue['test_case'][0]['rele_depend'] != None:
                yamlvalue['premise'][0]['relevance'] = yamlvalue['test_case'][0]['rele_depend']
            api_send_check(yamlvalue['test_case'][0],yamlvalue,relevance=yamlvalue['premise'][0]['relevance'],_path=PATH)
        else:
            self.init_relevance = ini_request(case_dict, PATH)
            # 发送测试请求
            api_send_check(case_data, case_dict, self.init_relevance, PATH)


if __name__ == '__main__':
    pytest.main(['-s'])