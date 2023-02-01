import json


class SaveInfo:
    def __init__(self):
        self.filepath = 'resources/saveinfo/save.json'

    def read_level_info(self):
        with open(self.filepath, 'r+') as f:
            data = json.load(f)
            if not data:
                data['level_info'] = 1
                json.dump(data, f)
                return 1
            else:
                try:
                    if 1 <= data['level_info'] <= 10:
                        return data['level_info']
                except Exception as e:
                    raise e

    def save_level_info(self, level_info):
        with open(self.filepath, 'r+') as f:
            data = json.load(f)

        with open(self.filepath, 'w') as f:
            data['level_info'] = level_info
            json.dump(data, f)


if __name__ == '__main__':
    a = SaveInfo()
    print(a.save_level_info(10))
    print(a.read_level_info())
