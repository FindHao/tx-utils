# 读写2003 excel
import argparse
import xlwt
import re


class Status:
    def __init__(self):
        # CPU部分
        # 每个cpu核心的频率变化
        self.cpu_freq = [[], [], [], [], [], []]
        # 占用率变化
        self.cpu_utilization = [[], [], [], [], [], []]
        # GPU部分
        self.ram = []
        self.emc = []
        self.gpu = []


def filter_content_from_raw_log(start_time, end_time, file_path):
    """将频率数据从原始log中提取出来"""
    with open(file_path, 'r') as fin:
        content = fin.read()
    print(start_time)
    print(end_time)
    if not start_time:
        start_time = ''
    if not end_time:
        end_time = ''
    reg = re.compile(r'%s[\s\S]+%s' % (start_time, end_time))
    reg2 = re.compile(
        r'RAM (\d+).+?cpu \[(\d+)%@(\d+),(\d+)%@(\d+),(\d+)%@(\d+),(\d+)%@(\d+),(\d+)%@(\d+),(\d+)%@(\d+)\] EMC (\d+)%@.+?GR3D (\d+)%')
    result = reg.findall(content)
    status = Status()
    if result:
        result2 = reg2.findall(result[0])
        if result2:
            for line in result2:
                status.ram.append(int(line[0]))
                for i in range(6):
                    status.cpu_utilization[i].append(int(line[i * 2 + 1]))
                    status.cpu_freq[i].append(int(line[i * 2 + 2]))
                status.emc.append(int(line[13]))
                status.gpu.append(int(line[14]))
        else:
            print("没有符合条件的输出-2")
    else:
        print("没有符合条件的输出-1")
    return status


def write_status_to_xls(status, xls_file='./log.xls'):
    """将获取的内容写到excel文件里"""
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("cpu")
    cpu_status = ['cpu0', 'cpu1', 'cpu2', 'cpu3', 'cpu4', 'cpu5']

    # cpu频率
    sheet.write(0, 0, 'cpu frequency')
    for i in range(6):
        sheet.write(1, i, cpu_status[i])
    for i in range(0, len(status.cpu_freq[0])):
        for j in range(0, 6):
            sheet.write(i + 2, j, status.cpu_freq[j][i])
    # cpu占用率
    base_offset_cpu_utilization = 7
    sheet.write(0, base_offset_cpu_utilization, 'cpu utilization')
    for i in range(6):
        sheet.write(1, i + base_offset_cpu_utilization, cpu_status[i])
    for i in range(0, len(status.cpu_utilization[0])):
        for j in range(0, 6):
            sheet.write(i + 2, j + base_offset_cpu_utilization, status.cpu_utilization[j][i])
    # ram
    base_offset_ram = 14
    sheet.write(0, base_offset_ram, 'ram')
    for i in range(0, len(status.ram)):
        sheet.write(i + 2, base_offset_ram, status.ram[i])
    # emc
    base_offset_emc = 15
    sheet.write(0, base_offset_emc, 'emc')
    for i in range(0, len(status.emc)):
        sheet.write(i + 2, base_offset_emc, status.emc[i])
    # gpu
    base_offset_gpu = 16
    sheet.write(0, base_offset_gpu, 'gpu')
    for i in range(0, len(status.gpu)):
        sheet.write(i + 2, base_offset_gpu, status.gpu[i])

    wb.save(xls_file)
    print("Done!")


if __name__ == '__main__':
    # 输入参数
    parser = argparse.ArgumentParser(description='用来提取一段时间内tegra cpu gpu利用率等信息的工具')
    parser.add_argument('-s', '--start', metavar='开始的时间戳', required=False, dest='start_time', action='store')
    parser.add_argument('-e', '--end', metavar='结束的时间', required=False, dest='end_time', action='store')
    parser.add_argument('-i', '--input', metavar='输入的log文件', required=True, dest='log_file_path', action='store')
    parser.add_argument('-o', '--output', metavar='输出的excel文件路径', required=False, dest='xls_file_path', action='store')
    args = parser.parse_args()
    log_file = args.log_file_path
    start_time = args.start_time
    end_time = args.end_time
    # 默认生成的xls表格是当前目录下的log.xls
    xls_file = args.xls_file_path
    status = filter_content_from_raw_log(start_time, end_time, log_file)
    write_status_to_xls(status, xls_file)
