import pdfkit
pdfkit.from_file(['Experiment 2/Tables/E2-A-Table.html', 'Experiment 2/Tables/E2-AA-Table.html', 'Experiment 2/Tables/E2-CAM-Table.html', 
'Experiment 2/Tables/E2-EA-Table.html', 'Experiment 2/Tables/E2-SA-Table.html'], 'Experiment 2/Tables/E2-Tables.pdf')