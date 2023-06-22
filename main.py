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
    pdf.ln(278)
    pdf.cell(w=0, txt=row['Topic'], align='R')
    pages = pages - 1

    # Page lines
    starting_y_position = 32
    pdf.set_draw_color(180, 180, 180)
    pdf.line(10, starting_y_position, 200, starting_y_position)
    for i in range(0, 25):
        starting_y_position = starting_y_position + 10
        pdf.line(10, starting_y_position, 200, starting_y_position)

    for pages in range(pages):
        pdf.add_page()

        # Set Footer
        pdf.set_font_size(10)
        pdf.set_text_color(180, 180, 180)
        pdf.ln(278)
        pdf.cell(w=0, txt=row['Topic'], align='R')

        # Page lines
        starting_y_position = 32
        pdf.set_draw_color(180, 180, 180)
        pdf.line(10, starting_y_position, 200, starting_y_position)
        for i in range(0, 25):
            starting_y_position = starting_y_position + 10
            pdf.line(10, starting_y_position, 200, starting_y_position)

pdf.output(name='test.pdf')
