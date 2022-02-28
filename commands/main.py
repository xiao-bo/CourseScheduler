from basic_command import BasicCommand

def main():
    init_parameter = BasicCommand()
    root_path = init_parameter.PROJECT_ROOT_PATH

    from libs.schedule.scheduler import Scheduler
    print('123')
    scheduler = Scheduler()
    scheduler.runner()

if __name__ == '__main__':
    main()