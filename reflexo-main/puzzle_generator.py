import svgwrite
from xml.dom import minidom
import random
import subprocess
import os
from database import DataBase as DB

db = DB()
stickers_1 = {
    '111': 'stickers/yellow.png',
    '112': 'stickers/yellow.png',
    '121': 'stickers/yellow.png',
    '122': 'stickers/pink.png',
    '131': 'stickers/pink.png',
    '132': 'stickers/pink.png',
    '113': 'stickers/purple.png',
    '123': 'stickers/purple.png',
    '133': 'stickers/purple.png',
    '211': 'stickers/yellow-bored.png',
    '221': 'stickers/yellow-bored.png',
    '222': 'stickers/blue-blue.png',
    '232': 'stickers/blue-blue.png',
    '212': 'stickers/blue-blue.png',
    '213': 'stickers/red-square.png',
    '223': 'stickers/red-circle.png',
    '233': 'stickers/red-circle.png',
    '231': 'stickers/red-circle.png',
    '311': 'stickers/green.png',
    '321': 'stickers/green.png',
    '312': 'stickers/red-square-bristles.png', 
    '322': 'stickers/red-square-bristles.png',
    '332': 'stickers/red-square-bristles.png',
    '331': 'stickers/red-square-bristles.png',
    '333': 'stickers/black-polygon.png',
    '323': 'stickers/black-polygon.png',
    '313': 'stickers/black-polygon.png'
}

stickers_2 = {
    '111': 'stickers/grey.png',
    '112': 'stickers/grey.png',
    '121': 'stickers/green-2.png',
    '122': 'stickers/grey.png',
    '131': 'stickers/purple-2.png',
    '132': 'stickers/purple-2.png',
    '113': 'stickers/green-2.png',
    '123': 'stickers/green-2.png',
    '133': 'stickers/purple-2.png',
    '211': 'stickers/turquoise.png',
    '221': 'stickers/pink.png',
    '222': 'stickers/pink.png',
    '232': 'stickers/blue-purple.png',
    '212': 'stickers/turquoise.png',
    '213': 'stickers/pink.png',
    '223': 'stickers/blue-purple.png',
    '233': 'stickers/blue-purple.png',
    '231': 'stickers/blue-purple.png',
    '311': 'stickers/orange.png',
    '321': 'stickers/orange.png',
    '312': 'stickers/light-pink.png', 
    '322': 'stickers/orange.png',
    '332': 'stickers/uknown.png',
    '331': 'stickers/uknown.png',
    '333': 'stickers/uknown.png',
    '323': 'stickers/orange.png',
    '313': 'stickers/light-pink.png'
}

def get_sticker(matrix, stickers):
    if matrix[1]== 0:
        matrix[1] = 2
    if matrix[2] == 0:
        matrix[2] = 2
    if matrix[3] == 0:
        matrix[3] = 2
    key = str(matrix[1]) + str(matrix[2]) + str(matrix[3])
    return stickers[key]

def get_puzzle(matrix):
    step = 1
    random.seed(42)

    dwg = svgwrite.Drawing('x1.svg', size=(3000, 3000))
    # fig = dwg.rect(insert=(0,0), size=('100%', '100%'), fill='white')  # White background

    for i, file in enumerate(os.listdir("puzzle")):
        if file.endswith(".svg"):
            fn = os.path.join("puzzle", file)
            doc = minidom.parse(fn)  # parseString also exists
            path_strings = [path.getAttribute('d') for path
                    in doc.getElementsByTagName('path')]
            p = svgwrite.path.Path(path_strings[0])
            clip_path = dwg.defs.add(dwg.clipPath(id=f'my_clip_path{i}', clipPathUnits="userSpaceOnUse")) #name the clip path
            p = svgwrite.path.Path(path_strings[0])
            clip_path.add(p)
            doc.unlink()
    max_puzzles = i
    # print(path_strings)

    # clip_path.add(dwg.circle((5*mm, 5*mm), 10*mm)) #things inside this shape will be drawn

    # fig = dwg.rect(insert=(0,0), size=('100%', '100%'), fill='white')  # White background
    # dwg.add(fig)
    l = 150
    d = 50
    for i in range(10):
        for j in range(10):
            if(len(matrix)==(i*10+j)):
                break
            time = random.randint(5, 20)
            # test = dwg.add(dwg.g(id=f'test{i+j}', stroke='red', stroke_width=1, fill='black', fill_opacity=1, clip_path="url(#my_clip_path1)"))
            # testCircle.add(dwg.circle((5*mm, 10*mm), 10*mm))
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            puzzle_num = random.randint(0, max_puzzles)
            if step < 5:
                stikers = stickers_1
            else:
                stikers = stickers_2

            img = dwg.image(get_sticker(matrix[i*10+j], stikers), 
                transform=f"translate({i*l-d},{j*l-d})",
                width=l, height=l)
            params = {
                "type": "rotate", 
                "from": f"0 1000 500", 
                "to": f"360 1000 500", 
                "dur": f"{time}s", 
                "additive": "sum", 
                "repeatCount": "indefinite"
            }
            an = svgwrite.animate.AnimateTransform(transform="rotate", **params)
            an['attributeName'] = 'transform'
            fig = dwg.rect((0, 0), (l, l),
                stroke='black',
                stroke_width=1,
                transform=f"translate({i*l},{j*l})",
                clip_path=f"url(#my_clip_path{puzzle_num})").fill(svgwrite.rgb(*color))
            # print(fig)
            # dwg.add(fig)
            # test.add(fig)
            # fig.add(test)
            img.add(an)
            dwg.add(img)
        if(len(matrix)==(i*10+j)):
            break
    # dwg.save()

    # dwg = svgwrite.drawing.Drawing('1.svg')

    # dwg.add(p)

    dwg.save()
    bashCommand = 'sshpass -p "F3Btfet&" scp x1.svg tn23m_reflexo@reflexo.space:x12.svg'
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()