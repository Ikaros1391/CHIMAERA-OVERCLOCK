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
        
        # 🧾 Hypercapitalist Redgrave Corporation Debt
        self.debt_total = 1000000.0  
        self.cash_in_hand = 0.0
        
        # 🛡️ Defensive Attrition Layer (Low health, breakable plates)
        self.max_health = 50
        self.current_health = 50
        self.armor_plates = 3        
        
        # ⚡ Advanced Overclock Engine ("Reaper Mode")
        self.overclock_meter = 0.0    
        self.is_reaper_mode = False
        self.reaper_timer = 0.0
        self.active_element_infusion = None
        
        # 📊 Core Margin / Style Metrics (Rank D to SSS)
        self.margin_points = 0.0
        self.margin_rank = "D"
        self.margin_decay_timer = 0.0
        self.stagnation_penalty_multiplier = 1.0  
        self.combo_history = []                    
        
        # 🔫 Modular Weapon Frame / Canister Settings
        self.chimaera_weapon_form = "Pistol"  
        self.canisters = {"Slag": 3, "Pyro": 3, "Cryo": 3, "Volt": 3}
        self.cooldowns = {}
        
        # Physics Engine Connection
        spawn_x = 100 if character_name == "Corey" else 900
        self.physics = PhysicsObject(x=spawn_x, y=0)
        
        self.metadata = {
            "frame_config": [0] * 60,
            "input_buffer": []
    }
    
    def take_damage(self, damage_amount):
        """Processes incoming damage from anomalies using disposable plate logic."""
        # 🛡️ RULE 1: If she has armor plates left, a plate shatters instead of taking health damage
        if self.armor_plates > 0:
            self.armor_plates -= 1
            print(f"ARMOR PLATE SHATTERED! Plates remaining: {self.armor_plates}")
            return # Block the rest of the damage completely

        # 💔 RULE 2: If armor is completely gone, the damage punches straight into her core health
        self.current_health = max(0, self.current_health - damage_amount)
        print(f"CORE HEALTH IMPACTED! Current Health: {self.current_health}")
        
        if self.current_health <= 0:
            print("REAPER DOWN. DEBT RECOVERY OPERATION FAILED.")
        
