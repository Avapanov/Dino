# ������ ���������
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime

#��������� ������ ���������� ������ ��������
data=pd.read_csv('exit_table_script_1.csv', parse_dates=['timeframe_start'])

#������� ������� , ������������� 'api_name','mtd'
data['api_and_mtd']=data['api_name']+';'+data['http_method']
data.head()

#����������� ���������� � ������� ��� ��� 'api'and 'mtd'
std=data.groupby('api_and_mtd')['count_http_code_5xx'].std()
means=data.groupby('api_and_mtd')['count_http_code_5xx'].mean()

# ������� ������� ��������
def anomali(data):
    is_anomali=[]
    for i in range(len(data)):
        for j in range(len(std)):
            if data.api_and_mtd[i]==std.index[j]:
                if data.count_http_code_5xx[i]>(means.values[j]+3*std.values[j]):
                    is_anomali.append(True)
                else:
                    is_anomali.append(False)
    data['is_anomali']=is_anomali
    return data
	
# ��������� ����� ��������
table=anomali(data)

# ������ ������ 'api_and_mtd'
table= table.drop('api_and_mtd', axis=1)

# ������ ������� � csv
table.to_csv('exit_table_script_2.csv')