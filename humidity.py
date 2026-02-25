# 湿度計算プログラム（モード選択付き）
while True:
    mode = input("\nモードを選択(湿度・蒸気・飽和) → ")

    if mode == "0":
        print("プログラムを終了します。")
        break

    # 1. 湿度を求める
    if mode == "湿度":
        g = float(input("水蒸気の質量(g) → "))
        h = float(input("飽和水蒸気量(g/m**3) → "))
        p = (g / h) * 100
        print(f"結果: 湿度は {p:.2f} % です。")

    # 2. 水蒸気の質量を求める (湿度 × 飽和 / 100)
    elif mode == "水蒸気":
        p = float(input("湿度(%) → "))
        h = float(input("飽和水蒸気量(g/m**3) → "))
        g = (p * h) / 100
        print(f"結果: 水蒸気の質量は {g:.2f} g/m³ です。")

    # 3. 飽和水蒸気量を求める (質量 / 湿度 × 100)
    elif mode == "飽和":
        g = float(input("水蒸気の質量(g) → "))
        p = float(input("湿度(%) → "))
        h = (g / p) * 100
        print(f"結果: 飽和水蒸気量は {h:.2f} g/m³ です。")

    else:
        print("正しい番号を入力してください。")
