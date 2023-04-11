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
                    if -1 <= data['level_info'] <= 13:
                        return data['level_info']
                except Exception as e:
                    raise e

    def restart(self):
        with open(self.filepath, 'r+') as f:
            data = json.load(f)
            if 'user_name' in data:
                del data['user_name']

        with open(self.filepath, 'w') as f:
            data['level_info'] = -1
            json.dump(data, f)

    def save_level_info(self, level_info):
        with open(self.filepath, 'r+') as f:
            data = json.load(f)

        with open(self.filepath, 'w') as f:
            data['level_info'] = level_info
            json.dump(data, f)

    def register_user(self, user_name):
        with open(self.filepath, 'r+') as f:
            data = json.load(f)
            data['user_name'] = user_name

        with open(self.filepath, 'w+') as f:
            json.dump(data, f)

    def check_user(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            if 'user_name' in data.keys():
                return True
            return False

    def get_user(self):
        if self.check_user():
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return data['user_name']
        return None


if __name__ == '__main__':
    a = SaveInfo()
    print(a.save_level_info(10))
    print(a.read_level_info())
