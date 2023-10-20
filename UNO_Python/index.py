import random

# Definindo as cores e os valores das cartas
colors = ['Red', 'Blue', 'Green', 'Yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']

# Criando o baralho
deck = [{'color': color, 'value': value} for color in colors for value in values]

# Função para embaralhar o baralho
def shuffle_deck():
    random.shuffle(deck)

# Função para distribuir cartas aos jogadores
def deal_cards(num_players, num_cards):
    players = [[] for _ in range(num_players)]
    for _ in range(num_cards):
        for i in range(num_players):
            card = deck.pop()
            players[i].append(card)
    return players

# Função para exibir a mão de um jogador
def display_hand(player_hand):
    for i, card in enumerate(player_hand):
        print(f"{i + 1}. {card['color']} {card['value']}")

# Função principal do jogo
def uno_game(num_players):
    shuffle_deck()
    players = deal_cards(num_players, 7)
    
    current_player = 0
    while True:
        print(f"\nPlayer {current_player + 1}'s turn:")
        display_hand(players[current_player])
        
        play = input("Choose a card to play (number) or 'draw' to draw a card: ")
        
        if play.lower() == 'draw':
            players[current_player].append(deck.pop())
        elif play.isdigit():
            index = int(play) - 1
            if 0 <= index < len(players[current_player]):
                card = players[current_player].pop(index)
                print(f"Played: {card['color']} {card['value']}")
                # You can add more game logic here
        else:
            print("Invalid input. Please choose a card or 'draw'.")

        current_player = (current_player + 1) % num_players

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    uno_game(num_players)