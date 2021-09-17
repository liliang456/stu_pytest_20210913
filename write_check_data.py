import os

def checkeout_yaml(data,case):
    curpath = os.path.realpath(__file__)  # 获取当前文件绝对路径
    dirpath = os.path.dirname(curpath)  # 获取当前文件的文件夹路径
    casespath = os.path.join(dirpath, "page","user",case["test_name"]+'.json')
    with open(casespath,'w',encoding='utf-8') as fp:
        fp.write(data)
