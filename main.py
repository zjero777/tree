import pygame as pg
import pygame_gui as gui
from tree import Tree
from os import path
import math

from ui import UI_panel

data_dir = 'data'

class App:
    def __init__(self) -> None:
        pg.init()
        vidinfo = pg.display.Info()
        viewport = pg.Rect(0,0,vidinfo.current_w, vidinfo.current_h)
        self.screen = pg.display.set_mode(viewport.size)
        self.screen.fill(pg.Color('black'))   
        self.result = self.screen.copy()
        self.is_runing = True
        
        self.tree = Tree()
        self.tree.draw(self.result)

        self.manager = gui.UIManager(viewport.size, path.join(data_dir, 'theme.json'))
        self.ui_panel = UI_panel(self)
        
        

    def run(self):
        while self.is_runing:
            self.screen.fill(pg.Color('black'))
            dt = pg.time.Clock().tick(60)/1000.0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_runing = False
                if event.type == gui.UI_BUTTON_PRESSED:
                    if event.ui_object_id=='panel.run_button':
                        self.tree.change_config(angle=self.ui_panel.angle, 
                                                max_depth=self.ui_panel.max_depth, 
                                                branch_propogation=self.ui_panel.branch_propogation)
                        self.tree.draw(self.result)
                    

                    
                self.ui_panel.process_events(event)
                self.manager.process_events(event)
            
            self.manager.update(dt)
            self.screen.blit(self.result, (0,0))
            self.manager.draw_ui(self.screen)
            pg.display.update()    
            
            
    def update(self):
        pass
    
    def draw(self):
        pass

if __name__=='__main__':
    app = App()
    app.run()