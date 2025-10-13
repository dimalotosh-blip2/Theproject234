class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"First, I'll finish your {self.work}. Then, I'll help you with {work}."

helper = Helper("project")
print(helper("shopping"))
