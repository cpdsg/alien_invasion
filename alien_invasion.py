import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:

    def __init__(self):
      """管理游戏资源和行为的类"""
      pygame.init()
      self.settings = Settings()

      self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
      pygame.display.set_caption("Alien Invasion")
      self.ship = Ship(self)
      #设置背景色
      self.bg_color = (230 ,230 ,230)
    
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events_()
            self.ship.update()
            self._update_screen_()
 
    def _check_events_(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                     self.ship.moving_right = True
                 if event.key == pygame.K_LEFT:
                     self.ship.moving_left = True
                        
            elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_RIGHT:
                     self.ship.moving_right = False
                 if event.key == pygame.K_LEFT:
                     self.ship.moving_left = False
            

                
    def _update_screen_(self):
        """每次循环重新绘制屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() 

        #让最近绘制的图片可见
        pygame.display.flip()


    
if __name__ == "__main__":
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
        

    
  