#!/usr/bin/env python3
from subprocess import run
def FileDiff(WhichFile):
    Length = 27*8
    OutpuOffset = 2
    BitError = 0

    if WhichFile == True:
        BufferOffset = 49
    else:
        BufferOffset = 98

    cmd1 = "xxd -b -c1 bpsk_vector_output.dat | cut -d\" \" -f2 | tr -d \"\\n\""
    cmd2 = "xxd -b -c1 bpsk_vector_output_receptor.dat | cut -d\" \" -f2 | tr -d \"\\n\""

    data1 = run(cmd1,capture_output=True,shell=True) 
    TransmissionData = str(data1.stdout)

    data2 = run(cmd2,capture_output=True,shell=True) 
    ReceptionData = str(data2.stdout)

    for i in range(0, Length):
        if(TransmissionData[i + OutpuOffset] != ReceptionData[i+OutpuOffset + BufferOffset]):
            BitError+=1

    print("\nTransmissão: " + TransmissionData[OutpuOffset:Length] + "\n\n" + "Recepção: " 
          + ReceptionData[(OutpuOffset+BufferOffset):(Length+OutpuOffset+BufferOffset)])
    print("\n Erros de deteção: " + str(BitError))
    print("\n B = " + str(WhichFile))

    return BitError

