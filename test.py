class LogDestination(object):

    def open(self):
        """Open a connection to the target service"""
        return True

    def close(self):
        """Close the connection to the target service"""
        pass

    def is_opened(self):
        """Check if the connection to the target is able to receive messages"""
        return True

    def init(self):
        """This method is called at initialization time"""
        return True

    def deinit(self):
        """This method is called at deinitialization time"""
        pass

    def send(self, msg):
        """Send a message to the target service

        It should return True to indicate success, False will suspend the
        destination for a period specified by the time-reopen() option."""
        pass


class handle(LogDestination):
    def __init__(self):
        self.outfile = None

    def init(self):
        self.outfile = open('/devel/log.txt', 'a')
        self.outfile.write("initialized\n")
        self.outfile.flush()
        return True

    def open(self):
        self.outfile.write("opened\n")
        self.outfile.flush()
        return True

    def close(self):
        self.outfile.write("closed\n")
        self.outfile.flush()
        return True

    def deinit(self):
        self.outfile.write("deinit\n")
        self.outfile.flush()
        self.outfile.close();
        return True

    def send(self, msg):
        self.outfile.write("Name Value Pairs are \n")

        for key,v in msg.items():
            self.outfile.write(str(key)+" "+str(v)+"\n");
        self.outfile.flush()
        return True
