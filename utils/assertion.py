def assertHttpCode(res, code_list=None):
    res_code = res.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError("Status code not in List!")