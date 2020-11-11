import math
import os
import pickle

import pygame

from level_generator.data.scripts.config import GRID_SIZE, LEVEL_WINDOW, NOTHING, BLOCK, NEXT_LINE, LEVEL_PATH


def read_f(path):
    f = open(path, 'r')
    dat = f.read()
    f.close()
    return dat


def write_f(path, dat):
    f = open(path, 'w')
    f.write(dat)
    f.close()


def load_image_dir(path, colorkey=(0, 0, 0)):
    images = {}
    for img_name in os.listdir(path):
        img = pygame.image.load(path + '/' + img_name).convert()
        img.set_colorkey(colorkey)
        images[img_name.split('.')[0]] = img.copy()
    return images


def warp_surf(surface, mask, loc, shift):
    offset = [mask.get_width() // 2, mask.get_height() // 2]
    loc = [loc[0] - offset[0], loc[1] - offset[1]]
    subsurf = clip(surface, loc[0], loc[1], mask.get_width(), mask.get_height())
    mask.set_colorkey((255, 255, 255))
    subsurf.blit(mask, (0, 0))
    subsurf.set_colorkey((0, 0, 0))
    surface.blit(subsurf, (loc[0] + shift[0], loc[1] + shift[1]))


def swap_color(img,old_c,new_c):
    global e_colorkey
    img.set_colorkey(old_c)
    surf = img.copy()
    surf.fill(new_c)
    surf.blit(img,(0,0))
    return surf


def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size, y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def rect_corners(points):
    point_1 = points[0]
    point_2 = points[1]
    out_1 = [min(point_1[0], point_2[0]), min(point_1[1], point_2[1])]
    out_2 = [max(point_1[0], point_2[0]), max(point_1[1], point_2[1])]
    return [out_1, out_2]


def corner_rect(points):
    points = rect_corners(points)
    r = pygame.Rect(points[0][0], points[0][1], points[1][0] - points[0][0], points[1][1] - points[0][1])
    return r


def points_between_2d(points):
    points = rect_corners(points)
    width = points[1][0] - points[0][0] + 1
    height = points[1][1] - points[0][1] + 1
    point_list = []
    for y in range(height):
        for x in range(width):
            point_list.append([points[0][0] + x, points[0][1] + y])
    return point_list


def angle_to(points):
    return math.atan2(points[1][1] - points[0][1], points[1][0] - points[0][0])


def horizontal_crop(loc_x, width, img):
    loc_x = int(loc_x)
    loc_x = loc_x % img.get_width()
    if loc_x + width <= img.get_width():
        return img.copy()
    else:
        left_sec = img.get_width() - loc_x
        right_sec = width - left_sec
        output_surf = pygame.Surface((width, img.get_height()))
        output_surf.blit(clip(img, loc_x, 0, left_sec, img.get_height()), (0,0))
        output_surf.blit(clip(img, 0, 0, right_sec, img.get_height()), (left_sec,0))
        colorkey = img.get_colorkey()
        output_surf.set_colorkey(colorkey)
        return output_surf


def bordering_tile_x(x):
    base_x = int(x / GRID_SIZE)
    return [base_x - 1, base_x, base_x + 1]


def blit_center(surf, surf2, pos):
    x = int(surf2.get_width() / 2)
    y = int(surf2.get_height() / 2)
    surf.blit(surf2, (pos[0] - x, pos[1] - y))


def get_center_pos(surf):
    return [int(surf.get_width() / 2), int(surf.get_height() / 2)]


def normalize(num, amt):
    if num > amt:
        num -= amt
    elif num < -amt:
        num += amt
    else:
        num = 0
    return num


def mouse_over(rect):
    if type(rect) == pygame.Rect:
        return rect.collidepoint(pygame.mouse.get_pos())
    else:
        return rect.get_rect().collidepoint(pygame.mouse.get_pos())


def level_to_string(level):
    level_list = []
    for i in range(LEVEL_WINDOW[1] // GRID_SIZE):
        y = i * GRID_SIZE + 1
        for j in range(LEVEL_WINDOW[0] // GRID_SIZE):
            x = j * GRID_SIZE + 1
            collided = False
            for block in level.level_list:
                if block.get_rect().collidepoint((x, y)) and not collided:
                    collided = True
                    level_list.append(block.type['letter'])
            if not collided:
                level_list.append(NOTHING)
        level_list.append(NEXT_LINE)
    level_string = ''.join(level_list)
    return level_string


def string_to_pickle(string, name):
    with open(LEVEL_PATH + name + '.pickle', 'wb') as file:
        pickle.dump(string, file)


def save_level(level, name):
    string_to_pickle(level_to_string(level), name)
    print("Level " + name + " saved.\n")


def load_level(game):
    name = input("Input the level name :\n")
    try:
        with open(LEVEL_PATH + name + '.pickle', 'rb') as file:
            string = pickle.load(file)
        print("Loaded " + name + " level.\n")
        return game.active_scene.convert_to_level(string)
    except:
        print("No such file found.\n")