from models import log_level
from models.base_class import BaseCharacter, Team
from models.constants import ELEMENT_TYPES, WEAPON_TYPES


class YeLan(BaseCharacter):
    """夜兰"""

    def __init__(self) -> None:
        name = "夜兰"
        element = ELEMENT_TYPES[1]
        weapon_type = WEAPON_TYPES[1]
        base_health = 14450
        base_attack = 244
        base_defence = 548
        critical_rate = 24.2
        super().__init__(
            name,
            element,
            weapon_type,
            base_health,
            base_attack,
            base_defence,
            critical_rate=critical_rate,
        )

    def skill1_effect(self) -> None:
        """普攻效果"""
        print("普攻效果")
        return None

    def skill2_effect(self) -> None:
        """元素战技效果"""
        print("元素战技效果生效")
        return None

    def skill3_effect(self) -> None:
        """元素爆发效果"""
        print("元素爆发效果生效")
        return None

    def fixed_skill1_effect(self, team: Team = Team()) -> None:
        """固有技能1效果"""
        if team.get_member_number() == 0:
            if log_level == "DEBUG":
                print("[WARNING] 当前队伍没有其他角色，仅计算单人入队效果。")
                team.add_member(self)
        party_element_types = set()
        for member in team:
            if member.element_type not in party_element_types:
                party_element_types.add(member.element_type)
        health_bunus = [0.06, 0.12, 0.18, 0.3][
            len(party_element_types) - 1
        ] * self.base_health
        self.health += health_bunus
        if log_level == "DEBUG":
            print(
                f"[DEBUG] 固有天赋效果生效，队伍存在 1/2/3/4 种元素类型的角色时，夜兰的生命值上限提升 6%/12%/18%/30% 。"
            )
            print(
                f"[DEBUG] 当前队伍存在 {len(party_element_types)} 种元素类型的角色，夜兰生命值提升 {health_bunus}。"
            )
        return None

    def fixed_skill2_effect(self) -> None:
        """固有技能2效果"""
        print("固有技能2效果生效")
        return None

    def get_into_team(self, team: Team) -> None:
        self.fixed_skill1_effect(team)
