# -*- coding:utf-8 -*-
import glob
import json
import pandas
import pandas.io.json

project_list = []

# globでresultフォルダにあるファイルを走査して読み込む
for filename in glob.glob("result/*.json"):
    project = json.loads(open(filename).read())
    project_list.append(project)

# json_normalizeを使ってDataFrameに変換する
df = pandas.io.json.json_normalize(project_list)

# 末尾が"_at"で終わるunixtimeのカラムをdatetimeに変換する
datetime_columns = filter(lambda a: a[-3:] == "_at", df.columns)
for column in datetime_columns:
    df[column] = pandas.to_datetime(df[column], unit='s')
    
# DataFrameからcsv形式のstrに変換する
csv_data = df.to_csv()

# macOSのExcelに読み込ませるので、CP932(Shift-JIS)にする
csv_data = csv_data.encode("cp932", "ignore")

# 結果を書き込む
with open("kickstarter_result.csv", "wb") as fp:
    fp.write(csv_data)
