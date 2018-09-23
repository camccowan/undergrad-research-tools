#!/usr/bin/env python 2

#Filename:  SPIDER_BLAST.py

#The BLAST search may take several minutes or hours to run
#depending on the number and length of sequences in the FASTA file
################################################################################

from Bio.Blast import NCBIWWW
import time

time.sleep(.5)

print "\n\n"
print "***Welcome to the NCBI Batch BLASTx Python Program***"


#prompt user to enter path to a FASTA file
print "please enter the full path to a FASTA file:"
input_file = raw_input("-->")
fasta_file = open(input_file).read()

time.sleep(1)

#prompt user to enter path to a FASTA file
print "please enter the full path to your output XML file:"
output_file = raw_input("-->")

#The  format_type keyword is only required if the output is something other than .XML.
#The output options are "Text" "HTML" "ASN.1" and "XML"

blast_result = NCBIWWW.qblast("blastx", "nr", fasta_file, format_type="XML")

#Open an output file & write results inside
result_file = open(str(output_file), "w")

result_file.write(blast_result.read())
result_file.close()
blast_result.close()


print "BLAST Search Completed"
print "the full path to your XML data is: " + output_file

#END program
