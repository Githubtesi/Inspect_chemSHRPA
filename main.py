#! env python
# -*- coding: utf-8 -*-
import logging
import os
import sys

# Inspect_chemSHRPA.main
# Date: 2022/08/13
# Filename: main 

__author__ = 'Yoshiaki Teshima'
__date__ = "2022/08/13"

from gui import chem

logging.basicConfig(level=logging.INFO)


def main():
    # 作業ディレクトリを自身のファイルのディレクトリに変更
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    chem.start_up()
    return


if __name__ == '__main__':
    main()
