#-*- coding: utf-8 -*-
"""
(ref) 코드 참고: https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/trivial_compression.py
"""

"""
nucleotide 정보는 2진수로 다음에 대응함: 
* A := 00
* C := 01
* G := 10
* T := 11
"""




#%% 
from sys import getsizeof
from typing import Generator


# ================================================================= #
#                        1. Create a class                          #
# ================================================================= #
# %% 01. Gene 정보를 압축하는 클래스 정의  
class CompressedGene:
    def __init__(self, gene: str) -> None:  
        self._compress(gene)  # 압축 실행 

    
    def _compress(self, gene: str) -> None:
        """ String representation으로 저장된 정보를 받아서 
            bit-string 으로 압축하기 
        """
        self.bit_string: int = 1  # start with sentinel
                                  # 그냥 아무 int 값으 초기화 

        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":  # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")


    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] reverses string by slicing backwards


    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()

# ================================================================= #
#                            2. Main                                #
# ================================================================= #
# %% 02. Main
if __name__ == '__main__':
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    
    print(f"the size before compression: {getsizeof(original)} bytes")


    compressed: CompressedGene = CompressedGene(original)  # 압축 객체 초기화 
    print(f"compressed is {getsizeof(compressed.bit_string)} bytes")

    print(compressed)  # decompress
    print(f"original and decompressed are the same: {original == compressed.decompress()}")


# %%
