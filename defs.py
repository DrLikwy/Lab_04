import string
import random
import pygame


def key_maker(enter):  # генератор ключа
    a = string.ascii_uppercase
    block_1 = enter[3:6] + random_choice(a) + random_choice(a)
    block_2 = enter[:3] + random_choice(a) + random_choice(a)
    block_3 = str(int(enter[3:6]) + int(enter[:3]))
    if len(block_3) == 3:
        return str(block_1) + '-' + str(block_2) +' 0'+str(block_3)
    if len(block_3) == 4:
        return str(block_1) + '-' + str(block_2) +' '+str(block_3)


def random_choice(a): # рандомайзер
    b = random.choice(a)
    return b


def play(): # проигрывание музыки
    pygame.mixer.music.load("MUS.mp3")
    pygame.mixer.music.play(loops=0)


def stop(): # остановка музыки
    pygame.mixer.music.stop()