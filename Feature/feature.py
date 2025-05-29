class Feature:
    def __init__(self, name, enabled=False):
        self.name = name
        self.enabled = enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def __str__(self):
        status = "enabled" if self.enabled else "disabled"
        return f"Feature '{self.name}' is {status}."


if __name__ == "__main__":
    feature = Feature("BasicFeature")
    print(feature)
    feature.enable()
    print(feature)