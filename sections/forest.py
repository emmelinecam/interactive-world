import time

from .animations import animations

def forest_scene():
    animations(30)
    print('  ^    ^    ^    ^    ^    ^  ')
    print(' / \  / \  / \  / \  / \  / \ ')
    print(' ---  ---  ---  ---  ---  ---')
    print('  |    |    |    |    |    |  ')
    print('we\'re in a forest! be careful of those thorns!')
    print('let\'s gather some things for cooking!')
    time.sleep(2)
    press = input('press P to pick up an item! ')
    print('    ---        ---     ')
    print('  / * * \    /     \   ')
    print('  -------    -------   ')
    print('    |_|        |_|      ')
    

def get_mushroom_choice():
    print('ooh, some mushrooms! but, which one is safe to eat?')
    guide = input('let\'s check the guide! to pull up the guide, press G! ')
    animations(40)
    print('welcome to the guide! so, mushrooms, is it? i can tell you all about those!')
    print('Spotted mushroom: grows in the forest and the flower field. NOT SAFE to eat. toxicity level: 60/100.')
    print('Plain mushroom: grows in the forest. SAFE to eat. recommended dish: Mushroom Soup. toxicity level: 2/100.')
    time.sleep(2)
    choice = input('so, what\'s it gonna be? spotted or plain? ')
    return choice