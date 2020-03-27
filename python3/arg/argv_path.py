#!/usr/bin/env python3

# コマンドライン引数に存在するファイルへの
# パスが与えられたことを確認する

def exists():
    from sys import argv
    from pathlib import Path

    return(len(argv) > 1 and Path.exists(Path(argv[1])))

if __name__ == '__main__':

    print(exists())
