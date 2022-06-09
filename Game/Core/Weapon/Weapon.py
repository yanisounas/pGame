from Game.Core.Settings.Settings import Settings


class Weapon:
    def __init__(self, weapon_id: int):
        self._settings = Settings("./Game/Core/Settings/Data/", weapons="__weapons.json")['weapons']
        self._weapon = self._settings[str(weapon_id)]

    def __getattr__(self, item):
        return self._weapon[item] if item in self._weapon else None

    def __getitem__(self, item):
        return self._weapon[item] if item in self._weapon else None
