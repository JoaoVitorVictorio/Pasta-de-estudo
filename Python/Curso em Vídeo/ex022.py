# Exercício de criar um programa para tocar algum som de fundo.
import pygame
pygame.init()
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()