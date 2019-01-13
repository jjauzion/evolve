class Death:

    def death(self, entity_list):
        dead_entity_list = [ent for _, ent in entity_list.items()
                            if "health" in ent.component and ent.component["health"].life <= 0]
        for entity in dead_entity_list:
            print("<RIP> ---- Cell {} has died at the age of {} ---- <RIP>".format(entity.id, entity.component["health"].age))
            entity_list.pop(entity.id)
