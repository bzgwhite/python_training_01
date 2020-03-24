"""
ExcelのIF関数ありましたね。
プログラミングでもIF条件分岐がありますよ。

記述ルール

・条件がTrueだった場合の処理
if 論理式 :
    Trueの時の処理

・条件をTrueの時とFalseの処理がある時
if 論理式 :
    Trueの時の処理
else:
    Falseの時の処理

**重要**
Pythonでif文、繰り返し文を
使用する時はネスト（入れ子）を使用する必要があります。

通常入れ子をする時は開始地点と終了地点を指定するのですが、
Pythonの場合は「インデント（字下げ）」で行います。

if 条件式:
    このように字下げを行う
ここの次点でif文の処理が終了している。


問題：以下を出力せよ
合格


"""



score = 59


if score >= 60:
    print("合格")
else:
    print("不合格")

