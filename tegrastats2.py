# coding: utf8
import argparse
import signal
import subprocess
import time

LOG_FILE = None


# 捕获Ctrl C退出
def exit_pro(signum, frame):
    if LOG_FILE:
        LOG_FILE.close()
    exit()


signal.signal(signal.SIGINT, exit_pro)
signal.signal(signal.SIGTERM, exit_pro)
# where the tegrastats binary file is
BIN_PATH = 'tegrastats'
LOG_FILE_PATH = './freq.log'


def work(write_to_log=False, your_args=''):
    """将tegrastats加上时间戳
    @:arg write_to_log 是否写入log文件"""
    global LOG_FILE
    cmds = [BIN_PATH]
    cmds += your_args.split()
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    if write_to_log:
        LOG_FILE = open(LOG_FILE_PATH, 'a')
    while 1:
        current_stat = p.stdout.readline().decode().strip()
        if current_stat == '':
            print("tegrastats error")
            break
        text = "%s:\n%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), current_stat)
        print(text)
        if write_to_log:
            LOG_FILE.write(text + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='调用tegrastats，并记录输出到log文件里')
    parser.add_argument('-b', '--bin', metavar='where tegrastats is', required=False, dest='bin_path', action='store')
    # the script will not write to log file unless you define the output log file path
    parser.add_argument('-o', '--output', metavar='write the log file to here', required=False, dest='log_file_path',
                        action='store')
    parser.add_argument('-p', '--params', metavar='additional arguments of tegrastats', required=False, dest='your_args',
                        action='store')
    args = parser.parse_args()
    if args.log_file_path:
        LOG_FILE_PATH = args.log_file_path
        write_to_log = True
    else:
        write_to_log = False
    if args.bin_path:
        BIN_PATH = args.bin_path
    work(write_to_log, args.your_args)
