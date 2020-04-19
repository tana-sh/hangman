import random
def hangman(word):
    # 間違えた数
    wrong = 0
    # ハングマンの絵を描いていくためのリスト
    stages =[
        '',
        '______     ',
        '|     |    ',
        '|     |    ',
        '|     O    ',
        '|    /|\   ',
        '|    / \   ',
        '|'
        ]

    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')

    # ゲームを進行するためのループ処理
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予想してね:'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You Win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('You Lose! answer is {}'.format(word))


if __name__ == '__main__':
    word_list = ['cat', 'dog', 'ant', 'eat', 'sit', 'ps4', 'pen']
    n = random.randint(0, len(word_list))
    hangman(word_list[n])

