import pygame

class lunarlandergame():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Lunar Lander")
        self.lander = LunarLander()
        self.surface = LunarSurface()
        self.ui = GameUI(self.screen, self.lander, self.surface)
        self.player_controller = PlayerController(self.lander)
        self.ai_controller = AIController(self.lander)
        # self.score_manager = ScoreManager()
        self.is_running = True

    def start_game(self):
        # Main game loop
        while self.is_running:
            self.handle_events()
            self.update_game_state()
            self.render()
            pygame.time.delay(30)  # Control frame rate

    def handle_events(self):
        # Handle player input and other events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            self.player_controller.handle_event(event)
    
    def update_game_state(self):
        # Update lander and check for collisions
        self.lander.update()
        if self.surface.check_collision(self.lander):
            self.is_running = False
            self.ui.display_game_over(self.lander)
    
    def render(self):
        # Render the game UI
        self.ui.render()

# Class to represent the lunar lander
class LunarLander:
    def __init__(self):
        self.position: list[float] = [390.0, 0.0]  # Center the lander horizontally at the top
        self.velocity: list[float] = [0.0, 0.0]
        self.fuel = 100
        self.thrusting = False

    def apply_gravity(self):
        # Simulate gravity affecting the lander
        self.velocity[1] += 0.1  # Simple gravity effect
    
    def apply_thrust(self):
        # Apply thrust to counteract gravity
        self.velocity[1] -= 0.5
        self.fuel -= 0.6

    def update(self):
        # Update the position and velocity based on thrust and gravity
        self.apply_gravity()
        if self.thrusting and self.fuel > 0:
            self.apply_thrust()
        self.position[1] += self.velocity[1]

# Class to represent the Lunar surface
class LunarSurface:
    def __init__(self):
        self.height = 50  # Height of the the terrain
    
    def check_collision(self, lander):
        # Check for collision with the lunar surface
        lander_bottom = lander.position[1] + 20
        if lander_bottom >= 600 - self.height:
            return True
        return False

# Class to manage the graphical user interface
class GameUI:
    def __init__(self, screen, lander, surface):
        self.screen = screen
        self.lander = lander
        self.surface = surface
        self.font = pygame.font.Font(None, 30)

    def render(self):
        # Render the lander, surface, and status information
        self.screen.fill((0, 0, 0))  # Fill screen with black

        # Draw the lunar lander as white square
        pygame.draw.rect(self.screen, (255, 255, 255), 
                         (self.lander.position[0], self.lander.position[1], 20, 20))
        
        # Draw the terrain as a green rectangle
        pygame.draw.rect(self.screen, (0, 255, 0), 
                         (0, 600 - self.surface.height, 800, self.surface.height))
        
        # Draw the HUD
        self.render_hud()

        pygame.display.flip()  # Update the screen

    def render_hud(self):
         # Render the HUD with altitude, velocity, and fuel level
         altitude = 600 - self.surface.height - (self.lander.position[1] + 20)
         velocity = self.lander.velocity[1]
         fuel = self.lander.fuel

         altitude_text = self.font.render(f"Altitude: {altitude:.2f}", True, (255, 255, 255))
         self.screen.blit(altitude_text, (10, 10))
         velocity_text = self.font.render(f"Velocity: {velocity:.2f}", True, (255, 255, 255))
         self.screen.blit(velocity_text, (10, 40))
         fuel_text = self.font.render(f"Fuel: {fuel:.2f}", True, (255, 255, 255))
         self.screen.blit(fuel_text, (10, 70))

    def display_game_over(self, lander):
        # Display the game over screen
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(text, (200, 250))
        pygame.display.flip()
        pygame.time.delay(2000)  # Display for 2 seconds

# Class to handle player input
class PlayerController:
    def __init__(self, lander):
        self.lander = lander
    
    def handle_event(self, event):
        # Handle player input events to control the lander
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.lander.thrusting = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.lander.thrusting = False

class AIController:
    def __init__(self, lander):
        self.lander = lander
    
    def conttrol_lander(self):
        # AI logic to control the lander
        pass

# Class to manage scoring anda feedback
class ScoreManager:
    def __init__(self):
        self.score = 0
    
    def calculate_score(self, landedr):
        # Calculate score based on landing success, fuel efficiency, and time taken
        pass

    def display_score(self):
        # Dispaly the score to the player
        pass
        


# Initializing and the starting the game
if __name__ == "__main__":
    game = lunarlandergame()
    game.start_game()
    pygame.quit()
