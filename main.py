from fpdf import FPDF
import pandas as pd

# Create DataFrame using pandas
df = pd.read_csv('topics.csv')

# Set the base config for the pdf
pdf = FPDF(orientation='P')
pdf.set_font('Helvetica', style='B')
pdf.set_auto_page_break(auto=False)

for index, row in df.iterrows():
    pages = int(row['Pages'])
    pdf.add_page()
    pdf.set_font_size(25)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], border='B')

    # Set Footer
    pdf.set_font_size(10)
    pdf.set_text_color(180, 180, 180)
    pdf.ln(273)
    pdf.cell(w=0, txt=row['Topic'], align='R')
    pages = pages - 1
    for pages in range(pages):
        pdf.add_page()

        # Set Footer
        pdf.set_font_size(10)
        pdf.set_text_color(180, 180, 180)
        pdf.ln(273)
        pdf.cell(w=0, txt=row['Topic'], align='R')

pdf.output(name='test.pdf')
