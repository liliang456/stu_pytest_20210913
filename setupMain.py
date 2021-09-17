import os
import pytest
from config.confManage import dir_manage
from script.logs import LogConfig
project_path = os.path.split(os.path.realpath(__file__))[0]


if ':' in project_path:
    project_path = project_path.replace('\\', '/')
else:
    pass

if __name__ == '__main__':
    LogConfig(project_path)
    # from script.writeCase import write_case
    # # depend 为false后 就没有依赖选项了
    # write_case(project_path + dir_manage('${data_dir}$'),depend=False,rele='data',rele_depend='ticket')
    # args = ['-s', '-q', '--alluredir', project_path + dir_manage('${report_xml_dir}$')]
    # pytest.main(args)
    pytest.main(['-s'])
    # cmd = 'allure generate %s -o %s -c' % (project_path + dir_manage('${report_xml_dir}$'),
    #                                        project_path + dir_manage('${report_html_dir}$'))
    # os.system(cmd)