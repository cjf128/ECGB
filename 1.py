# 定义输入文件路径
file_ecg = r'D:\PythonProjects\ECGB\Data\ecg_m_0_2025-06-11_11-43-15.txt'
file_resp = r'D:\PythonProjects\ECGB\Data\resp_m_0_2025-06-11_11-43-15.txt'
file_spo2 = r'D:\PythonProjects\ECGB\Data\spo2_m_0_2025-06-11_11-43-15.txt'

# 输出文件路径
output_file = 'merged_data.txt'

# 打开三个输入文件和一个输出文件
with open(file_ecg, 'r', encoding='utf-8') as f_ecg, \
     open(file_resp, 'r', encoding='utf-8') as f_resp, \
     open(file_spo2, 'r', encoding='utf-8') as f_spo2, \
     open(output_file, 'w', encoding='utf-8') as out:

    # 按行读取并处理
    for line_ecg, line_resp, line_spo2 in zip(f_ecg, f_resp, f_spo2):
        # 去除两边空格和中括号，分割成数字列表
        ecg = [int(x.strip()) for x in line_ecg.strip()[1:-1].split(',')]
        resp = [int(x.strip()) for x in line_resp.strip()[1:-1].split(',')]
        spo2 = [int(x.strip()) for x in line_spo2.strip()[1:-1].split(',')]

        # 写入输出文件
        out.write(f"{ecg}\n{resp}\n{spo2}\n")