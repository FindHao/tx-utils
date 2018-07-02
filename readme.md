# tx-utils
This is a utils pack for nvidia tegra x series.

## install 

You can just download released zip file and unzip it.

## usage

### tegrastats2

It's a enhanced pack of Nvidia tegrastats tool. The origin tegrastats locates in `~/tegrastats` and it's a executable binary file which shows the current status of tx's cpus and gpu. However it not open sourced and you can not change anything about what it outputs. And I warp it in this script and add time mark. 
 
 ```bash
 sudo python3 tegrastats2.py --bin=/home/nvidia/tegrastats --output=./a.log --params "--interval 500"
 ```
It should be under sudo privilege if you want to get the gpu status.
`--bin` is the path of original tegrastats location and `--output` defines the file path you want to write to.

`--params` adds the optional arguments to `tegrastats` which has support more functions from jetpack 3.2. `--interval 500` means the interval of every probe. 

Tegrastats has more options from jetpack 3.2. And I add the tegrastats_jp3.1 and tegrastats_jp_3.2 to this project. You can just download and run tegrastats_jp_3.2 on tx of jetpack 3.1.

### visualize

It's a visualization tool of tx status.

It will read the tegrastats2's output and resort the data into a xls file.

```bash
python3 visualize.py --start="2018-06-09 02:42:30" --end="2018-06-09 02:43:15" --input="/home/find/ddown/a.log" --output=./freq.xls
```

If you don't define the `--start` and `--end`, you will get the whole logs' data.

# tx-utils

这一个nvidia jetson tegra x系列的工具包。主要用来记录tx板子的状态，并将其写入excel表格，便于生成图表。

## 安装

直接从release下载zip压缩包解压即可。

## 使用

### tegrastats2

Nvidia自带了一个tegrastats工具，默认位于home目录下。可以用来查看cpu和gpu的一些状态信息，我写了这个脚本，在其输出结果中加入了时间。

 ```bash
 sudo python3 tegrastats2.py --bin=/home/nvidia/tegrastats --output=./a.log --params "--interval 500"
 ```

你应该用sudo来执行这个脚本，因为sudo权限才能让tegrastats获得到gpu的状态。
`--bin`是tegrastats的路径，`--output`是log日志输出的路径。

`--params`是附加给`tegrastats`的参数，自从jetpack3.2以后，nvidia提供的tegrastats工具越来越强大，给了更多了运行参数。同时我也将新旧版本的tegrastats加到了这个项目中。

### visualize

将原始日志内容格式化到excel文件里，并自动生成cpu占用率和gpu占用率的折线图。

![](http://www.findhao.net/wp-content/uploads/2018/06/tx2-utils.excel_.jpg)


```bash
python3 visualize.py --start="2018-06-09 02:42:30" --end="2018-06-09 02:43:15" --input="/home/find/ddown/a.log" --output=./freq.xls
```
![](http://www.findhao.net/wp-content/uploads/2018/06/tx2-utils.linechar.jpg)

如果你不指定`--start` 和 `--end`，那么将针对整个日志文件进行格式化。

