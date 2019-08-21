import time
import threading


class RunJob(object):
    def __init__(self, durationMillis, callback):
        self.durationMillis = durationMillis
        self.callback = callback
        self.timeJobStarted = None


# Note: this is just a sample implimentation to help me run the code.
class Runnable(object):
    def __init__(self, callback):
        self.callback = callback

    def run(self):
        print
        "\nRunning the job", self.callback


class MySystem(object):
    def __init__(self):
        self.q = []
        self.hasProcessingStarted = False
        self.thread = threading.Thread(target=self.processJob)
        self.thread.daemon = True

        # Note: this is just a sample implimentation to help me run the code.

    def setTimer(self, durationMillis, callback):
        # Waits durationMillis milliseconds then runs the callback.
        print
        "Set timer is sleeping for", durationMillis, "milliseconds"
        time.sleep(durationMillis / 1000)
        callback.run()

    # Note: this is just a sample implimentation to help me run the code.
    def getCurrentTimeMillis(self):
        # Returns the current time in milliseconds
        return int(round(time.time() * 1000))

    def processJob(self):
        print
        "\nTrying to process job in background while you add stuff to the queue"
        self.hasProcessingStarted = True
        while (self.q):
            # If no jobs have been scheduled, then schedule it
            if (self.q[0].timeJobStarted == None):
                self.setTimer(self.q[0].durationMillis, self.q[0].callback)
                # There might be some delay of few milliseconds when I update timeJobStarted
                self.q[0].timeJobStarted = self.getCurrentTimeMillis()
            else:
                # get the current time and check has the specified milliseconds in the job passed ?
                if (self.q[0].durationMillis <= (self.getCurrentTimeMillis() - self.q[0].timeJobStarted)):
                    self.q.pop(0)
        self.hasProcessingStarted = False

    def addTimer(self, durationMillis, callback):
        print
        "\nAdded job to the queue"
        job = RunJob(durationMillis, callback)
        self.q.append(job)
        # If the queue is already not being processed then start processing it
        # else you have already added a task to the queue so let processJob take care of it, no need to start new thread for it.
        if not (self.hasProcessingStarted):
            self.thread.start()
