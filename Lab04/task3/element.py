class LightHTMLElement:
    def __init__(self, tag, text=""):
        self.tag = tag
        self.text = text
        self.event_listeners = {}

    def addEventListener(self, event_type, listener):
        if event_type not in self.event_listeners:
            self.event_listeners[event_type] = []
        self.event_listeners[event_type].append(listener)
        print(f"Додано слухача події '{event_type}' для <{self.tag}>.")

    def dispatchEvent(self, event_type, event_info=None):
        print(f"\nВиклик події '{event_type}' для <{self.tag}>:")
        if event_type in self.event_listeners:
            for listener in self.event_listeners[event_type]:
                listener(event_info)
        else:
            print(f"Для події '{event_type}' немає зареєстрованих слухачів.")

    def __str__(self):
        return f"<{self.tag}>{self.text}</{self.tag}>"
