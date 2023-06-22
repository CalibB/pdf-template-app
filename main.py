from fpdf import FPDF
import pandas as pd

# Create DataFrame using pandas
df = pd.read_csv('topics.csv')

# Set the base config for the pdf
pdf = FPDF(orientation='P')
pdf.set_font('Helvetica', style='B', size=25)

for index, row in df.iterrows():
    pages = int(row['Pages'])
    pdf.add_page()
    pdf.cell(w=0, h=12, txt=row['Topic'], border='B')
    pages = pages - 1
    while pages >= 0:
        pdf.add_page()
        pages = pages - 1

pdf.output(name='test.pdf')
