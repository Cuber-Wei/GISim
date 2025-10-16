from models.artifacts.heart_depth import HeartOfDepth
from models.artifacts.nymph_dream import NymphDream
from models.base_class import Team
from models.characters.yelan import YeLan
from models.constants import ELEMENT_TYPES
from models.weapons.AquaSimulacra import AquaSimulacra

if __name__ == "__main__":
    yelan = YeLan()
    aqua = AquaSimulacra(refinement_level=1)
    yelan.equip_weapon(aqua)
    artifacts = []
    artifacts.append(NymphDream(position="时之沙", attack_percentage=18.0))
    artifacts.append(
        NymphDream(position="空之杯", element_damage_bunus=(ELEMENT_TYPES[1], 46.6))
    )
    artifacts.append(NymphDream(position="理之冠", critical_rate=31.1))
    artifacts.append(HeartOfDepth(position="生之花", health=4780))
    artifacts.append(HeartOfDepth(position="死之羽", attack=311))
    yelan.equip_artifacts(artifacts)
    team = Team()
    team.add_member(yelan)
    print(team)
    print(team["夜兰"])
