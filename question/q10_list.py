"""
配列って中々イメージできないですよね？
プログラミングでは配列をよく使います。
変数が一つの箱だとしたら、配列は箪笥のイメージです！

Pythonでは配列のことを
list形式
tupple形式
の2種類を差します。


name_list = ["名前1","名前2","名前3"] # 後から要素の追加削除可能
name_tupple = ("名前1","名前2","名前3") # 一度定義したら要素の追加削除不可

配列の追加、削除の関数

末尾に追加 配列.append()
指定に追加 配列.insert(要素番号, 値)

末尾を削除 配列.pop()
指定を削除 配列.pop(要素番号)


問題：配列を扱って以下を出力せよ

====出力===
鈴木さんの役職は部長
佐藤さんの役職は課長
山田さんの役職は係長
====再代入出力===
藤田さんの役職は部長
====要素追加===
['藤田', '藤田', '佐藤', '山田', '藤田']
['部長', '課長', '係長', '大統領']
====要素削除(末尾)===
['藤田', '藤田', '佐藤', '山田']
['課長', '係長', '大統領']


"""

name_list = ["鈴木", "佐藤", "山田"]
position = ["部長", "課長", "係長"]


print("====出力===")
print("配列name_listの鈴木を出力" + "さんの役職は" + "配列name_listの部長を出力")
print("配列name_listの佐藤を出力" + "さんの役職は" + "配列name_listの課長を出力")
print("配列name_listの山田を出力" + "さんの役職は" + "配列name_listの係長を出力")

# 再代入
print("====再代入出力===")
name_list[0] = "藤田"
print(name_list[0] + "さんの役職は" + position[0])


print("====要素追加===")

# ↓コメントアウトを外し"藤田"と"大統領"を末尾に追加しよう
# name_list.末尾に追加する関数と引数
# position.末尾に追加する関数と引数

# ↓要素番号 1に追加
# name_list.

print(name_list)
print(position)

print("====要素削除(末尾)===")
# ↓コメントアウトを外し末尾と先頭を削除しよう
# name_list.pop()
# position.pop(0)

print(name_list)
print(position)