import time

from .animations import animations

def welcome():
    print('welcome, new user!')

def get_name():
    name = input('What is your name?: ')
    return name
    
def intro_scene(name):
    print(f'that\'s a lovely name, {name}. are you ready? time to adventure!')
    animations(20)

    print('''     
       --------
     /          \\
     ------------
    |            |
    |    ____    |
    |   |    |   |
    |   |   *|   |
    |   |    |   |
    --------------------------
    ''')
    print('we can go anywhere, just have to be back for 6 pm. plenty of time to explore!')
    time.sleep(2)
    print('|    |   |')
    print('|    |   |')
    print('|    |   |')
    print('|    |   |')
    print('|    |   |')
    print('|    |   |')
    print('and we\'re off! let\'s follow the road for now.')
    time.sleep(4)