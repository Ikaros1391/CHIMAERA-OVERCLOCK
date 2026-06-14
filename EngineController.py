# =============================================================================
# CHIMAERA OVERCLOCK: MASTER ENGINE CONTROLLER (CORE PHYSICS & INTENT LOOP)
# =============================================================================

from StateData import PlayerState, Element
from Intent import IntentProcessor


class GameState:
    """A lightweight, zero-allocation container for the active battle data."""
    def __init__(self):
        # Coordinates and Physics Vectors
        self.position_x = 0.0
        self.position_y = 0.0
        self.position_z = 0.0
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.velocity_z = 0.0
        
        # Core Mechanical Metrics
        self.current_health = 100
        self.margin_rank = "D"
        self.overclock_charge = 0.0
        self.is_grounded = True
        self.active_hover = False
        self.hover_fuel = 2.0
        
        # Environmental and Animation Triggers
        self.is_touching_slag = False
        self.post_hit_frame_window = 0
        self.combo_gravity_lock = False
        
        # HUD / Render Flags
        self.active_element_color = (1.0, 0.2, 0.0) # Defaults to Pyro Orange-Red
        self.hud_is_scrambled = False


class EngineController:
    """
    The Master Engine Brain. 
    Directs raw hardware inputs straight into abstract player intents.
    """
    def __init__(self, active_intent_map, active_elements, physics_system):
        self.intent_map = active_intent_map      # Automatically slots in Corey, Sage, Glitch, etc.
        self.elements = active_elements          # Tracks Right-Stick Cardinal Flicks
        self.physics = physics_system            # Handles Newtonian speed and Slag pools
        self.state = GameState()
        
        # Globally Enforced Cooldowns
        self.overclock_timer = 0.0
        self.grenade_cooldown = 0.0

            # 🕹️ Right Stick Flick Input Tracking (For Canister Swaps)
        self.right_stick_horizontal_neutral = True
        self.right_stick_vertical_neutral = True
        self.flick_threshold = 0.8  # Registers a deliberate push past 80%

        # ⚡ Dual Analog Stick Click Tracking (For L3 + R3 Overclock)
        self.overclock_button_neutral = True
        

    def run_frame_update(self, raw_inputs, delta_time):
        """Processes the entire game state every single frame at a crisp 60 FPS."""
        # 1. Update Cooldown Timers
        if self.overclock_timer > 0.0:
            self.overclock_timer -= delta_time
            if self.overclock_timer <= 0.0:
                self.intent_map.is_overclocked = False
                
        if self.grenade_cooldown > 0.0:
            self.grenade_cooldown -= delta_time

        # 2. Read the Right Analog Stick: Instant Cardinal Element / Weapon Swap
        self.elements.process_stick_flick(
            raw_inputs["STICK_R_X"], 
            raw_inputs["STICK_R_Y"], 
            self.state
        )

        # 3. Process Universal Super Activation: L3 + R3
        if raw_inputs["BUTTON_L3"] and raw_inputs["BUTTON_R3"]:
            if self.state.overclock_charge >= 100.0 and not self.intent_map.is_overclocked:
                self.intent_map.is_overclocked = True
                self.state.overclock_charge = 0.0
                self.overclock_timer = 10.0  # Exactly 10 seconds of glorious chaos

        # 4. Read the Left Analog Stick Vector for Locomotion
        left_stick_x = raw_inputs["STICK_L_X"]
        left_stick_z = raw_inputs["STICK_L_Y"]

        # 5. Execute Flat Intent Map Layout (Protects Absolute Muscle Memory)
        if raw_inputs["BUTTON_SQUARE"]:
            if self.grenade_cooldown <= 0.0:
                self.intent_map.execute_utility(self.state)
                self.grenade_cooldown = 4.0  # Global utility recharge window

        elif raw_inputs["BUTTON_CIRCLE"]:
            # Pass direction vectors directly for slide-cancels or directional blinks
            self.intent_map.execute_relocation(self.state, (left_stick_x, left_stick_z))

        elif raw_inputs["BUTTON_TRIANGLE"]:
            self.intent_map.execute_counter(self.state)

        # 6. Primary and Precision Targeting Layer (L2 / R2 Override)
        self.intent_map.execute_primary_and_precision(
            self.state, 
            hold_l2=raw_inputs["BUTTON_L2"], 
            tap_r2=raw_inputs["BUTTON_R2"]
        )

        # 7. Process Sprint and Jumps (R1 / X)
        if raw_inputs["BUTTON_R1"]:
            # Back thrusters / jets ignite instantly, stacking speed vectors
            self.physics.apply_jet_propulsion_sprint(self.state, left_stick_x, left_stick_z, delta_time)
            
        if raw_inputs["BUTTON_X"]:
            if self.state.is_grounded:
                self.physics.execute_ground_jump(self.state)
            else:
                self.physics.engage_runic_or_jet_hover(self.state, delta_time)

                                 # 🎮 READ HARDWARE STICK HARDWARE DATA
        # (Assuming standard Pygame joystick index mapping for stick coordinates and clicks)
        try:
            joystick = pygame.joystick.Joystick(0)
            axis_x = joystick.get_axis(2)  # Right Stick Horizontal
            axis_y = joystick.get_axis(3)  # Right Stick Vertical
            l3_click = joystick.get_button(9)  # Left Stick Click Button
            r3_click = joystick.get_button(10) # Right Stick Click Button
            
            # Pass hardware updates down to your new stick rule filters
            self.process_right_stick_flicks(axis_x, axis_y)
            self.check_overclock_activation(l3_click, r3_click)
        except pygame.error:
            # If no physical controller is plugged in, default safe bypass
            pass
        

        # 8. Run Newtonian Physics Matrix Simulation
        self.physics.simulate_world_vectors(delta_time, self.state)

    def process_right_stick_flicks(self, axis_x, axis_y):
        """Monitors the right analog stick coordinates to trigger canister swaps."""
        # HORIZONTAL AXIS FLICK (Left / Right)
        if abs(axis_x) > self.flick_threshold:
            if self.right_stick_horizontal_neutral:
                self.player1.rotate_canister()
                self.right_stick_horizontal_neutral = False  
        else:
            self.right_stick_horizontal_neutral = True  

        # VERTICAL AXIS FLICK (Up / Down)
        if abs(axis_y) > self.flick_threshold:
            if self.right_stick_vertical_neutral:
                self.player1.rotate_canister()
                self.right_stick_vertical_neutral = False
        else:
            self.right_stick_vertical_neutral = True

    def check_overclock_activation(self, left_stick_click, right_stick_click):
        """Listens for L3 + R3 simultaneous analog clicks to pop Reaper Mode."""
        if left_stick_click and right_stick_click:
            if self.overclock_button_neutral:
                self.overclock_button_neutral = False 
                
                # Check if Corey's Overclock meter is fully charged (saturated at 100)
                if self.player1.overclock_meter >= 100.0 and not self.player1.is_reaper_mode:
                    # ACTIVATE REAPER MODE OVERCLOCK
                    self.player1.is_reaper_mode = True
                    self.player1.reaper_timer = 600.0  # 10 full seconds at 60 frames per second
                    
                    # Weapon platform copies her active grenade element
                    self.player1.active_element_infusion = self.player1.active_element
                    
                    # Drain the meter tank back to zero
                    self.player1.overclock_meter = 0.0
                    print("⚡ CHIMÆRA OVERCLOCK ACTIVE: ZERO STARTUP FRAMES ENGAGED.")
        else:
            self.overclock_button_neutral = True
                                   
