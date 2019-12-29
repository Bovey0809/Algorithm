import sys


def main(lines):
            # このコードは標準入力と標準出力を用いたサンプルコードです。
        # このコードは好きなように編集・削除してもらって構いません。
        # ---
        # This is a sample code to use stdin and stdout.
        # Edit and remove this code as you like.
        prices = [int(price) for price in lines[1].split(' ')]
        n, k, money = [int(i) for i in lines[0].split(' ')]

        # %%
        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i-1])
        # %%
        i = 0
        while i < len(diff):
            if diff[i] > 0:
                stock = money // prices[i]
                if stock > k:
                    stock = k
                left = money - stock * prices[i]
                while i+1 < len(diff) and diff[i+1] > 0:
                    i += 1
                money = stock * prices[i+1]
                money += left
                i += 1
            else:
                i += 1
        print(money)

if __name__ == '__main__':
        lines = []
        for l in sys.stdin:
                lines.append(l.rstrip('\r\n'))
        main(lines)
