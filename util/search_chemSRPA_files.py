# -*- coding: utf-8 -*-
# Created by Yoshiaki Teshima at 2022/08/11
import logging
import pathlib

from Constant import *
import enum
import shutil

from typing import List

import tkinter
from tkinter import filedialog

# ロガー設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@enum.unique
class SUFFIX(enum.Enum):
    SHAI = ".shai"
    SHCI = ".shci"
    ZIP = ".zip"


d1 = []  # [(元ファイルのパス,ファイル名(拡張子なし)),(元ファイルのパス,ファイル名(拡張子なし)),...]


def create_dict_path_and_name(d: dict, path: str):
    p = pathlib.Path(path)
    d.append((p, p.stem))


def copy_chemSHRPA_datas(search_folder: str = None, suffix: SUFFIX = SUFFIX.SHAI):
    """
    検索するターゲットフォルダを選択、
    再帰検索でsuffixの拡張子データをzipに変更しtempファイルにコピーする
    :param search_folder:
    :param suffix:
    :return:
    """
    l = get_filelist(folder=search_folder, suffix=suffix)
    for f in l:
        create_dict_path_and_name(d1, f)
        change_suffix(f, SUFFIX.SHAI, SUFFIX.ZIP)


def folder_dialog(iDir=None) -> pathlib.Path:
    """
    ファイルダイアログを開く
    :param iDir:
    :return:
    """
    # ルートウィンドウ
    root = tkinter.Tk()
    root.withdraw()  # ルートウィンドウの非表示

    if (iDir is None) or (not pathlib.Path(iDir).exists()):
        iDir = TEST_DIR  # テストフォルダ

    # askdirectory ディレクトリを選択する。
    dirname = filedialog.askdirectory(initialdir=iDir, title="ディレクトリを選択")
    return pathlib.Path(dirname)


def file_dialog(iDir=None) -> pathlib.Path:
    # asksaveasfilename
    myFormats = [
        ('CSVファイル', '*.csv'),
    ]
    root = tkinter.Tk()
    root.withdraw()

    if (iDir is None) or (not pathlib.Path(iDir).exists()):
        iDir = TEST_DIR  # テストフォルダ

    fileName = filedialog.asksaveasfilename(
        parent=root,
        filetypes=myFormats,
        title="名前をつけて保存",
        initialdir=iDir,
        initialfile="output.csv",
        defaultextension="csv",
    )
    return pathlib.Path(fileName)


def change_suffix(file_name=None, from_suffix: SUFFIX = SUFFIX.SHAI, to_suffix: SUFFIX = SUFFIX.ZIP):
    """
    tempフォルダにshai,shciファイルをzip拡張子に変更してコピーする
    :param file_name:
    :param from_suffix:
    :param to_suffix:
    :return:
    """
    if file_name is None:  # テストコード用
        file_name = TEST_DIR / "SHAI_All_parts_for_Toch_light_2.05.00_V2_20220406000000.shai"
        print(file_name)

    if to_suffix is not SUFFIX.ZIP:
        print("to_suffixにミスがあります")
        return

    if (from_suffix is SUFFIX.SHAI) or (from_suffix is SUFFIX.SHCI):
        # ファイルの拡張子
        file_suffix = pathlib.PurePath(file_name).suffix

        # 変更対象かどうか判定する
        if file_suffix in from_suffix.value:
            # 変更後のファイル名+拡張子
            name = pathlib.Path(file_name).stem + to_suffix.value

            # tmpフォルダのパス+変更後のファイル名+拡張子
            to_name = pathlib.Path(TEMP_DIR) / pathlib.Path(name)

            # ファイル名を変更する
            shutil.copy(file_name, to_name)

    else:
        print(from_suffix)
        print("from_suffixにミスがあります")
        return


def get_filelist(folder: str = None, suffix: SUFFIX = SUFFIX.SHAI) -> List:
    """
    指定したフォルダ以下にあるshaiファイル または shciファイルのパス一覧を取得する
    :param folder: 検索対象のフォルダ
    :param suffix: shai or shci ファイル SUFFIX.SHAI , SUFFIX.SHCI クラスで指定
    :return: パスのlist
    """
    if folder is None:  # テストコード用
        folder = pathlib.Path(TEST_DIR)

    p_temp = pathlib.Path(folder)

    file_liset = list(p_temp.glob(f'**/*{suffix.value}'))

    # ファイルを探したが見つからなかったとき->指定フォルダを間違っていないか
    if len(file_liset) == 0:
        logger.info({'action'  : 'get_filelist',
                     'status'  : 'caution',
                     'messaage': 'no file found'}
                    )

    return file_liset
