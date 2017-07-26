import os
from xlrd import open_workbook
from common.Log import MyLog as Log
import readConfig
import request
import json
import unittest

log = Log.get_log()
logger = log.get_logger()
proDir=readConfig.proDir


def get_xls(xls_name,sheet_name):
    cls=[]
    xlsPath=os.path.join(proDir,"testFile","case",xls_name)
    file=open_workbook(xlsPath)

    sheet=file.sheet_by_name(sheet_name)

    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0]!=u"case_name":
            cls.append(sheet.row_values(i))

    return cls


def show_return_msg(response):
    url=response.url
    msg=response.text
    print("\n请求地址："+url)
    # 可以显示中文
    print("\n请求返回值："+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))


def get_value_from_return_json(json, name1, name2):
    """
    get value by key
    :param json:
    :param name1:
    :param name2:
    :return:
    """
    info = json['info']
    group = info[name1]
    value = group[name2]
    return value