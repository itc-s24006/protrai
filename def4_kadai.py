#s24006
#main関数を使っておみくじ処理をする


import random
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

def main():
    kekka = omikuji()
    print("結果は", kekka, "です。")


if __name__ == "__main__":
    main()
