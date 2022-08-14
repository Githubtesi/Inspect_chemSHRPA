# -*- coding: utf-8 -*-
# Created by Yoshiaki Teshima at 2022/08/11
import collections
import glob
import zipfile
from copy import copy
from bs4 import BeautifulSoup
from util.search_chemSRPA_files import *
import csv

d2 = []  # [(zip前のファイル,zip後の構成ファイル),(zip前のファイル,zip後の構成ファイル),...]


class ChemData(object):
    """  shci,shaiデータから必要なデータを出力下クラス  """

    def __init__(self, product_name: str, company_name: str, path: List = None):
        self.product_name = product_name
        self.company_name = company_name
        if path is None:
            self.path = []
        self.path = copy(path)

    def __str__(self):
        return f"ProductID: {self.product_name} SupplyCompany: {self.company_name} path: {self.path}"

    @classmethod
    def to_csv(cls, xmldatas: List, output: str = None):
        # 出力先の指定がない場合
        if output is None:
            output = pathlib.Path(PROJECT_DIR) / pathlib.Path("output.csv")

        with open(output, mode="w", newline="", encoding="utf_8_sig") as csv_file:
            # タイトルのセット
            Titles = collections.namedtuple("Titles", ["product_name", "company_name", "path"])
            fieldnames = Titles(
                product_name="製品名", company_name="会社名", path="保存先")
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # タイトルヘッダー表示
            writer.writeheader()

            # 要素の書き込み
            datas = []
            for xmldata in xmldatas:
                abs_path = ""
                for path in xmldata.path:
                    abs_path += str(pathlib.Path(path).absolute()) + ","
                data = {
                    fieldnames.product_name: xmldata.product_name,
                    fieldnames.company_name: xmldata.company_name,
                    fieldnames.path        : abs_path,
                }
                datas.append(data)
            writer.writerows(datas)


def unzip_all():
    """ TEMP_DIRフォルダ内にあるzipファイルを展開 """

    def get_temp_all_files() -> List:
        """ TEMP_DIRフォルダのファイル取得 """
        l = []
        files = glob.glob(f"{TEMP_DIR}/*")
        for file in files:
            l.append(file)
        return l

    def unzip(folder: str):
        """ zipを展開+{zip前のファイル+zip後の構成ファイル}をd2に格納  """
        with zipfile.ZipFile(folder, "r") as z:
            # 圧縮されているファイルの一覧を取得
            zip_list = z.namelist()

            for f in zip_list:
                d2.append((pathlib.Path(folder).stem, pathlib.Path(f).stem))

            # ファイルの展開
            z.extractall(UNZIP_TEMP_DIR)

    files = get_temp_all_files()
    for file in files:
        unzip(file)


def create_ChemDatas() -> List[ChemData]:
    def get_unzip_temp_all_files() -> List:
        """ Unzipしたファイルのパス一覧 """
        l = []
        files = glob.glob(f"{UNZIP_TEMP_DIR}/*")
        for file in files:
            l.append(file)
        return l

    def attach_filename_to_path(xmlfile, d1, d2) -> list[str]:
        """
        d1 (元ファイルのパス,ファイル名(拡張子なし))+ d2 (zip前のファイル,zip後の構成ファイル)
        -> zip後の構成ファイル-元のファイルパス
        """
        l = []
        for k2, v2 in d2:
            if v2 == pathlib.Path(xmlfile).stem:
                for k1, v1 in d1:
                    if v1 == k2:
                        l.append(k1)
        return l

    chemDatas = []  # ChemDataを格納する配列

    # 全ファイルの展開
    unzip_all()

    # xmlデータ
    xmlfiles = get_unzip_temp_all_files()

    # ChemDataクラスのリスト
    for xmlfile in xmlfiles:
        with open(xmlfile, "r", encoding="utf-8") as f:
            sentence = f.read()
            soup = BeautifulSoup(sentence, "xml")
            product_name = soup.find(name="ProductID")['name']
            supply_company = soup.find(name="SupplyCompany")['nameLocal']
            path = attach_filename_to_path(xmlfile, d1, d2)

            chemDatas.append(
                ChemData(product_name, supply_company, path)
            )
    return chemDatas
