
class Death:

    def death(self, entity_list, cycle=None):
        dead_entity_list = [ent for ent in entity_list if hasattr(ent, "health") and ent.health.life <= 0]
        for entity in dead_entity_list:
            print(f'{cycle} | <RIP> ---- Cell {entity.id} has died at the age of {entity.health.age} ---- <RIP>')
            entity.kill()
