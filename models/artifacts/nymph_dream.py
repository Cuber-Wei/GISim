from models.base_class import BaseArtifact, BaseCharacter
from models.constants import ELEMENT_TYPES


class NymphDream(BaseArtifact):
    """涅墨西斯之梦"""

    def __init__(
        self,
        position: str,  # 部位
        health: float = 0,  # 生命值
        attack: float = 0,  # 攻击力
        defence: float = 0,  # 防御力
        health_percentage: float = 0,  # 生命值百分比
        attack_percentage: float = 0,  # 攻击力百分比
        defence_percentage: float = 0,  # 防御力百分比
        energy_recharge: float = 0,  # 元素充能效率
        elemental_mastery: int = 0,  # 元素精通
        critical_rate: float = 0,  # 暴击率
        critical_damage: float = 0,  # 暴击伤害
        element_damage_bunus: tuple[str, float] = ("", 0),  # 元素伤害加成
        healing_bonus: float = 0,  # 治疗加成
    ) -> None:
        self.set_name = "涅墨西斯之梦"
        super().__init__(
            self.set_name,
            position,
            health,
            attack,
            defence,
            health_percentage,
            attack_percentage,
            defence_percentage,
            energy_recharge,
            elemental_mastery,
            critical_rate,
            critical_damage,
            element_damage_bunus,
            healing_bonus,
        )

    @staticmethod
    def two_piece(character: BaseCharacter):
        """两件套效果: 提供15%水元素伤害加成"""
        character.element_damage_bunus[ELEMENT_TYPES[1]] += 15.0

    @staticmethod
    def four_piece(character: BaseCharacter):
        """四件套效果: 触发元素战技后，提升30%普通攻击和重击伤害，持续15秒"""
        character.damage_bunus_list["normal_and_charged"] = (
            character.damage_bunus_list.get("normal_and_charged", 0) + 30.0
        )
