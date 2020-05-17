"""
ExcelのSUM関数使いましたよね？
プログラミングでは、自分で関数を作ることもできます！

引数や、戻り値についてはご存知ですよね！
わからないって方はExcel講習の第6章を
受講してみましょう！

関数定義について
def 関数名 (引数):
    実行する処理を記述
    return 戻り値

このように関数を自分で定義することができます。
引数や、戻り値は必須ではありません。

<問題：下記を出力せよ>
30

"""

# 引数にlistを渡す。
# list内は全て数字で構成されており、全てを加算した結果を返す。
# 引数：[1,5,20,4]ならば、戻り値は1 + 5 + 20 + 4 = 30
def sum(ran):
    result = 0
    for one in ran:
        result += one

    return result


data = sum([1,5,20,4])

print(data)