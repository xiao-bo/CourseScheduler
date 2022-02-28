from libs.google.google_sheet_controller import GoogleSheetController as GSC
from libs.schedule.class_schedule import ClassSchedule
from libs.schedule.teacher_schedule import TeacherSchedule
from libs.schedule.schedule_builder import ScheduleBuilder

class Scheduler(object):

    def __init__(self):
        self.gsc = GSC()
        self.class_schedule = ClassSchedule()
        self.TeacherSchedule = TeacherSchedule()
        self.ScheduleBuilder = ScheduleBuilder()
    def runner(self):
        print('Scheduler runner')
        self.gsc.runner()        
        self.class_schedule.runner()
        self.TeacherSchedule.runner()
        self.ScheduleBuilder.runner()