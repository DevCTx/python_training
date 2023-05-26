""" Abstraction class and methods samples """
import abc


class MFD(abc.ABC):
    """ This class is automatically defined as abstract if it has an abstract method """

    def print(self):
        return "Can Print"

    # @abc.abstractclassmethod      # 'abc.abstractclassmethod' is deprecated since Python 3.3.
    @classmethod                    # Use 'classmethod' with 'abc.abstractmethod' instead
    @abc.abstractmethod
    def scan_document(cls):
        return "Can Scan without Imp"


class ImpScan(MFD):
    nb_total = 0

    def __init__(self):
        ImpScan.nb_total += 1

    def scan_document(self):
       return "Can Scan Documents"

    def __repr__(self):
        return "Nb Imp Scan :" + str(ImpScan.nb_total)

imp_scan_1 = ImpScan()

print(imp_scan_1, imp_scan_1.scan_document(), imp_scan_1.print(), sep="\n")

print("MFD :", MFD.scan_document(), sep="\n")
