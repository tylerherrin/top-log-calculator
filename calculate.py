import sys
import re

# Given the output below, grab non-zero  %CPU values then calculate average and max values.
#
# [30-07-21 16:36:50]
# top - 16:36:50 up 2 days, 23:29,  2 users,  load average: 0.40, 0.
# Tasks: 188 total,   1 running, 119 sleeping,   0 stopped,   0 zomb
# %Cpu(s):  0.3 us,  0.1 sy,  0.1 ni, 99.6 id,  0.0 wa,  0.0 hi,  0.
# KiB Mem : 15922328 total,  1041508 free,  2796408 used, 12084412 b
# KiB Swap:        0 total,        0 free,        0 used. 12510164 a
#
#   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM
#  3019 freeswi+  -2  19 3383308 155416  16908 S  13.3  1.0
# 28625 kurento   20   0 6841200  84516  28824 S  13.3  0.5
#  3122 bigblue+  20   0 5967088 322028  21344 S   6.7  2.0
#     1 root      20   0  225540   9504   6824 S   0.0  0.1
#     2 root      20   0       0      0      0 S   0.0  0.0
#     3 root       0 -20       0      0      0 I   0.0  0.0
#     4 root       0 -20       0      0      0 I   0.0  0.0
#     6 root       0 -20       0      0      0 I   0.0  0.0
#
# Top Log is generated with:
# while ( sleep 60 ) ; do (printf "\n\n\n" && date +"[%d-%m-%y %T]" && /
# top -bn 1 -o %CPU | head -n 15 && printf "\n\n\n") >> top_log.txt ; done

try:
    file_path = sys.argv[1]
except IndexError:
    print("No filepath provided! Exiting!")
    exit(1)

# Regex used to match relevant %CPU values.
line_regex = re.compile(r"\d+\s+\w+\+*\s+-*\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\w\s+(?!0\.0)(\d+\.?\d*)")

try:
    with open(sys.argv[1], "r") as top_log_file:
        top_log_string = top_log_file.read()
except FileNotFoundError:
    print(file_path + " does not exist! Exiting!")
    exit(1)

cpu_values = line_regex.findall(top_log_string)
for index, value in enumerate(cpu_values):
    cpu_values[index] = float(value)

avg_cpu = format(sum(cpu_values) / len(cpu_values), ".2f")
max_cpu = format(max(cpu_values), ".2f")
print("Average CPU Usage: " + avg_cpu + "%")
print("Maximum CPU Usage: " + max_cpu + "%")
