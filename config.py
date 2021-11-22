''' 
@name: config file
@include: data game
@note:
    - 22/11
        + mình get url bằng lệnh: os.path.join(os.getcwd(), 'assets/font/font.ttf')
        + nhưng trên win nó ra đường dẫn kiểu: D:\\python\\assets/font/font.ttf
        + nhìn nó tức
        + nên sửa lại đường dẫn tương đối nha 
'''
import glob

# font
FONTPATH = './assets/font/font.ttf'

#game images

BULLET_IMAGE_PATHS = {
    'up': './assets/images/bullet/bullet_up.png',
    'down': './assets/images/bullet/bullet_down.png',
    'left': './assets/images/bullet/bullet_left.png',
    'right': './assets/images/bullet/bullet_right.png'
}

ENEMY_TANK_IMAGE_PATHS = {
    '1': [
        './assets/images/enemyTank/enemy_1_0.png',
        './assets/images/enemyTank/enemy_1_1.png',
        './assets/images/enemyTank/enemy_1_2.png',
        './assets/images/enemyTank/enemy_1_3.png'
    ],
    '2': [
        './assets/images/enemyTank/enemy_2_0.png',
        './assets/images/enemyTank/enemy_2_1.png',
        './assets/images/enemyTank/enemy_2_2.png',
        './assets/images/enemyTank/enemy_2_3.png'
    ],
    '3': [
        './assets/images/enemyTank/enemy_3_0.png',
        './assets/images/enemyTank/enemy_3_1.png',
        './assets/images/enemyTank/enemy_3_2.png',
        './assets/images/enemyTank/enemy_3_3.png'
    ],
    '4': [
        './assets/images/enemyTank/enemy_4_0.png',
        './assets/images/enemyTank/enemy_4_1.png',
        './assets/images/enemyTank/enemy_4_2.png',
        './assets/images/enemyTank/enemy_4_3.png'
    ]
}
PLAYER_TANK_IMAGE_PATHS = {
    'player1': [
        './assets/images/playerTank/tank_T1_0.png',
        './assets/images/playerTank/tank_T1_1.png',
        './assets/images/playerTank/tank_T1_2.png'
    ],
    'player2': [
        './assets/images/playerTank/tank_T2_0.png',
        './assets/images/playerTank/tank_T2_1.png',
        './assets/images/playerTank/tank_T2_2.png'
    ]
}

FOOD_IMAGE_PATHS = {
    'boom': './assets/images/food/food_boom.png',
    'clock': './assets/images/food/food_clock.png',
    'gun': './assets/images/food/food_gun.png',
    'iron': './assets/images/food/food_iron.png',
    'protect': './assets/images/food/food_protect.png',
    'star': './assets/images/food/food_star.png',
    'tank': './assets/images/food/food_tank.png'
}
HOME_IMAGE_PATHS = [
    './assets/images/home/home1.png',
    './assets/images/home/home_destroyed.png'
]
SCENE_IMAGE_PATHS = {
    'brick': './assets/images/scene/brick.png',
    'ice': './assets/images/scene/ice.png',
    'iron': './assets/images/scene/iron.png',
    'river1': './assets/images/scene/river1.png',
    'river2': './assets/images/scene/river2.png',
    'tree': './assets/images/scene/tree.png'
}
OTHER_IMAGE_PATHS = {
    'appear': './assets/images/others/appear.png',
    'background': './assets/images/others/background.png',
    'boom_dynamic': './assets/images/others/boom_dynamic.png',
    'boom_static': './assets/images/others/boom_static.png',
    'gameover': './assets/images/others/gameover.png',
    'logo': './assets/images/others/logo.png',
    'mask': './assets/images/others/mask.png',
    'protect': './assets/images/others/protect.png',
    'tip': './assets/images/others/tip.png',
    'gamebar': './assets/images/others/gamebar.png'
}


#audio 
AUDIO_PATHS = {
    'add': './assets/audios/add.wav',
    'bang': './assets/audios/bang.wav',
    'blast': './assets/audios/blast.wav',
    'fire': './assets/audios/fire.wav',
    'Gunfire': './assets/audios/Gunfire.wav',
    'hit': './assets/audios/hit.wav',
    'start': './assets/audios/start.wav'
}

#screen
WIDTH = 630
HEIGHT = 630
BORDER_LEN = 3
GRID_SIZE = 24
PANEL_WIDTH = 150
TITLE = 'Tank-1990'

#level
# LEVELFILEDIR = './modules/levels'
LEVELFILEPATHS = glob.glob("./modules/levels/*.lvl")

# import os

#font
# FONTPATH = os.path.join(os.getcwd(), 'assets/font/font.ttf')

# #game images

# BULLET_IMAGE_PATHS = {
#     'up': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_up.png'),
#     'down': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_down.png'),
#     'left': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_left.png'),
#     'right': os.path.join(os.getcwd(), 'assets/images/bullet/bullet_right.png')
# }

# ENEMY_TANK_IMAGE_PATHS = {
#     '1': [
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_0.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_1.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_2.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_1_3.png')
#     ],
#     '2': [
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_0.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_1.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_2.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_2_3.png')
#     ],
#     '3': [
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_0.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_1.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_2.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_3_3.png')
#     ],
#     '4': [
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_0.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_1.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_2.png'),
#         os.path.join(os.getcwd(), 'assets/images/enemyTank/enemy_4_3.png')
#     ]
# }
# PLAYER_TANK_IMAGE_PATHS = {
#     'player1': [
#         os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T1_0.png'),
#         os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T1_1.png'),
#         os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T1_2.png')
#     ],
#     'player2': [
#         os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T2_0.png'),
#         os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T2_1.png'),
#         os.path.join(os.getcwd(), 'assets/images/playerTank/tank_T2_2.png')
#     ]
# }

# FOOD_IMAGE_PATHS = {
#     'boom': os.path.join(os.getcwd(), 'assets/images/food/food_boom.png'),
#     'clock': os.path.join(os.getcwd(), 'assets/images/food/food_clock.png'),
#     'gun': os.path.join(os.getcwd(), 'assets/images/food/food_gun.png'),
#     'iron': os.path.join(os.getcwd(), 'assets/images/food/food_iron.png'),
#     'protect': os.path.join(os.getcwd(), 'assets/images/food/food_protect.png'),
#     'star': os.path.join(os.getcwd(), 'assets/images/food/food_star.png'),
#     'tank': os.path.join(os.getcwd(), 'assets/images/food/food_tank.png')
# }
# HOME_IMAGE_PATHS = [
#     os.path.join(os.getcwd(), 'assets/images/home/home1.png'),
#     os.path.join(os.getcwd(), 'assets/images/home/home_destroyed.png')
# ]
# SCENE_IMAGE_PATHS = {
#     'brick': os.path.join(os.getcwd(), 'assets/images/scene/brick.png'),
#     'ice': os.path.join(os.getcwd(), 'assets/images/scene/ice.png'),
#     'iron': os.path.join(os.getcwd(), 'assets/images/scene/iron.png'),
#     'river1': os.path.join(os.getcwd(), 'assets/images/scene/river1.png'),
#     'river2': os.path.join(os.getcwd(), 'assets/images/scene/river2.png'),
#     'tree': os.path.join(os.getcwd(), 'assets/images/scene/tree.png')
# }
# OTHER_IMAGE_PATHS = {
#     'appear': os.path.join(os.getcwd(), 'assets/images/others/appear.png'),
#     'background': os.path.join(os.getcwd(), 'assets/images/others/background.png'),
#     'boom_dynamic': os.path.join(os.getcwd(), 'assets/images/others/boom_dynamic.png'),
#     'boom_static': os.path.join(os.getcwd(), 'assets/images/others/boom_static.png'),
#     'gameover': os.path.join(os.getcwd(), 'assets/images/others/gameover.png'),
#     'logo': os.path.join(os.getcwd(), 'assets/images/others/logo.png'),
#     'mask': os.path.join(os.getcwd(), 'assets/images/others/mask.png'),
#     'protect': os.path.join(os.getcwd(), 'assets/images/others/protect.png'),
#     'tip': os.path.join(os.getcwd(), 'assets/images/others/tip.png'),
#     'gamebar': os.path.join(os.getcwd(), 'assets/images/others/gamebar.png')
# }


# #audio 
# AUDIO_PATHS = {
#     'add': os.path.join(os.getcwd(), 'assets/audios/add.wav'),
#     'bang': os.path.join(os.getcwd(), 'assets/audios/bang.wav'),
#     'blast': os.path.join(os.getcwd(), 'assets/audios/blast.wav'),
#     'fire': os.path.join(os.getcwd(), 'assets/audios/fire.wav'),
#     'Gunfire': os.path.join(os.getcwd(), 'assets/audios/Gunfire.wav'),
#     'hit': os.path.join(os.getcwd(), 'assets/audios/hit.wav'),
#     'start': os.path.join(os.getcwd(), 'assets/audios/start.wav')
# }

# #screen
# WIDTH = 630
# HEIGHT = 630
# BORDER_LEN = 3
# GRID_SIZE = 24
# PANEL_WIDTH = 150
# TITLE = 'Tank-1990'

# #level
# LEVELFILEDIR = os.path.join(os.getcwd(), 'modules/levels')
# LEVELFILEPATHS = [os.path.join(LEVELFILEDIR, filename) for filename in sorted(os.listdir(LEVELFILEDIR))]