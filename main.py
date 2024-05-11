import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# CSVファイルの読み込み（index_col=0を指定して、最初の列を行ラベルとして使用）
df = pd.read_csv('s-year-a.csv', index_col=0)

# 行ラベル（カテゴリ）を取得
categories = df.index

# 年度を列のラベルから取得
years = df.columns

# 各カテゴリについてプロット
for category in categories:
    values = df.loc[category].values
    plt.figure(figsize=(14, 8))
    plt.plot(years, values, marker='o')  # プロット
    # 各データポイントに値を表示
    for x, y in zip(years, values):
        plt.text(x, y, format(y, ','), ha='center', va='bottom')
    plt.xticks(rotation=45)
    plt.xlabel('年度')
    plt.ylabel(category)
    plt.title(f'年度別の推移 - {category}')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'images/{category}.png')
    plt.close()  # 現在の図を閉じて次の図のためにクリア
