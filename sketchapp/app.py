from android import PythonActivity  # provided by briefcase Android template

from android.view import LinearLayout, TextView  # classes from Android Java API


class SketchApp:
    def __init__(self):
        self._activity = PythonActivity.setListener(self)

    def onCreate(self):
        label = TextView(self._activity)
        label.setText('Hello Android World from Python!')

        vlayout = LinearLayout(self._activity)
        vlayout.addView(label)

        self._activity.setContentView(vlayout)


def main():
    return SketchApp()
