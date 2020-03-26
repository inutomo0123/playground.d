#!/bin/bash

set -Cue

LOG_FILE='/var/log/ufw.log'

if [ -p /dev/stdin ]; then
    # パイプで標準入力が与えられたとき
    cat -
else
    if [ -f $1 ]; then
        # オプションのファイルが存在するとき
        cat $1
    else
        cat ${LOG_FILE}
    fi
fi | grep -o 'SRC=\S*' | cut -b5- | sort | uniq -c | sort -nr | \
    awk 'BEGIN { OFS="," } { print $2, $1 }'
