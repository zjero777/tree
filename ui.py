import pygame as pg
import pygame_gui as gui

class UI_panel:
    def __init__(self, app) -> None:
        self.manager = app.manager
        self.tree = app.tree
        
        self.angle = self.tree.angle 
        self.max_depth = self.tree.max_depth
        self.branch_propogation = self.tree.branch_propagation
        
        run_panel = gui.elements.UIPanel(relative_rect=pg.Rect((0, 0), (400, 200)),
                                         starting_layer_height=0, 
                                         manager=self.manager)
        
        button_layout_rect = pg.Rect(0, 0, 100, -1)
        button_layout_rect.bottomright = (-10, -10)    
        run_button = gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Run',
                                             manager=self.manager, 
                                             container=run_panel,
                                             object_id='run_button',
                                             anchors={'left': 'right',
                                            'right': 'right',
                                            'top': 'bottom',
                                            'bottom': 'bottom'})

        button_layout_rect = pg.Rect(0, 0, -1, -1)
        button_layout_rect.bottomright = (-115, -10)    
        reset_button = gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Reset to default',
                                             manager=self.manager, 
                                             container=run_panel,
                                             object_id='reset_button',
                                             anchors={'left': 'right',
                                            'right': 'right',
                                            'top': 'bottom',
                                            'bottom': 'bottom'})



        layout_rect = pg.Rect(0, 0, 380, -1)
        layout_rect.topleft = (10, 10)    
        self.label_angle = gui.elements.UILabel(relative_rect=layout_rect,
                                           text=f'Angle({self.angle})',
                                           manager=self.manager,
                                           container=run_panel
                                           )
        
        layout_rect = pg.Rect(0, 0, 380, 15)
        layout_rect.topleft = (10, 30)    
        self.slider_angle = gui.elements.UIHorizontalSlider(relative_rect=layout_rect,
                                                     start_value=self.angle,
                                                     value_range=(0, 359),
                                                     manager=self.manager,
                                                     container=run_panel,
                                                     object_id='slider_angle',
                                                     anchors={'left': 'left',
                                                     'right': 'left',
                                                     'top': 'top',
                                                     'bottom': 'bottom'}
                                                     )

        layout_rect = pg.Rect(0, 0, 380, -1)
        layout_rect.topleft = (10, 50)    
        self.label_max_depth = gui.elements.UILabel(relative_rect=layout_rect,
                                           text=f'Max depth({self.max_depth})',
                                           manager=self.manager,
                                           container=run_panel
                                           )
        
        layout_rect = pg.Rect(0, 0, 380, 15)
        layout_rect.topleft = (10, 70)    
        self.slider_max_depth = gui.elements.UIHorizontalSlider(relative_rect=layout_rect,
                                                     start_value=self.max_depth,
                                                     value_range=(1, 10),
                                                     manager=self.manager,
                                                     container=run_panel,
                                                     object_id='slider_max_depth',
                                                     anchors={'left': 'left',
                                                     'right': 'left',
                                                     'top': 'top',
                                                     'bottom': 'bottom'}
                                                     )

        layout_rect = pg.Rect(0, 0, 380, -1)
        layout_rect.topleft = (10, 90)    
        self.label_branch_propogation = gui.elements.UILabel(relative_rect=layout_rect,
                                           text=f'Branch propogation({self.branch_propogation})',
                                           manager=self.manager,
                                           container=run_panel
                                           )
        
        layout_rect = pg.Rect(0, 0, 380, 15)
        layout_rect.topleft = (10, 110)    
        self.slider_branch_propogation = gui.elements.UIHorizontalSlider(relative_rect=layout_rect,
                                                     start_value=self.branch_propogation,
                                                     value_range=(1, 10),
                                                     manager=self.manager,
                                                     container=run_panel,
                                                     object_id='slider_branch_propogation',
                                                     anchors={'left': 'left',
                                                     'right': 'left',
                                                     'top': 'top',
                                                     'bottom': 'bottom'}
                                                     )
        

      
    def process_events(self, event):
        if event.type == gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_object_id=='panel.slider_angle':
                self.angle = self.slider_angle.get_current_value()
                self.label_angle.set_text(f'Angle({self.angle})')
            if event.ui_object_id=='panel.slider_max_depth':
                self.max_depth = self.slider_max_depth.get_current_value()
                self.label_max_depth.set_text(f'Max depth({self.max_depth})')
            if event.ui_object_id=='panel.slider_branch_propogation':
                self.branch_propogation = self.slider_branch_propogation.get_current_value()
                self.label_branch_propogation.set_text(f'Branch propogation({self.branch_propogation})')
        if event.type == gui.UI_BUTTON_PRESSED:
            if event.ui_object_id=='panel.reset_button':
                self.angle = 30
                self.label_angle.set_text(f'Angle({self.angle})')
                self.slider_angle.set_current_value(self.angle)
                self.max_depth = 10
                self.label_max_depth.set_text(f'Max depth({self.max_depth})')
                self.slider_max_depth.set_current_value(self.max_depth)
                self.branch_propogation = 3
                self.label_branch_propogation.set_text(f'Branch propogation({self.branch_propogation})')
                self.slider_branch_propogation.set_current_value(self.branch_propogation)
        
    
    