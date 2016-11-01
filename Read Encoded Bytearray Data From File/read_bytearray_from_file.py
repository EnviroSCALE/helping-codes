with open("logs/missing.bin", "r") as infile:
    for line in infile:
        unpacked = decode_bitstruct(line, c)
        print unpacked
