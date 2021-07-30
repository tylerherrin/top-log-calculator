# Top Log Calculator
A simple script that will calculate the average CPU usage and maximum CPU usage when provided with a top log.

```shell
python3 calculate.py top_log.txt
```

### Top Log Command

The regex used to parse top logs is designed around the top output logged by the following command. Don't expect it to work with other top outputs.

```shell
while ( sleep 60 ) ; do (printf "\n\n\n" && date +"[%d-%m-%y %T]" \
&& / top -bn 1 -o %CPU | head -n 15 && printf "\n\n\n") >> top_log.txt ; done
```

### Sample Top Log Output
```text
[30-07-21 16:31:49]
top - 16:31:49 up 2 days, 23:24,  2 users,  load average: 0.05, 0.
Tasks: 190 total,   1 running, 119 sleeping,   0 stopped,   0 zomb
%Cpu(s):  0.2 us,  0.1 sy,  0.1 ni, 99.6 id,  0.0 wa,  0.0 hi,  0.
KiB Mem : 15922328 total,  1136944 free,  2726880 used, 12058504 b
KiB Swap:        0 total,        0 free,        0 used. 12580060 a

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM
 3019 freeswi+  -2  19 3383308 155416  16908 S  33.3  1.0
 3072 bigblue+  20   0 5638152 355404  21464 S   6.7  2.2
 3122 bigblue+  20   0 5967088 322028  21344 S   6.7  2.0
28625 kurento   20   0 5017492  44860  28540 S   6.7  0.3
28668 bigblue+  20   0  769532  64372  30944 S   6.7  0.4
    1 root      20   0  225540   9504   6824 S   0.0  0.1
    2 root      20   0       0      0      0 S   0.0  0.0
    3 root       0 -20       0      0      0 I   0.0  0.0
```

