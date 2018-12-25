
import re

count = 0
target = ""
border = 10

# data.txtを読み込み
with open("data.txt","r") as text_data :
    # データがあるだけループ
    while True :
        count = count + 1
        line = text_data.readline()

        # 改行を除いてシングルクォート括りカンマ区切り
        if not line == "":
            target = target + "'" + re.sub('[\r\n]+$', '', line) + "',"

        # 閾値毎に行末のカンマを除いて出力
        if (count % border == 0) or (not line):
            target = target[:-1]
            print(target)
            target = ""
            if not line :
                break
