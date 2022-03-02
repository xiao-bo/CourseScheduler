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
        self.build_class_schedule()


    def build_class_schedule(self):
        self.__read_teacher_subject()
        #self.gsc.runner()        
        #self.class_schedule.runner()
        #self.TeacherSchedule.runner()
        self.ScheduleBuilder.runner()
        
    def transfer_class_schedule_to_teacher_schedule(self):
        pass

    def __read_teacher_subject(self):
        pass 

    def __read_teacher_requirement(self):
        pass

    def __read_leave_date_of_teacher(self):
        pass

    def __read_class_counts_be_arrange(self):
        pass 

    def __read_counts_of_subject(self):
        pass  

    def __read_general_config(self):
        pass 
    