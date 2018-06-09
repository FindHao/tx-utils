# tx-utils
This is a utils pack for nvidia tegra x series.

## install 

You can just download released zip file and unzip it.

## usage

### tegrastats2

It's a enhanced pack of Nvidia tegrastats tool. The origin tegrastats locates in `~/tegrastats` and it's a executable binary file which shows the current status of tx's cpus and gpu. However it not open sourced and you can not change anything about what it outputs. And I warp it in this script and add time mark. 
 
 ```bash
 sudo python3 tegrastats2.py --bin=/home/nvidia/tegrastats --output=./a.log
 ```
It should be under sudo privilege if you want to get the gpu status.
`--bin` is the path of original tegrastats location and `--output` defines the file path you want to write to.

### visualize

It's a visualization tool of tx status.

It will read the tegrastats2's output and resort the data into a xls file.

```bash
python3 visualize.py --start="2018-06-09 02:42:30" --end="2018-06-09 02:43:15" --input="/home/find/ddown/a.log" --output=./freq.xls
```

If you don't define the `--start` and `--end`, you will get the whole logs' data.

