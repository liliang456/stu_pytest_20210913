

def set_state(value,path,testname):
    file_name = path+ '/' +testname+ '.yml'
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