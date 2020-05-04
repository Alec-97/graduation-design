import datetime
import pandas as pd


def get_color(inputpath):  #定义get_color函数
    print('Excel File Path: {}'.format(inputpath))  #打印显示表格的路径
    start = datetime.datetime.now()  #赋值当前系统的时间
    # return a dict {sheet_name:dataframe}
    excel_file = pd.read_excel(inputpath, sheet_name=None) #从指定的路径中读取表格到excel_file
    end = datetime.datetime.now() #赋值系统的当前时间
    print('Read Excel Time: {}'.format(end - start)) #打印读取文件所用的时间
    sheet_num = len(excel_file) #读出表格的长度
    sheet_names = list(excel_file.keys())  # dict_keys->list

    sheets = [0]*sheet_num
    sheets_1dim = [0]*sheet_num
    i = 0
    for sheet_name in sheet_names:
        sheets[i] = excel_file[sheet_name].values  # DataFrame->numpy.ndarray
        sheets_1dim[i] = sheets[i].flatten()
        i += 1

    return sheets, sheets_1dim
