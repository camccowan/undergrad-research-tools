# undergrad-research-tools

for my undergraduate research project I needed to create a couple of simple tools to BLAST and catalog 
large numbers of EST sequences that I was generating in the lab.  I used-already available tools in the open source third-party BioPython package.  There are two tools in this repository that go together:

1.  An easy-to-use batch BLAST script that submits a large file of sequences to NCBI.  It returns an XML file for downstream parsing.

2.  A BLAST xml parser the records info from the top hit in each BLAST query in a tab-separated text file that can be opened in excel.  Before I wrote this script, I had to record the results into an excel sheet manually.

BioPython can be downloaded from here :  https://biopython.org/
