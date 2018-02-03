import joblib
import os
class Saver:
    def save(self, obj, path, file_name):
        full_path = os.path.join(path, file_name)
        joblib.dump(obj, full_path)

    def load(self, path, file_name):
        full_path = os.path.join(path, file_name)
        return joblib.load(full_path)
