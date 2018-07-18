import yaml
import os
from xlrd import open_workbook


class YamlReader(object):
    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yamlf = yaml_file
        else:
            raise FileNotFoundError("YAML FILE IS NOT EXISTS")
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlf) as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader(object):
    """
       读取excel文件中的内容。返回list。

       如：
       excel中内容为：
       | A  | B  | C  |
       | A1 | B1 | C1 |
       | A2 | B2 | C2 |

       如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
       [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

       如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
       [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

       可以指定sheet，通过index或者name：
       ExcelReader(excel, sheet=2)
       ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError("Excel File IS NOT EXISTS")
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    '''Test read yaml file'''
    # BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    # config_path = os.path.join(BASE_PATH, 'config', 'config.yml')
    # test = YamlReader(config_path)
    # print(test.data)

    excel = r'C:\Users\liuda\Desktop\Langbo_WEBUI_TEST\data\baidu.xlsx'
    reader = ExcelReader(excel, title_line=True)
    print(reader.data)
    # reader2 = ExcelReader(excel, title_line=False)
    # print(reader2.data)
    for data in reader.data:
        print(data.pop('condition'))
        print(data.items())