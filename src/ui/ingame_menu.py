import pygame
from ui.buttons import Buttons
from load_image import load_image
from sprites.towers import Tower


class IngameMenu():

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 28)

        self.x = 962
        self.y = 0
        self.rect = (self.x, self.y, 318, 720)
        self.bg_color = (118, 109, 103)

        self.basic_tower = Buttons(
            self.x+30, 180, load_image("tower1.png"), load_image("tower1_alt.png"))
        self.sniper_tower = Buttons(self.x+120, 180, load_image("sniper.png"))
        self.sell_button = Buttons(
            self.x+20, 400, load_image("sell.png"), load_image("sell_alt.png"))
        self.retire_button = Buttons(self.x+160, 620, load_image("retire.png"))
        self.pause_button = Buttons(
            self.x+20, 620, load_image("pause.png"), load_image("pause_alt.png"))

        self.tower_type = None
        self.tower_selected = False
        self.sell_mode = False

        self.tower_preview = None
        self.tower_preview_rect = None

    def draw_all(self, display, health, money, wave_nro, waves):
        health_text = self.font.render(
            f"Health: {health}", True, (255, 255, 255))
        money_text = self.font.render(f"Money: {money}", True, (255, 255, 255))
        wave_text = self.font.render(
            f"Wave: {wave_nro}/{waves}", True, (255, 255, 255))
        towers_font = pygame.font.SysFont("Arial", 36)
        towers_text = towers_font.render("Towers", True, (255, 255, 255))

        pygame.draw.rect(display, self.bg_color, self.rect)
        display.blit(health_text, (self.x+20, 50))
        display.blit(money_text, (self.x+150, 50))
        display.blit(wave_text, (self.x + 100, 10))
        display.blit(towers_text, (self.x+100, 120))
        
        self.basic_tower.draw(display)
        self.sniper_tower.draw(display)
        self.sell_button.draw(display)
        self.retire_button.draw(display)
        self.pause_button.draw(display)
        
        self.draw_tower_info(display, self.x+40, 270)
        self.draw_tower_info(display, self.x+130, 270, "sniper")

        if self.tower_selected:
            tower = Tower(self.tower_preview_rect.center, self.tower_type)
            tower.draw_range(display)
            display.blit(self.tower_preview, self.tower_preview_rect)

        if self.sell_mode:
            self.sell_button.alt = True
        else:
            self.sell_button.alt = False

    def set_tower_preview(self, pos):
        if self.tower_type == "sniper":
            self.tower_preview = self.sniper_tower.image
        else:
            self.tower_preview = self.basic_tower.image
        self.tower_preview_rect = self.tower_preview.get_rect()
        self.tower_preview_rect.center = pos
        
    def draw_tower_info(self,display, x, y, tower_type=None):
        info_font = pygame.font.SysFont("Arial", 16)
        line_heigth = 18
        tower = Tower((0,0), tower_type)
        
        cost_text = f"cost: {tower.price}"
        cost_surface = info_font.render (cost_text, True, (255, 255, 255))
        
        damage_text = f"damage: {tower.damage}"
        damage_surface = info_font.render (damage_text, True, (255, 255, 255))
        
        range_text = f"range: {tower.range // 10}"
        range_surface = info_font.render (range_text, True, (255, 255, 255))
        
        fire_rate_text = f"fire rate: {10000//tower.cooldown}"
        fire_rate_surface = info_font.render (fire_rate_text, True, (255, 255, 255))
        
        display.blit(cost_surface, (x, y))
        display.blit(damage_surface, (x, y + line_heigth))
        display.blit(range_surface, (x, y + (line_heigth*2)))
        display.blit(fire_rate_surface, (x, y + (line_heigth*3)))
        
        
