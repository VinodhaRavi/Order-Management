class DBPropertyUtil:

    @staticmethod
    def load_properties(filepath):
        props = {}
        try:
            with open(filepath, "r") as file:
                for line in file:
                    if line.strip() == "" or line.strip().startswith("#"):
                        continue
                    key_value = line.strip().split("=", 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        props[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Properties file not found: {filepath}")
        except Exception as e:
            print(f"Error reading properties file: {e}")
        return props
