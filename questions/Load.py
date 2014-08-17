from swirlypy.questions.Text import TextQuestion
import os

class LoadQuestion(TextQuestion):
    """Displays text to the user and waits for newline."""
    def execute(self, data={}):
        self.readdata(data,"vc")
        super().execute(data=data)
#        print("New data")
#        print(data["state"]["vc"])

    def selftest(self, on_err, on_warn):
        # Technically, we can print anything, but it's unlikely that
        # things other than strings will be meaningful.
        if type(self.output) != str:
            on_warn("Output is %s, not str: %s" % (type(self.output),
                self.output))

    def readdata(self,data,myvar):
        if not "state" in data:
            data["state"]=dict()
        myfile = os.path.join(data["rawdir"],self.datafile)
        fin=open(myfile)
        data["state"][myvar]=''
        for line in fin:
            data["state"][myvar] += line
        data["state"][myvar]=data["state"][myvar].replace('\n','').replace('\r','')
#TODO close fin

