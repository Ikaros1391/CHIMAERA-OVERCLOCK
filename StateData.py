import time
from Physics import PhysicsObject

class Element:
    SLAG = "Slag"
    PYRO = "Pyro"
    CRYO = "Cryo"
    VOLT = "Volt"

class PlayerState:
    def __init__(self, character_name):
        self.character_name = character_name
        
        # Hypercapitalist Economy Tracking
        self.debt_total = 1000000.0  # Project Redgrave initial price tag
        self.cash_in_hand = 0.0
        
        # Defensive Attrition Layer
        self.max_health = 50
        self.current_health = 50
        self.armor_plates = 3        # Absorbs full hits before health is touched
        
        # Advanced Overclock Engine ("Reaper Mode")
        self.overclock_meter = 0.0    # Builds to 100.0 to activate
        self.is_reaper_mode = False
        self.reaper_timer = 0.0
        self.active_element_infusion = None
        
        # Core Margin Metrics (Rank D to SSS)
        self.margin_points = 0.0
        self.margin_rank = "D"
        self.margin_decay_timer = 0.0
        self.stagnation_penalty_multiplier = 1.0  # Rises if you spam attacks
        self.combo_history = []                    # Tracks recent actions to spot repetition
        
        # Shared Modular Configurations
        self.canisters = {"Slag": 0, "Pyro": 0, "Cryo": 0, "Volt": 0}
        self.cooldowns = {}
        
        # All characters pull from the same movement vectors
        spawn_x = 100 if character_name == "Corey" else 900
        self.physics = PhysicsObject(x=spawn_x, y=0)
        
        self.metadata = {
            "frame_config": [0] * 60,
            "input_buffer": []
        }
