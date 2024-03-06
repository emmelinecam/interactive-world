from .animations import animations

def supermarket_scene(mushroom_soup):
    print('cool! do you remember what we need? let\'s check the list!')
    print(mushroom_soup)
    print('ok, so the only thing we need from here is the chicken stock! but i\'m not too sure where it would be. let\'s look around!')
    print('it should look something like this: 口')

def get_aisle_choice(aisles):
    if len(aisles) == 3 or len(aisles) == 2:
        if len(aisles) == 3:
            available_aisles = f"{aisles[0]}, {aisles[1]} or {aisles[2]}"
        else:
            available_aisles = f"{aisles[0]} or {aisles[1]}"
        choice = int(input(f'pick an aisle: {available_aisles}?: '))
    else:
        print(f'let\'s go down aisle {aisles[0]}')
        choice = aisles[0]
    return choice

def aisle_1_scene():
    animations(20)
    print('                 ')
    print('----------------')
    print('           ✳   ')
    print('----------------')
    print('     ◼            ')
    print('----------------')
    print('ooh, aisle 1 looks a bit bare! no chicken stock here. let\'s check a different aisle.')
    




