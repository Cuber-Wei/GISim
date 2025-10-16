from models.constants import (
    ARTIFACT_PIECE_POSITION,
    ELEMENTAL_ANTI_INIT_DICT,
    ELEMENTAL_BONUS_INIT_DICT,
)


class BaseCharacter:
    """基础角色类"""

    def __init__(
        self,
        name: str,  # 角色名称
        element_type: str,  # 元素类型
        weapon_type: str,  # 武器类型
        base_health: float,  # 基础生命值
        base_attack: float,  # 基础攻击力
        base_defence: float,  # 基础防御力
        energy_recharge: float = 100,  # 元素充能效率
        elemental_mastery: int = 0,  # 元素精通
        critical_rate: float = 5,  # 暴击率
        critical_damage: float = 50,  # 暴击伤害
        element_damage_bunus: dict[
            str, float
        ] = ELEMENTAL_BONUS_INIT_DICT,  # 元素伤害加成
        healing_bonus: float = 0,  # 治疗加成
        incoming_healing_bonus: float = 0,  # 受治疗加成
        cd_reduction: float = 0,  # 冷却缩减
        shield_strength: float = 0,  # 护盾强效
        damage_bunus_list: dict = {},  # 增伤乘区列表
        element_anti_list: dict = ELEMENTAL_ANTI_INIT_DICT,  # 元素抗性
    ) -> None:
        self.name = name
        self.element_type = element_type
        self.weapon_type = weapon_type
        self.weapon = None
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.health = base_health
        self.attack = base_attack
        self.defence = base_defence
        self.energy_recharge = energy_recharge
        self.elemental_mastery = elemental_mastery
        self.critical_rate = critical_rate
        self.critical_damage = critical_damage
        self.element_damage_bunus = element_damage_bunus
        self.healing_bonus = healing_bonus
        self.incoming_healing_bonus = incoming_healing_bonus
        self.cd_reduction = cd_reduction
        self.shield_strength = shield_strength
        self.damage_bunus_list = damage_bunus_list
        self.element_anti_list = element_anti_list

    def skill1_effect(self):
        """普攻效果"""
        print("普攻效果")
        return None

    def skill2_effect(self):
        """元素战技效果"""
        print("元素战技效果生效")
        return None

    def skill3_effect(self):
        """元素爆发效果"""
        print("元素爆发效果生效")
        return None

    def fixed_skill1_effect(self):
        """固有技能1效果"""
        print("固有技能1效果生效")
        return None

    def fixed_skill2_effect(self):
        """固有技能2效果"""
        print("固有技能2效果生效")
        return None

    def equip_weapon(self, weapon: "BaseWeapon"):
        """装备武器"""
        if weapon.weapon_type != self.weapon_type:
            raise ValueError(
                f"Cannot equip weapon of type {weapon.weapon_type} to character with weapon type {self.weapon_type}"
            )
        self.weapon = weapon
        weapon.main_effect(self)
        weapon.sub_effect(self, weapon.refinement_level)

    def equip_artifacts(self, artifact_list: list["BaseArtifact"]):
        artifact_set_count: dict[type[BaseArtifact], int] = {}
        for artifact in artifact_list:
            # 记录圣遗物套装及其数量
            artifact_set_count[type(artifact)] = (
                artifact_set_count.get(type(artifact), 0) + 1
            )
            # 圣遗物属性加成
            self.health += artifact.health
            self.attack += artifact.attack
            self.defence += artifact.defence
            self.health += self.base_health * artifact.health_percentage / 100
            self.attack += self.base_attack * artifact.attack_percentage / 100
            self.defence += self.base_defence * artifact.defence_percentage / 100
            self.energy_recharge += artifact.energy_recharge
            self.elemental_mastery += artifact.elemental_mastery
            self.critical_rate += artifact.critical_rate
            self.critical_damage += artifact.critical_damage
            if (
                artifact.element_damage_bunus[1] > 0
                and artifact.element_damage_bunus[0]
            ):
                self.element_damage_bunus[artifact.element_damage_bunus[0]] += (
                    artifact.element_damage_bunus[1]
                )
            self.healing_bonus += artifact.healing_bonus
        # 圣遗物套装特效生效
        for artifact, count in artifact_set_count.items():
            if count >= 2:
                artifact.two_piece(self)
            if count >= 4:
                artifact.four_piece(self)

    def get_into_team(self, team: "Team"):
        return None

    def __repr__(self) -> str:
        return f"""{"=" * 60}
{self.name} @ {self.element_type} @ {self.weapon_type} 角色面板 (当前武器：{self.weapon})

生命值 {self.health:.1f}
攻击力 {self.attack:.1f}
防御力 {self.defence:.1f}
暴击率 {self.critical_rate:.1f}%
暴击伤害 {self.critical_damage:.1f}%
元素充能效率 {self.energy_recharge:.1f}%
元素精通 {self.elemental_mastery:.1f}
元素伤害加成 {[f"{elem} : {bunus}%" for elem, bunus in self.element_damage_bunus.items()]}
增伤乘区列表 {[f"{item} : {bunus}%" for item, bunus in self.damage_bunus_list.items()]}

治疗加成 {self.healing_bonus:.1f}%
受治疗加成 {self.incoming_healing_bonus:.1f}%
冷却缩减 {self.cd_reduction:.1f}%
护盾强效 {self.shield_strength:.1f}%
元素伤害抗性 {[f"{elem} : {anti}%" for elem, anti in self.element_anti_list.items()]}
{"=" * 60}
"""


class BaseWeapon:
    """基础武器类"""

    def __init__(
        self,
        name: str,  # 武器名称
        weapon_type: str,  # 武器类型
        base_attack: float,  # 基础攻击力
        refinement_level: int = 1,  # 精炼等级
    ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.base_attack = base_attack
        self.refinement_level = refinement_level

    def main_effect(self, character: BaseCharacter):
        """主效果"""
        print("主效果生效")
        return None

    def sub_effect(self, character: BaseCharacter, refinement_level: int):
        """副效果"""
        print("副效果生效")
        return None

    def __str__(self) -> str:
        return self.name


class BaseArtifact:
    """基础圣遗物类"""

    def __init__(
        self,
        set_name: str,  # 套装名称
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
        self.set_name = set_name
        self.position = position
        if position not in ARTIFACT_PIECE_POSITION.values():
            raise ValueError(f"Invalid artifact position: {position}")
        self.health = health
        self.attack = attack
        self.defence = defence
        self.health_percentage = health_percentage
        self.attack_percentage = attack_percentage
        self.defence_percentage = defence_percentage
        self.energy_recharge = energy_recharge
        self.elemental_mastery = elemental_mastery
        self.critical_rate = critical_rate
        self.critical_damage = critical_damage
        self.element_damage_bunus = element_damage_bunus
        self.healing_bonus = healing_bonus

    @staticmethod
    def two_piece(character: BaseCharacter):
        """两件套效果"""
        print("两件套效果生效")
        return None

    @staticmethod
    def four_piece(character: BaseCharacter):
        """四件套效果"""
        print("四件套效果生效")
        return None


class Enemy:
    """敌人类"""

    def __init__(
        self,
        level: int,  # 敌人等级
        base_health: float,  # 基础生命值
        base_defence: float,  # 基础防御力
        elemental_resistance: dict[str, float] = ELEMENTAL_BONUS_INIT_DICT,  # 元素抗性
    ) -> None:
        self.level = level
        self.base_health = base_health
        self.health = base_health
        self.base_defence = base_defence
        self.defence = base_defence
        self.elemental_resistance = elemental_resistance

    def __repr__(self) -> str:
        return f"""敌人面板"""


class Team:
    """队伍类"""

    def __init__(
        self,
    ) -> None:
        self.members: list[BaseCharacter] = []

    def add_member(self, member: BaseCharacter):
        if len(self.members) >= 4:
            raise ValueError("队伍成员不能超过4个")
        self.members.append(member)
        member.get_into_team(self)

    def remove_member(self, member: BaseCharacter):
        self.members.remove(member)

    def get_member_number(self) -> int:
        return len(self.members)

    def __repr__(self) -> str:
        return f"""队伍成员: {[f"{member.name} @ {member.element_type}" for member in self.members]}"""

    def __iter__(self):
        return iter(self.members)

    def __getitem__(self, index: int | str) -> BaseCharacter:
        if isinstance(index, str):
            for member in self.members:
                if member.name == index:
                    return member
            raise ValueError(f"队伍中没有名为 {index} 的角色")
        else:
            return self.members[index]
