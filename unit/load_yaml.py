import yaml,os
from config.confManage import dir_manage

def load_yaml(case_file,yml_Path):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_path = BASE_DIR.replace('\\', '/')
    # PATH = project_path + dir_manage('${page_dir}$')
    file_name = yml_Path + '/'+ case_file + '.yml'
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()
        yamlvalue = yaml.load(file_content, Loader=yaml.FullLoader)
        return yamlvalue


def set_state(value,case_file):
    # file_name = r"F:\pythoncode\learn_pytest_20200720\page\home\famous_list.yml"

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_path = BASE_DIR.replace('\\', '/')
    PATH = project_path + dir_manage('${page_dir}$')
    file_name = PATH + '/' + case_file + '.yml'
    import yaml
    with open(file_name, 'r', encoding="utf-8") as f:
        doc = list(yaml.safe_load_all(f))
    doc[0]['test_case'][0]['parameter'] = value
    with open(file_name, 'w', encoding="utf-8") as f:
        yaml.safe_dump_all(doc, f, default_flow_style=False)
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()
        yamlvalue = yaml.load(file_content, Loader=yaml.FullLoader)
        return yamlvalue

# if __name__ == '__main__':
#     load_yaml('famous_list')