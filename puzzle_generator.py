import svgwrite
from xml.dom import minidom
import random
import subprocess
import os
from database import DataBase as DB
from math import sqrt, ceil
import ftplib
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
    q1 = matrix[1]
    q2 = matrix[2]
    q3 = matrix[3]
    if matrix[1]== 0:
        q1 = 2
    if matrix[2] == 0:
        q2 = 2
    if matrix[3] == 0:
        q3 = 2
    key = str(q1) + str(q2) + str(q3)
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
            clip_path = dwg.defs.add(dwg.clipPath(
                id=f'my_clip_path{i}', clipPathUnits="userSpaceOnUse"))  # name the clip path
            p = svgwrite.path.Path(path_strings[0])
            clip_path.add(p)
            doc.unlink()
    max_puzzles = i
    # print(path_strings)

    # clip_path.add(dwg.circle((5*mm, 5*mm), 10*mm)) #things inside this shape will be drawn

    # fig = dwg.rect(insert=(0,0), size=('100%', '100%'), fill='white')  # White background
    # dwg.add(fig)
    l = 100
    d = 70
    for i in range(ceil(sqrt(len(matrix)))):
        for j in range(ceil(sqrt(len(matrix)))):
            if(len(matrix) == (i*ceil(sqrt(len(matrix)))+j)):
                break
            time = random.randint(1, 20)
            # test = dwg.add(dwg.g(id=f'test{i+j}', stroke='red', stroke_width=1, fill='black', fill_opacity=1, clip_path="url(#my_clip_path1)"))
            # testCircle.add(dwg.circle((5*mm, 10*mm), 10*mm))
            color = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            puzzle_num = random.randint(0, max_puzzles)
            if step < 5:
                stikers = stickers_1
            else:
                stikers = stickers_2

            if(matrix[i*ceil(sqrt(len(matrix)))+j][5] > 0.5):
                time = str(matrix[i*ceil(sqrt(len(matrix)))+j][5]*time/20)
            else:
                time = '1.5'
            img = dwg.image(get_sticker(matrix[i*ceil(sqrt(len(matrix)))+j], stikers),
                            transform=f"translate({i*d-10},{j*d-10})",
                            width=l, height=l)
            params2 = {
                "type": "scale",
                "additive": "sum",
                "from": "0.7 0.7",
                "to": "1 1",
                "begin": str((i+j)/10)+"s",
                "values": "0.8;1;0.8",
                "dur": time+"s",
                "repeatCount": "indefinite"
            }
            an2 = svgwrite.animate.AnimateTransform(
                transform="scale", **params2)
            an2['attributeName'] = 'transform'

            fig = dwg.rect((0, 0), (l, l),
                           stroke='black',
                           stroke_width=1,
                           transform=f"translate({i*d},{j*d})",
                           clip_path=f"url(#my_clip_path{puzzle_num})").fill(svgwrite.rgb(*color))
            # print(fig)
            # dwg.add(fig)
            # test.add(fig)
            # fig.add(test)
            # img.add(an)
            img.add(an2)
            dwg.add(img)
        if(len(matrix) == (i*ceil(sqrt(len(matrix)))+j)):
            break
    # dwg.save()

    # dwg = svgwrite.drawing.Drawing('1.svg')

    # dwg.add(p)

    dwg.save()
    session = ftplib.FTP('reflexo.space','tn23m_reflexo','F3Btfet&')
    file = open('x1.svg','rb')                  # file to send
    session.storbinary('STOR x1.svg', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
