import yaml
import random

class _MonsterFactory(object):
    _instance = None

    def __new__(klass):
        if(klass._instance == None): 
            klass._instance = super(_MonsterFactory, klass).__new__(klass)
            klass._instance._load_monsters()

        return klass._instance

    def random_monster(self):
        available_monsters = list(self._monsters["monsters"].values())
        return random.choice(available_monsters)

    def get_monster_by_name(self, monster_name):
        return self._monsters["monsters"].get(monster_name)

    # private methods

    def _load_monsters(self):
        with open("monster_data.yml", "r") as stream:
            try:
                self._monsters = yaml.safe_load(stream)
            except yaml.YAMLError as exception:
                print(exception)

MonsterFactory = _MonsterFactory()
