
class Death:

    def death(self, entity_list):
        dead_entity_list = [ent for ent in entity_list
                            if "health" in ent.component and ent.component["health"].life <= 0]
        for entity in dead_entity_list:
            print("<RIP> ---- Cell {} has died at the age of {} ---- <RIP>".format(entity.id, entity.component["health"].age))
            entity.kill()
