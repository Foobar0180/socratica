class Printer:
    def print(self, document):
        raise NotImplementedError


class Fax:
    def fax(self, document):
        raise NotImplementedError


class Scanner:
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionDevice(Printer, Fax, Scanner):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class FaxMachine(Fax):
    def fax(self, document):
        pass


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class DotMatrixPrinter(Printer):
    def print(self, document):
        pass

