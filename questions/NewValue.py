from swirlypy.questions.Recording import RecordingQuestion
import os

class NewValueQuestion(RecordingQuestion):
    """Tests dictionary updating feature. """
    def selftest(self, on_err, on_warn):
        # Technically, we can print anything, but it's unlikely that
        # things other than strings will be meaningful.
        if type(self.output) != str:
            on_warn("Output is %s, not str: %s" % (type(self.output),
                self.output))
    def test_response(self, response, data={}):
        return response["changed"]==self.value


