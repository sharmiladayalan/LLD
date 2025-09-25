"""     Break the interface into smaller role specific      """

from abc import ABC, abstractmethod

class Printer(ABC):

    @abstractmethod
    def print_doc(self, document):
        pass

class Fax(ABC):

    @abstractmethod
    def fax(self):
        pass

class Scan(ABC):

    @abstractmethod
    def scan(self, document):
        pass


class Oldprinter(Printer):

    def print_doc(self, document):
       print(f"Printing : {document}")

class MultiFunctionalPrinter(Printer, Fax, Scan):

    def print_doc(self, document):
       print(f"Printing : {document}")
    def fax(self, document):
       print(f"Faxing : {document}")
    def scan(self):
       print(f"Scaning Document ")


old_printer = Oldprinter()
old_printer.print_doc("resume.pdf")


multi_printer = MultiFunctionalPrinter()
multi_printer.print_doc("word.excel")
multi_printer.fax("informtion poster")
multi_printer.scan()

"""
    ==> Old Printer has only one responsiblity (printing)
    ==> Multi Printer extends functionality naturally.
    ==> No class is forced to implement unused methods
"""
