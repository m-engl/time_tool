import time

class Timer:

    def start(self):
        startPoint = time.time()
        startPoint = int(startPoint)
        return startPoint

    def stop(self):
        stopPoint = time.time()
        stopPoint = int(stopPoint)
        return stopPoint

    def format_time(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        return ("{0} h {1} min {2} sec".format(int(hours), int(mins), sec))

    def show_time_elapsed(self, start, stop, format="hms"):

        timeLapsed = stop - start

        if format == "hms":
            return self.format_time(timeLapsed)
        elif format == "seconds":
            return timeLapsed


##### testing class, to be deleted #####
Kamil = Timer()
input("Press Enter to START")
start = Kamil.start()
input("Press Enter to STOP")
stop = Kamil.stop()
print(Kamil.show_time_elapsed(start, stop))