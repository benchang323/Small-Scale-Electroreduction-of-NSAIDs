import pdfkit
pdfkit.from_file(['Experiment 4/Tables/E4-A-Table.html', 'Experiment 4/Tables/E4-AA-Table.html', 'Experiment 4/Tables/E4-CAM-Table.html', 
'Experiment 4/Tables/E4-EA-Table.html', 'Experiment 4/Tables/E4-SA-Table.html'], 'Experiment 4/Tables/E4-Tables.pdf')