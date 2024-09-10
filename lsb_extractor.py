import sys


class LSBExtractor:
    def _get_lsb_from_byte(self, byte: bytes) -> int:
        return byte & 0x01

    def _input_last_bit_on_byte(self, bit: int, byte: bytes) -> bytes:
        return (byte << 1) | bit

    def extract(self, data: bytes) -> bytes:
        result = b""
        number_of_bytes = len(data)

        for i in range(0, number_of_bytes, 8):
            new_byte = 0

            for byte in data[i : i + 8]:
                bit = self._get_lsb_from_byte(byte)
                new_byte = self._input_last_bit_on_byte(bit, new_byte)

            result += new_byte.to_bytes(1, sys.byteorder)

        return result
