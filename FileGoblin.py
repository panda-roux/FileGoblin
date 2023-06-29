import configparser


class FileGoblin:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.current_level = 0.0

        self.level = 1
        self.xp = 0

    def earn_xp(self, milestone):
        amount = int(self.config['rewards'][milestone])
        self.xp += amount
        print(f"File Goblin earned {amount} XP for {milestone}!")

        # Check if File Goblin has enough XP to level up
        if self.xp >= self.level * int(self.config['rewards']['full_level']):  # Require 100 XP per level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0  # Reset XP to 0 after leveling up
        print(f"File Goblin leveled up! It's now level {self.level}.")

    def xp_for_next_level(current_level):
        return 100 * current_level ** 2
