from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTertiaryText


from datetime import datetime, timedelta
from calendar import day_name
from shedule.shedule import schedule_dict


# Window.size = (360, 640)


class ScheduleApp(MDApp):
    def __init__(self):
        self.date = datetime.now()
        self.day = self.date.strftime('%A').upper()
        super(ScheduleApp, self).__init__()

    def build(self):
        self.root.ids.month_lbl.text = self.day
        self.root.ids.left_button.on_release = self.left_arrow_btn
        self.root.ids.right_button.on_release = self.right_arrow_btn
        self.update_list()
        return super(ScheduleApp, self).build()

    def left_arrow_btn(self):
        self.date -= timedelta(days=1)
        self.day = self.date.strftime('%A').upper()
        self.root.ids.month_lbl.text = self.day
        self.update_list()

    def right_arrow_btn(self):
        self.date += timedelta(days=1)
        self.day = self.date.strftime('%A').upper()
        self.root.ids.month_lbl.text = self.day
        self.update_list()

    def update_list(self):
        self.root.ids.schedule_list.clear_widgets()
        schedule = schedule_dict.get(self.day.lower())
        if schedule:
            ind = self.date.isocalendar()[1] % 2
            list_items = []
            for key, value in schedule.items():
                object = value['object'][ind]
                name_teacher = value['name_teacher'][ind]
                room = value['room'][ind]
                list_items.append(MDListItem(MDListItemHeadlineText(text=object),
                                             MDListItemSupportingText(text=name_teacher),
                                             MDListItemTertiaryText(text=room)))
            for item in list_items:
                self.root.ids.schedule_list.add_widget(item)




if __name__ == '__main__':
    app = ScheduleApp()
    app.run()
