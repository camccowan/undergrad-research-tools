#!/usr/bin/env python2
#Filename:  SpiderBLASTParser.py
#Caryn McCowan

#Description:  This script is intended to parse a  previously saved BLAST XML output file into a text file
#formatted with "tabs" (/t) for easy importation into an excel spreadsheet.  This program imports
#the following items in oder:  FASTA header, , Top Hit(name), top hit genbank accessionn number, E value,
#reading frame, organism.


from Bio.Blast import NCBIXML
import time

print "\n\n"
print "***Welcome to the BLAST Result XML Parser***"
print "\n"

#prompt user to enter path to XML file
print "please enter the full path to your input XML file:"
xml_path = raw_input("-->")

time.sleep(1)

#prompt user to enter path to output file
print "please enter the full path to your output .txt file:"
output_file = raw_input("-->")

time.sleep(1)

#open the xml file
blast_result= open(xml_path)

#parse the xml file
blast_records= NCBIXML.parse(blast_result)  #parsed results

save_file= open(output_file, "a")
#write the table header
save_file.write("query FASTA header" + "\t" + "top hit name" + "\t" + "top hi accession number" + "\t" + "top hit E-value" + "\t" + "alignment reading frame" + "\t" + "alignment species" +"\n")

###################################################################################################

#The following block of script loops through the records int he XML file.
#Basic results are printed to the terminal

for blast_record in blast_records:

    n = len(blast_record.alignments)   # this is the number of alignments
    query = blast_record.query
    #querylist = query.split(|)
    #queryname = querylist[-2]
    print query,  " has ", str(n), " alignments"

    #if a query turns up no sig matches, write this to file:
    if n == 0:
        save_file.write(quy+"\t\t no significant matches\n")
        save_file.close

    #if there are matches: set up loop to iterate through the hits for *each* query
    else:
        i=0
        for alignment in blast_record.alignments:
            i=i+1

            #if the alignment is a top hit:
            if i==1:

                ##########################################################################
                #this block defines variables for each blast output component.
                #some of these required additional string parsing
                query = query
                #parse out the text before the "[", in this case, the name of the protein
                hd= alignment.hit_def.partition("[")
                #parse out the text after the "[", in this case, the name of the protein
                hd2=hd[2]
                #before the '['
                hit_protein= hd[0]
                #after the ']'
                hit_species= hd2.partition("]") [0]

                #accession number is burried in this tag
                hit_id= alignment.hit_id.split("|")
                accession_num=hit_id[-2]

                hsp= alignment.hsps[0]
                readingframe= str(hsp.frame[0])
                expect = str(hsp.expect)
                ##############################################################################
                #Write blast results to a tab separated text file
                save_file= open(output_file, "a")
                save_file.write( query + "\t" + hit_protein + "\t" + accession_num + "\t" + expect + "\t" + readingframe + "\t"+ hit_species + "\n" )
                save_file.close

blast_records.close

print ("Program Complete \n\n")
