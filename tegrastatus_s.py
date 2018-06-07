import signal
import subprocess
import time


# 捕获Ctrl C退出
def exit_pro(signum, frame):
    exit()


signal.signal(signal.SIGINT, exit_pro)
signal.signal(signal.SIGTERM, exit_pro)


def work(cmds):
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    while 1:
        # 继续处理
        current_stat = p.stdout.readline().decode().strip()
        print("%s:\n%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), current_stat))


if __name__ == '__main__':
    cmds = ['/home/nvidia/tegrastats']
    work(cmds)
