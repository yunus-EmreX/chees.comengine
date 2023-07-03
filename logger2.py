def write_log(move):
    with open('game_log.txt', 'a') as log_file:
        log_file.write(move + '\n')

def play_game():
    print("Chees.com Oyun Loglayıcı")
    print("------------------------")

    while True:
        move = input("Bir hamle girin (Çıkmak için 'q' tuşuna basın): ")
        if move.lower() == 'q':
            break

        write_log(move)

    print("Oyun loglama tamamlandı.")

play_game()
