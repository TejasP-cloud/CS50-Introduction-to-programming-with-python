from fpdf import FPDF

name = input("Enter name: ")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.add_page()

pdf.set_fill_color(245, 245, 220)
pdf.rect(0, 0, 210, 297, style="F")

pdf.set_draw_color(165, 28, 48)
pdf.set_line_width(3)
pdf.rect(8, 8, 194, 281, style="D")

pdf.set_line_width(1)
pdf.rect(12, 12, 186, 273, style="D")

pdf.set_font("Helvetica", style="B", size=36)
pdf.set_text_color(165, 28, 48)
pdf.set_xy(0, 25)
pdf.cell(210, 15, "CS50 Shirtificate", align="C")

pdf.line(20, 43, 190, 43)
pdf.cell(210, 8, "Harvard University...", align="C")

pdf.image("shirtificate.pdf", x=20, y=58, w=170)

pdf.set_text_color(255, 255, 255)
pdf.cell(210, 12, f"{name} took CS50", align="C")

pdf.rect(10, 10, 5, 5, style="F") 

pdf.output("shirtificate.pdf")


