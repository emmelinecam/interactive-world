import time

from .animations import animations

def mushroom_reaction(choice):
    if choice == 'spotted':
        animations(20)
        print('did you not read the guide?? i\'ll let this one slide, but that\'s the only time i\'m going to help!')
    elif choice == 'plain':
        animations(20)
        print('good choice! now that we\'ve picked it up, we can add it to our inventory.')
    time.sleep(2)

def soup_prompt(mushroom_soup):
    print('Picked up 4 Plain Mushrooms! added to inventory.')
    print('great! this is turning out to be a very successful trip! ')
    print('hey, did the guide mention about the mushroom soup? i think that would be an excellent meal for today. shall we pull up the recipie?')
    guide = input('do you remember which key to press to pull up the guide? press G! ')
    animations(40)
    time.sleep(2)
    print('hey, back to the guide! so, you fancy a mushroom soup today? no problemo!')
    print('ingredients for mushroom soup are:', mushroom_soup)
    print('we\'ve already got the mushrooms, so we can remove those from the list!')
    mushroom_soup.pop(1)
    animations(20)
    print(mushroom_soup)
    time.sleep(4)
    print('ah, looks like we\'ll have to buy some of these ingredients. i don\'t think we\'ll find chicken stock out here!')
    print('shall we head to the village? it\'s just across the forest.')
    time.sleep(3)