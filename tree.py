import pygame as pg
import math

class Tree:
    def __init__(self, start_x=None, start_y=None,angle=30, max_depth=10, branch_propogation = 3) -> None:
        self.surface = None
        self.change_config(x=start_x, y=start_y,angle=angle, max_depth=max_depth, branch_propogation=branch_propogation)


    def draw_branch(self, x=None,y=None,height=None, angle=0,depth=math.pi / 2):
        if depth>self.max_depth: return

        end_x = x - height * math.sin(angle)
        end_y = y - height * math.cos(angle)    
        
        pg.draw.line(self.surface, pg.Color('white'), (math.trunc(x),math.trunc(y)), (math.trunc(end_x), math.trunc(end_y)), 1)
        
        new_height = (height * 8) / 12
        if self.branch_propagation % 2 == 0:
            angle_start = angle-self.angle_increment / 2 - (math.trunc(self.branch_propagation / 2) - 1) * self.angle_increment
        else:
            angle_start = angle-math.trunc(self.branch_propagation / 2) * self.angle_increment
        for i in range(self.branch_propagation):
            self.draw_branch(end_x, end_y, new_height, angle_start + i * self.angle_increment, depth + 1)


    def change_config(self, x=None,y=None,angle=30, max_depth=10, branch_propogation = 3):
        self.angle = angle
        self.angle_increment = (angle * math.pi) / 180;
        self.max_depth = max_depth
        self.branch_propagation = branch_propogation
        self.start_x = x
        self.start_y = y
        
        
        
    def draw(self, surface):
        self.surface = surface
        viewport = self.surface.get_rect()
        if self.start_x==None: 
            self.start_x = viewport.width / 2
        if self.start_y==None: 
            self.start_y = viewport.height
        self.height = (viewport.height * 8) / 24;        
        
        surface.fill(0)
        self.draw_branch(x=self.start_x, y=self.start_y, height=self.height)