import json


class Settings:
    def __init__(self, directory: str, **kwargs):
        self._directory = directory
        if not kwargs:
            raise Exception("Missing JSON files")

        self._files = {}
        self._settings = {"Test": "ok"}
        for k, v in kwargs.items():
            self._files[k] = f"{self._directory}{v}"
            self._settings[k] = self._load_json(self._files[k])
            self.__setattr__(k, self._settings[k])

    def __getitem__(self, item):
        return self._settings[item] if item in self._settings else None

    def push_changes(self, *args: str) -> None:
        for arg in args:
            if type(arg) != str:
                _type = str(type(arg)).split("'")[1]
                raise TypeError(f"Expected type 'str', got '{_type}' instead ")

            if arg not in self._files:
                raise KeyError(f"No settings for {arg}")

            with open(self._files[arg], 'w') as file:
                json.dump(self._settings[arg], file)

    @classmethod
    def _load_json(cls, path: str) -> dict:
        with open(path, "r") as file:
            return json.load(file)
