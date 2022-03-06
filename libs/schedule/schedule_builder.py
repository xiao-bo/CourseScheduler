
class ScheduleBuilder(object):
    def __init__(self):
        self.config = 1
        self.date = ['1/20', '1/21', '1/22']  # , '1/22', '1/24', '1/25',
        # '1/26', '2/8', '2/9', '2/10']
        self.teacher_data = [
            {
                "name": '阿梅',
                "code": '1',
                "subject": 'C',
                'count': 3
            },
            {
                "name": 'bobo',
                "code": '2',
                "subject": 'M',
                'count': 3
            }
        ]
        self.count_each_day = 2
        pass

    def runner(self):
        print('this is ScheduleBuilder runner')
        self.build_schedule()

    def build_schedule(self):

        schedule = [ [None for x in range(0, self.count_each_day)] for y in range(0,len(self.date))]
        print(schedule)
        pass

    def __arrange_course(self):
        pass

    def __check_arrange(self):
        pass

    def __check_requirements_of_teacher(self):
        pass

    def __check_reqirements_of_class(self):
        pass
