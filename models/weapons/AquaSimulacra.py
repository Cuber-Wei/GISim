from models.base_class import BaseCharacter, BaseWeapon
from models.constants import WEAPON_TYPES


class AquaSimulacra(BaseWeapon):
    """若水"""

    def __init__(self, refinement_level: int) -> None:
        name = "若水"
        weapon_type = WEAPON_TYPES[1]
        base_attack = 542
        super().__init__(name, weapon_type, base_attack, refinement_level)

    def main_effect(self, character: BaseCharacter):
        # 主效果的具体实现
        character.critical_damage += 88.2

    def sub_effect(self, character: BaseCharacter, refinement_level: int):
        # 副效果的具体实现
        character.health += (
            character.base_health * [0.16, 0.20, 0.24, 0.28, 0.32][refinement_level - 1]
        )
        character.damage_bunus_list["base_bunus"] = (
            character.damage_bunus_list.get("base_bunus", 0)
            + [0.2, 0.25, 0.3, 0.35, 0.4][refinement_level - 1]
        )
