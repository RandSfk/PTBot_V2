import json
import random

class rand:
    def __init__(self, username):
        self.username = username
        self.database_file = "users.json"
        self.load_database()
        self.load_effect()
        self.items = [
            {"name": "Excalibur Sword", "type": "sword", "rank": "legendary", "effects": {"physical_attack": 30}},
            {"name": "Aegis Armor", "type": "armor", "rank": "legendary", "effects": {"health": 100}},
            {"name": "Staff of Wonders", "type": "staff", "rank": "legendary", "effects": {"magic_attack": 25}},
            {"name": "Legendary Robe", "type": "robe", "rank": "legendary", "effects": {"mana": 100}},
            {"name": "Fire Scroll", "type": "scroll", "rank": "legendary", "effects": {"magic_attack": 40}},
            {"name": "Silver Sword", "type": "sword", "rank": "mythical", "effects": {"physical_attack": 25}},
            {"name": "Golden Armor", "type": "armor", "rank": "mythical", "effects": {"health": 75}},
            {"name": "Magic Wand", "type": "wand", "rank": "mythical", "effects": {"magic_attack": 20}},
            {"name": "Mythical Robe", "type": "robe", "rank": "mythical", "effects": {"max_mana": 75}},
            {"name": "Ice Scroll", "type": "scroll", "rank": "mythical", "effects": {"magic_attack": 35}},
            {"name": "Iron Sword", "type": "sword", "rank": "rare", "effects": {"physical_attack": 20}},
            {"name": "Leather Armor", "type": "armor", "rank": "rare", "effects": {"health": 50}},
            {"name": "Wooden Staff", "type": "staff", "rank": "rare", "effects": {"magic_attack": 15}},
            {"name": "Rare Robe", "type": "robe", "rank": "rare", "effects": {"mana": 50}},
            {"name": "Thunder Scroll", "type": "scroll", "rank": "rare", "effects": {"magic_attack": 30}},
            {"name": "Wooden Sword", "type": "sword", "rank": "common", "effects": {"physical_attack": 15}},
            {"name": "Cloth Armor", "type": "armor", "rank": "common", "effects": {"health": 30}},
            {"name": "Basic Staff", "type": "staff", "rank": "common", "effects": {"magic_attack": 10}},
            {"name": "Common Robe", "type": "robe", "rank": "common", "effects": {"mana": 30}},
            {"name": "Basic Scroll", "type": "scroll", "rank": "common", "effects": {"magic_attack": 20}},
            {"name": "Broken Sword", "type": "sword", "rank": "trash", "effects": {"physical_attack": 10}},
            {"name": "Rusty Armor", "type": "armor", "rank": "trash", "effects": {"health": 20}},
            {"name": "Torn Staff", "type": "staff", "rank": "trash", "effects": {"magic_attack": 5}},
            {"name": "Torn Robe", "type": "robe", "rank": "trash", "effects": {"mana": 20}},
            {"name": "Useless Scroll", "type": "scroll", "rank": "trash", "effects": {"magic_attack": 10}}
        ]
    def load_effect(self):
        rpg_data = self.get_rpg_data()
        equipped_items = rpg_data.get('equip', [])
        try:
            for item_name in equipped_items:
                for item in rpg_data['inventory'].get('items', []):
                    if item['name'] == item_name:
                        if item['rank'] == 'legendary':
                            duration = 10
                        elif item['rank'] == 'mythical':
                            duration = 8  # Durasi dalam jumlah ronde atau sesuai kebutuhan
                        elif item['rank'] == 'rare':
                            duration = 5  # Durasi dalam jumlah ronde atau sesuai kebutuhan
                        elif item['rank'] == 'common':
                            duration = 3  # Durasi dalam jumlah ronde atau sesuai kebutuhan
                        elif item['rank'] == 'trash':
                            duration = 1  # Durasi dalam jumlah ronde atau sesuai kebutuhan
                        else:
                            duration = 5

                        for effect_type, effect_value in item.get('effects', {}).items():
                            if effect_type == 'mana':
                                rpg_data['mana'] += effect_value * duration
                            elif effect_type == 'health':
                                rpg_data['health'] += effect_value * duration
                            elif effect_type == 'physical_attack':
                                rpg_data['physical_attack'] += effect_value * duration
                            elif effect_type == 'magic_attack':
                                rpg_data['magic_attack'] += effect_value * duration
                            elif effect_type == 'max_mana':
                                rpg_data['max_mana'] += effect_value * duration

            self.save_rpg_data(rpg_data)
        except TypeError:
            pass
        except KeyError:
            pass
    def load_database(self):
        try:
            with open(self.database_file, 'r') as file:
                self.database = json.load(file)
        except FileNotFoundError:
            self.database = {"account": []}
            self.save_database()

    def save_database(self):
        with open(self.database_file, 'w') as file:
            json.dump(self.database, file, indent=4)

    def find_account(self):
        accounts = self.database['account']
        for account in accounts:
            if account['username'] == self.username:
                return account
        return None

    def get_rpg_data(self):
        account = self.find_account()
        if account:
            return account.get('rpg', {})
        return {}

    def save_rpg_data(self, data):
        for account in self.database['account']:
            if account['username'] == self.username:
                account['rpg'] = data
                self.save_database()
                return True
        return False

    def reset(self):
        self.save_rpg_data({'max_health':200, 'max_mana':100, 'health': 200, 'mana': 150, 'exp': 0, 'gold': 20, 'level': 1, 'inventory': {"items":[] }, 'equip': None, 'physical_attack':12, 'magic_attack':12})

    def new_user(self, classs='warrior'):
        if classs == 'warrior':
            self.save_rpg_data({'class':classs,'max_health':200, 'max_mana':100, 'health': 200, 'mana': 150, 'exp': 0, 'gold': 20, 'level': 1, 'inventory': {"items":[] }, 'equip': None, 'physical_attack':12, 'magic_attack':8})
        elif classs == "mage":
            self.save_rpg_data({'class':classs,'max_health':200, 'max_mana':100, 'health': 200, 'mana': 150, 'exp': 0, 'gold': 20, 'level': 1, 'inventory': {"items":[] }, 'equip': None, 'physical_attack':8, 'magic_attack':12})
        return True

    def levelup(self):
        rpg_data = self.get_rpg_data()
        current_level = rpg_data.get('level', 1)
        level_asal = current_level
        exp = rpg_data.get('exp', 0)
        max_health = rpg_data.get('max_health', 100)
        max_mana = rpg_data.get('max_mana', 100)
        health_asal = max_health
        mana_asal = max_mana
        _levelup_ = current_level * 100
        if exp > _levelup_:
            current_level += 1
            max_health += 40 * (5 % current_level)
            max_mana += 20 * (5 % current_level)
            rpg_data['level'] = current_level
            rpg_data['max_health'] = max_health
            rpg_data['max_mana'] = max_mana
            rpg_data['health'] = max_health
            rpg_data['mana'] = max_mana
            rpg_data['exp'] -= _levelup_
            self.save_rpg_data(rpg_data)
            return f'Player {self.username} levelup ({level_asal} => {current_level})\nHealth: ({health_asal} => {max_health}) \n Mana: ({mana_asal} => {max_mana})'

    def status(self):
        try:
            rpg_data = self.get_rpg_data()
            if not rpg_data:
                return f"Data RPG tidak ditemukan atau inventory kosong untuk pengguna {self.username}."

            health = rpg_data.get('health', 'belum ada')
            mana = rpg_data.get('mana', 'belum ada')
            gold = rpg_data.get('gold', 'belum ada')
            level = rpg_data.get('level', 'belum ada')
            inventory = ''.join([f"{item['name']}({item['rank']}) => {''.join([f'{key} +{value}' for key, value in item['effects'].items()])}\n" for item in rpg_data['inventory'].get('items', [])])
            equip = rpg_data.get('equip', 'belum ada')
            exp = rpg_data.get('exp', 'belum ada')
            return f"Petualang {self.username} Status:\nLevel: {level}\nHealth: {health}\nMana: {mana}\nGold: {gold}\nExp: {exp}\nEquip: {equip}\nInventory: \n{inventory}\n"
        except Exception as e:
            return f"Error: {str(e)}"

    def gacha(self):
        item = random.choice(self.items)
        return f"Anda mendapatkan {item['name']} ({item['type']}, {item['rank']})."

    def open_loot_crates(self, count=1):
        results = []
        for _ in range(count):
            results.append(self.gacha())
        return "\n".join(results)

    def adventure_beta(self):
        rpg_data = self.get_rpg_data()
        current_level = rpg_data.get('level', 1)
        current_health = rpg_data.get('health', 100)
        character_class = rpg_data.get('class', 'warrior')

        dungeons = {
            "1-10": [
                "Goblin Caves", "Spider Nest", "Bandit Hideout", "Haunted Mine",
                "Forgotten Ruins", "Shadowed Crypt", "Rusty Catacombs", "Murky Tunnels",
                "Whispering Halls", "Ancient Cellar"
            ],
            "11-20": [
                "Orc Stronghold", "Cursed Catacombs", "Darkwood Forest", "Sorcerer's Tower",
                "Dragon's Lair", "Frozen Crypt", "Sacred Tombs", "Abyssal Keep",
                "Enchanted Ruins", "Labyrinthine Caves"
            ],
            "21-30": [
                "Titan's Forge", "Eternal Abyss", "Celestial Sanctuary", "Primordial Vault",
                "Chaos Citadel", "Infernal Pit", "Arcane Nexus", "Twilight Stronghold",
                "Void Depths", "Mythic Catacombs"
            ],
            "31+": [
                "Astral Sanctum", "Demonic Citadel", "Elemental Nexus", "Eldritch Labyrinth",
                "Abyssal Spire", "Ethereal Bastion", "Phoenix Crypt", "Celestial Crucible",
                "Shadowed Abyss", "Elders' Vault", "Heavenly Citadel"
            ]
        }

        enemies = {
            "1-10": [
                "Goblin Warrior", "Giant Spider", "Bandit Archer", "Ghost Miner",
                "Skeleton Guard", "Crypt Bat", "Rusty Golem", "Murk Dweller",
                "Whispering Specter", "Ancient Lich"
            ],
            "11-20": [
                "Orc Warlord", "Cursed Specter", "Darkwood Druid", "Sorcerer's Apprentice",
                "Dragonkin Sentinel", "Frozen Spirit", "Sacred Guardian", "Abyssal Warden",
                "Enchanted Sentinel", "Labyrinth Minotaur"
            ],
            "21-30": [
                "Titan's Colossus", "Eternal Wraith", "Celestial Guardian", "Primordial Behemoth",
                "Chaos Demon", "Infernal Dragon", "Arcane Watcher", "Twilight Shadow",
                "Void Elemental", "Mythic Hydra"
            ],
            "31+": [
                "Astral Overlord", "Demonic Warlord", "Elemental Avatar", "Eldritch Horror",
                "Abyssal Leviathan", "Ethereal Seraph", "Phoenix Elemental", "Celestial Arbiter",
                "Shadowed Reaper", "Elder Titan"
            ]
        }

        if current_level <= 10:
            dungeon = random.choice(dungeons["1-10"])
            enemy = random.choice(enemies["1-10"])
            probabilities = [0.7, 9, 0.1]
        elif current_level <= 20:
            dungeon = random.choice(dungeons["11-20"])
            enemy = random.choice(enemies["11-20"])
            probabilities = [0.6, 0.3, 0.1]
        elif current_level <= 30:
            dungeon = random.choice(dungeons["21-30"])
            enemy = random.choice(enemies["21-30"])
            probabilities = [0.5, 0.4, 0.1]
        else:
            dungeon = random.choice(dungeons["31+"])
            enemy = random.choice(enemies["31+"])
            probabilities = [0.4, 0.5, 0.1]

        if current_health < 20:
            event = 'dead'

        appear = ['fight', 'found', 'none']
        event = random.choices(appear, probabilities)[0]

        if event == 'fight':
            return f"{self.username} pergi ke {dungeon}\nterlibat pertarungan dengan {enemy}"
        elif event == 'found':
            item_rarity_weights = {
                'common': 5, 
                'rare': 3 if current_level >10 else 0,
                'mythical': 2 if current_level > 30 else 0, 
                'legendary': 1 if current_level > 30 else 0, 
                'trash': 4
            }
            item_rarity = random.choices(list(item_rarity_weights.keys()), weights=list(item_rarity_weights.values()))[0]

            items_by_class = {
                'warrior': ['sword', 'armor'],
                'mage': ['robe', 'staff', 'scroll'],
            }
            
            available_items = []
            if character_class in items_by_class:
                available_items = [item for item in self.items if item['rank'] == item_rarity and item['type'] in items_by_class[character_class]]
            else:
                available_items = [item for item in self.items if item['rank'] == item_rarity]

            if available_items:
                found_item = random.choice(available_items)
                effects = ', '.join([f"{key} +{value}" for key, value in found_item['effects'].items()])
                inventory_items = rpg_data['inventory']['items']
                item_found = False
                for inventory_item in inventory_items:
                    if inventory_item['name'] == found_item['name']:
                        inventory_item['count'] += 1
                        item_found = True
                        break

                if not item_found:
                    found_item['count'] = 1
                    inventory_items.append(found_item)

                rpg_data['inventory']['items'] = inventory_items
                self.save_rpg_data(rpg_data)

                return f"{self.username} menemukan item: {found_item['name']} ({found_item['rank']}) dengan efek {effects}"
            else:
                return f"{self.username} tidak menemukan item yang cocok di {dungeon}."
        else:
            return f"Tidak ada yang terjadi di {dungeon}."
        
    def use_item(self, item_name):
        rpg_data = self.get_rpg_data()
        items = rpg_data['inventory'].get('items', [])

        for item in items:
            if item['name'] == item_name:
                if item['count'] > 0:
                    item['count'] -= 1
                    if item['count'] == 0:
                        items.remove(item)
                    
                    # Tambahkan nama item yang digunakan ke dalam equip
                    equipped_items = rpg_data.get('equip', [])
                    equipped_items.append(item['name'])
                    rpg_data['equip'] = equipped_items

                    self.save_rpg_data(rpg_data)
                    return True
                else:
                    return False
        return False

    def remove_item(self, item_name):
        rpg_data = self.get_rpg_data()
        items = rpg_data['inventory'].get('items', [])

        for item in items:
            if item['name'] == item_name:
                items.remove(item)
                self.save_rpg_data(rpg_data)
                return True
        
        return False
