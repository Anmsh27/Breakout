import pygame
from os import walk


def import_folder(path):
    surface_list = []

    for _, __, imgs in walk(path):
        for img_surf in imgs:
            full_path = path + '/' + img_surf
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)

    return surface_list
