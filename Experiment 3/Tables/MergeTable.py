import pdfkit
pdfkit.from_file(['Experiment 3/Tables/E3-A-Table.html', 'Experiment 3/Tables/E3-AA-Table.html', 'Experiment 3/Tables/E3-CAM-Table.html', 
'Experiment 3/Tables/E3-EA-Table.html', 'Experiment 3/Tables/E3-SA-Table.html'], 'Experiment 3/Tables/E3-Tables.pdf')