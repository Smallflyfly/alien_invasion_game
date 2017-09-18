class Settings():
    """store all Settings"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 7
        self.speedup_scale = 1.5
        self.ship_speed_factor = 10
        self.ship_limit = 3
        self.score_scale = 2
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        self.alien_points = 5
    
    def increase_speed(self):
        self.fleet_drop_speed = self.fleet_drop_speed * self.speedup_scale
        self.alien_speed_factor = self.alien_speed_factor * self.speedup_scale
        self.alien_points = self.alien_points * self.score_scale
