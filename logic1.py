"""
問題 1：ユニークな要素の出現順に並べよう
整数のリスト A が与えられます。
この中から重複を取り除き、最初に出てきた順番を保ったまま要素を1行で出力してください。
"""
A = [3, 5, 3, 2, 5, 6, 2, 7]
unique = []

for num in A:
    if num not in unique:
        unique.append(num)

print(" ".join(map(str, unique)))

        
         
    
    