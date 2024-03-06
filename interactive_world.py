from sections.animations import animations
from sections.split import split_path_scene, get_path
from sections.intro import intro_scene, welcome, get_name
from sections.forest import forest_scene, get_mushroom_choice
from sections.mushroom import mushroom_reaction, soup_prompt
from sections.village import village_scene, get_first_shop_choice
from sections.supermarket import get_aisle_choice, aisle_1_scene, supermarket_scene

welcome()
name = get_name()
intro_scene(name)

split_path_scene()
path = get_path()

if path == 'left':
    mushroom_soup = ['1 pack of butter', '4 mushrooms', '1 chicken stock', '1 pot of cream' ]
    forest_scene()
    mushroom_choice = get_mushroom_choice()
    mushroom_reaction(mushroom_choice)
    soup_prompt(mushroom_soup)
    village_scene()
    first_shop_choice = get_first_shop_choice()
    if first_shop_choice == 'supermarket':
        supermarket_scene(mushroom_soup)
        aisles = [1,2,3]
        aisle_choice = None
        while aisle_choice != 3:
            aisle_choice = get_aisle_choice(aisles)
            if aisle_choice == 1:
                aisles.remove(1)
                aisle_1_scene()
            if aisle_choice == 2:
                aisles.remove(2)
                print('aisle 2 chosen')
        print('aisle 3 chosen')
