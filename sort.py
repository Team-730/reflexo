stickers = {
    '111': 'yellow.jpg',
    '112': 'yellow.jpg',
    '121': 'yellow.jpg',
    '122': 'pink.jpg',
    '131': 'pink.jpg',
    '132': 'pink.jpg',
    '113': 'purple.jpg',
    '123': 'purple.jpg',
    # '133'
    # '211'
    # '221'
    # '222'
    # '232'
    # '212'
    # '213'
    # '223'
    # '233'
    # '231'
    # '311'
    # '321'
    # '312'
    # '322'
    # '332'
    # '331'
    # '333'
    # '323'
    # '313'
}

def get_values():
    return {'q1': 1, 'q2': 1, 'q3': 2}

def get_sticker(values):
    key = values['q1'] + values ['q2'] + values['q3']
    return stickers[key]