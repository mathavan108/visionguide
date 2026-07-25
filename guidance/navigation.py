class NavigationGuide:

    def __init__(self):

        self.previous_scene = ""

    def parse(self, response):

        scene = ""
        navigation = ""
        warning = ""

        section = None

        for line in response.splitlines():

            line = line.strip()

            if line.startswith("Scene:"):
                section = "scene"
                scene += line.replace("Scene:", "").strip()

            elif line.startswith("Navigation:"):
                section = "navigation"
                navigation += line.replace("Navigation:", "").strip()

            elif line.startswith("Warning:"):
                section = "warning"
                warning += line.replace("Warning:", "").strip()

            else:

                if section == "scene":
                    scene += " " + line

                elif section == "navigation":
                    navigation += " " + line

                elif section == "warning":
                    warning += " " + line

        return {
            "scene": scene.strip(),
            "navigation": navigation.strip(),
            "warning": warning.strip()
        }

    def should_speak(self, current):

        scene = current.get("scene", "").strip()

        if scene == "":
            return False

        if scene == self.previous_scene:
            return False

        self.previous_scene = scene

        return True

    def format_for_speech(self, current):

        speech = ""

        scene = current.get("scene", "")
        navigation = current.get("navigation", "")
        warning = current.get("warning", "")

        if scene:
            speech += scene

        if navigation:
            speech += ". " + navigation

        if warning and warning.lower() != "none":
            speech += ". Warning. " + warning

        return speech