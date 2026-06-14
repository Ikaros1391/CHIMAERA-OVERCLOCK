import pygame
from Intent import IntentProcessor, MarginRankEngine
from StateData import PlayerState, Element

class EngineController:
    def __init__(self):
        # Default empty actors initialized by Main.py later
        self.player1 = None
        self.player2 = None
        
        # 🕹️ Right Stick Flick Input Tracking (For Canister Swaps)
        self.right_stick_horizontal_neutral = True
        self.right_stick_vertical_neutral = True
        self.flick_threshold = 0.8  # Registers a deliberate push past 80%

        # ⚡ Dual Analog Stick Click Tracking (For L3 + R3 Overclock)
        self.overclock_button_neutral = True

    def process_right_stick_flicks(self, axis_x, axis_y):
        """Monitors the right analog stick coordinates to trigger canister swaps."""
        # Ensure player1 exists before evaluating inputs
        if self.player1 is None:
            return

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
        if self.player1 is None:
            return

        if left_stick_click and right_stick_click:
            if self.overclock_button_neutral:
                self.overclock_button_neutral = False 
                
                # Check if Corey's Overclock meter is fully charged (saturated at 100)
                if self.player1.overclock_meter >= 100.0 and not self.player1.is_reaper_mode:
                    # ACTIVATE REAPER MODE OVERCLOCK
                    self.player1.is_reaper_mode = True
                    self.player1.reaper_timer = 600.0  # 10 full seconds at 60 FPS
                    
                    # Weapon platform copies her active grenade element
                    self.player1.active_element_infusion = self.player1.active_element
                    
                    # Drain the meter tank back to zero
                    self.player1.overclock_meter = 0.0
                    print("⚡ CHIMÆRA OVERCLOCK ACTIVE: ZERO STARTUP FRAMES ENGAGED.")
        else:
            self.overclock_button_neutral = True

    def handle_events(self):
        """Processes continuous hardware inputs on every single frame loop tick."""
        # 🎮 READ HARDWARE STICK DATA
        # (Using standard Pygame joystick index mapping for stick coordinates and clicks)
        try:
            if pygame.joystick.get_count() > 0:
                joystick = pygame.joystick.Joystick(0)
                if not joystick.get_init():
                    joystick.init()
                    
                axis_x = joystick.get_axis(2)       # Right Stick Horizontal axis
                axis_y = joystick.get_axis(3)       # Right Stick Vertical axis
                l3_click = joystick.get_button(9)   # Left Stick Click Button
                r3_click = joystick.get_button(10)  # Right Stick Click Button
                
                # Pass hardware updates down to your stick rule filters
                self.process_right_stick_flicks(axis_x, axis_y)
                self.check_overclock_activation(l3_click, r3_click)
        except pygame.error:
            # If no physical controller is plugged into a system, default safe bypass
            pass
