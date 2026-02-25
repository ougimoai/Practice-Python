#逆接待じゃんけん
import random
import time

def slow_print(message, delay=0.15):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print() #最後に改行を入れる


mode = 2
while True:
    I = input("\nあなたの手は？")
    #自分の手の設定
    hands = ["グー", "チョキ", "パー"]
    if I == "勝たせて":
        mode = 1
        slow_print("……仕方がないですねぇ。")
        continue
    if I not in hands:
        slow_print("……おや、手が震えて正しく入力できていませんよ？")
        continue
    #2でのcmpの手
    if mode == 2:
        cmp = {"グー": "パー", "チョキ": "グー","パー":"チョキ"}
        you = cmp[I]
    #1(接待)でのcmpの手
    else:
        cmp = {"パー": "グー", "グー": "チョキ","チョキ":"パー"}
        you = cmp[I]

    #共通の演出
    slow_print("\nじゃん、けん…………")
    time.sleep(1) 
    slow_print("ぽん！")
    slow_print(f"{I}VS{you}")
    slow_print("これは…………")
    time.sleep(1)

    #モードが2の時の結果
    if mode == 2:
        slow_print("あなたの負けですねぇ。まぁ、次は勝てますって。")
    #モードが1の時の結果
    else:
        slow_print("あなたの勝ちですね。……これで満足ですか？")

    #共通の再戦
    time.sleep(1)
    while True:
        sai = input("\nもう一度勝負しますか？(はい/いいえ)")

#"はい"の時の再戦
        if sai == "はい":
            if mode == 2:
                slow_print("次は勝てるといいですね")
                break
            elif mode == 1:
                slow_print("次は正々堂々ですよ？")
                mode = 2
                break
#"いいえ"の時の再戦
        elif sai == "いいえ":
            if mode == 1:
                slow_print("勝ち逃げ、ですか。")
                exit()
            if mode == 2:
                slow_print("おや、逃げるのですか？…そんなはずはありませんよね？")
    if sai == "いいえ" and mode == 2:
        pass

