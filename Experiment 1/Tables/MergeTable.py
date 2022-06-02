import pdfkit
pdfkit.from_file(['Experiment 1/Tables/E1-A-Table.html', 'Experiment 1/Tables/E1-AA-Table.html', 'Experiment 1/Tables/E1-CAM-Table.html', 
'Experiment 1/Tables/E1-EA-Table.html', 'Experiment 1/Tables/E1-SA-Table.html'], 'Experiment 1/Tables/E1-Tables.pdf')