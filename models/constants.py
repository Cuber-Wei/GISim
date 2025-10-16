ELEMENT_TYPES = ["火", "水", "雷", "冰", "风", "岩", "草", "物"]
ARTIFACT_SET_NAME = {}
ARTIFACT_PIECE_POSITION = {
    1: "生之花",
    2: "死之羽",
    3: "时之沙",
    4: "空之杯",
    5: "理之冠",
}
ELEMENTAL_BONUS_INIT_DICT: dict[str, float] = {}.fromkeys(ELEMENT_TYPES, 0)
ELEMENTAL_ANTI_INIT_DICT: dict[str, float] = {}.fromkeys(ELEMENT_TYPES, 0)
WEAPON_TYPES = ["单手剑", "弓", "法器", "长柄武器", "双手剑"]
