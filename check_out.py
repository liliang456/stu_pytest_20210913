from unit import checkResult, apiSend

def check_out_api(code,data,case, project_dict,relevance,_path):
    if isinstance(case["check"], list):
        for i in case["check"]:
            checkResult.check_result(case["test_name"], i, code, data, _path, relevance)
    else:
        checkResult.check_result(case["test_name"], case["check"], code, data, _path, relevance)