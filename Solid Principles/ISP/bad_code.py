"""
    ==> Clients should not be forced to depend on methods they do not use

    ==> Instead of one big "fat" interface create multiple smaller, more specific ones

    ==> This principle avoid bloating classes with unnecessary methods and keeps contract clean.
"""

"""     Why its matter.?
            
            ==> Prevents classes from having "dummy" methods.
            ==> Keeps system flexible and easier.
            ==> Reduce unnesecessary coupling between unrelated behaviours.

"""
# Bad Example Code..

from abc import ABC, abstractmethod

class MultifunctionDevice(ABC):

    @abstractmethod
    def print_doc(self, document: str):
        pass
    @abstractmethod
    def scan(self):
        pass
    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(MultifunctionDevice):

    def print_doc(self, document: str):
        self.document = document
        print(f"Printing Document : {self.document}")

    def scan(self):
       raise NotImplementedError("This Printer Cannot Scan..")
    
    def fax(self, document):
        raise NotImplementedError("This Printer Cannot fax..")
    

oldprinter = OldPrinter()
# oldprinter.print_doc("resume.pdf")
oldprinter.scan()

"""     What is the Problem     """

"""     
    ==> Old printer is forced to depend on scan and fax even thoung it doesn't support them..
"""

