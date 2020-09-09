import unittest

from django.test.runner import DiscoverRunner


class EmojiTestRunner(DiscoverRunner):
    def get_resultclass(self):
        klass = super().get_resultclass()
        if klass is None:
            return EmojiTestResult
        return klass


class EmojiTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If the "dots" style was going to be used, show emoji instead
        self.emojis = self.dots
        self.dots = False

    def addSuccess(self, test):
        super().addSuccess(test)
        if self.emojis:
            self.stream.write('✅')
            self.stream.flush()

    def addError(self, test, err):
        super().addError(test, err)
        if self.emojis:
            self.stream.write('💥')
            self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        if self.emojis:
            self.stream.write('❌')
            self.stream.flush()

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        if self.emojis:
            self.stream.write("⏭")
            self.stream.flush()

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        if self.emojis:
            self.stream.write("❎")
            self.stream.flush()

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        if self.emojis:
            self.stream.write("✳️")
            self.stream.flush()

    def printErrors(self):
        if self.emojis:
            self.stream.writeln()
        super().printErrors()
