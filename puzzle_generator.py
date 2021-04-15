import svgwrite
from xml.dom import minidom
import random
import subprocess
import os

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

def get_sticker(q1, q2, q3):
    key = q1 + q2 + q3
    return stickers[key]

def get_puzzle(matrix):
    random.seed(42)

    dwg = svgwrite.Drawing('x1.svg', size=(20000, 20000))
    fig = dwg.rect(insert=(0,0), size=('100%', '100%'), fill='white')  # White background

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

    fig = dwg.rect(insert=(0,0), size=('100%', '100%'), fill='white')  # White background
    dwg.add(fig)
    l = 300
    d = 100
    for i in range(10):
        for j in range(10):
            # test = dwg.add(dwg.g(id=f'test{i+j}', stroke='red', stroke_width=1, fill='black', fill_opacity=1, clip_path="url(#my_clip_path1)"))
            # testCircle.add(dwg.circle((5*mm, 10*mm), 10*mm))
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            puzzle_num = random.randint(0, max_puzzles)
            img = dwg.image(get_sticker(matrix[i*10+j]), 
                transform=f"translate({i*l-d},{j*l-d})",
                width=l, height=l,
                clip_path=f"url(#my_clip_path{puzzle_num})")
            fig = dwg.rect((0, 0), (l, l),
                stroke='black',
                stroke_width=1,
                transform=f"translate({i*l},{j*l})",
                clip_path=f"url(#my_clip_path{puzzle_num})").fill(svgwrite.rgb(*color))
            # print(fig)
            # dwg.add(fig)
            # test.add(fig)
            # fig.add(test)
            dwg.add(img)
    # dwg.save()

    # dwg = svgwrite.drawing.Drawing('1.svg')

    # dwg.add(p)

    dwg.save()
    # bashCommand = 'sshpass -p "F3Btfet&" scp x1.svg tn23m_reflexo@reflexo.space:x12.svg'
    # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()