''' 
@name: config file
@include: data game
'''
import os

#font
FONTPATH = os.path.join(os.getcwd(), 'assets/font/font.ttf')

#game images

BULLET_IMAGE_PATHS = {
    'up': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_up.png'),
    'down': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_down.png'),
    'left': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_left.png'),
    'right': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_right.png')
}

ENEMY_TANK_IMAGE_PATHS = {
    '1': [
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_0.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_1.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_2.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_3.png')
    ],
    '2': [
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_0.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_1.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_2.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_3.png')
    ],
    '3': [
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_0.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_1.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_2.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_3.png')
    ],
    '4': [
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_0.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_1.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_2.png'),
        os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_3.png')
    ]
}
PLAYER_TANK_IMAGE_PATHS = {
    'player1': [
        os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T1_0.png'),
        os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T1_1.png'),
        os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T1_2.png')
    ],
    'player2': [
        os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T2_0.png'),
        os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T2_1.png'),
        os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T2_2.png')
    ]
}

FOOD_IMAGE_PATHS = {
    'boom': os.path.join(os.getcwd(), 'assets/images/food/food_boom.png'),
    'clock': os.path.join(os.getcwd(), 'assets/images/food/food_clock.png'),
    'gun': os.path.join(os.getcwd(), 'assets/images/food/food_gun.png'),
    'iron': os.path.join(os.getcwd(), 'assets/images/food/food_iron.png'),
    'protect': os.path.join(os.getcwd(), 'assets/images/food/food_protect.png'),
    'star': os.path.join(os.getcwd(), 'assets/images/food/food_star.png'),
    'tank': os.path.join(os.getcwd(), 'assets/images/food/food_tank.png')
}
HOME_IMAGE_PATHS = [
    os.path.join(os.getcwd(), 'assets/images/home/home1.png'),
    os.path.join(os.getcwd(), 'assets/images/home/home_destroyed.png')
]
SCENE_IMAGE_PATHS = {
    'brick': os.path.join(os.getcwd(), 'assets/images/scene/brick.png'),
    'ice': os.path.join(os.getcwd(), 'assets/images/scene/ice.png'),
    'iron': os.path.join(os.getcwd(), 'assets/images/scene/iron.png'),
    'river1': os.path.join(os.getcwd(), 'assets/images/scene/river1.png'),
    'river2': os.path.join(os.getcwd(), 'assets/images/scene/river2.png'),
    'tree': os.path.join(os.getcwd(), 'assets/images/scene/tree.png')
}
OTHER_IMAGE_PATHS = {
    'appear': os.path.join(os.getcwd(), 'assets/images/others/appear.png'),
    'background': os.path.join(os.getcwd(), 'assets/images/others/background.png'),
    'boom_dynamic': os.path.join(os.getcwd(), 'assets/images/others/boom_dynamic.png'),
    'boom_static': os.path.join(os.getcwd(), 'assets/images/others/boom_static.png'),
    'gameover': os.path.join(os.getcwd(), 'assets/images/others/gameover.png'),
    'logo': os.path.join(os.getcwd(), 'assets/images/others/logo.png'),
    'mask': os.path.join(os.getcwd(), 'assets/images/others/mask.png'),
    'protect': os.path.join(os.getcwd(), 'assets/images/others/protect.png'),
    'tip': os.path.join(os.getcwd(), 'assets/images/others/tip.png'),
    'gamebar': os.path.join(os.getcwd(), 'assets/images/others/gamebar.png')
}


#audio 
AUDIO_PATHS = {
    'add': os.path.join(os.getcwd(), 'assets/audios/add.wav'),
    'bang': os.path.join(os.getcwd(), 'assets/audios/bang.wav'),
    'blast': os.path.join(os.getcwd(), 'assets/audios/blast.wav'),
    'fire': os.path.join(os.getcwd(), 'assets/audios/fire.wav'),
    'Gunfire': os.path.join(os.getcwd(), 'assets/audios/Gunfire.wav'),
    'hit': os.path.join(os.getcwd(), 'assets/audios/hit.wav'),
    'start': os.path.join(os.getcwd(), 'assets/audios/start.wav')
}

#screen
WIDTH = 630
HEIGHT = 630
BORDER_LEN = 3
GRID_SIZE = 24
PANEL_WIDTH = 150
TITLE = 'Tank-1990'

#level
LEVELFILEDIR = os.path.join(os.getcwd(), 'modules/levels')
LEVELFILEPATHS = [os.path.join(LEVELFILEDIR, filename) for filename in sorted(os.listdir(LEVELFILEDIR))]