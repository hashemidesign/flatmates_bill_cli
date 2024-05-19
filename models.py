import os
import webbrowser

from fpdf import FPDF


class Bill:
    """
    Bill class holds information about a bill, such as amount, and
    period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays
    a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return bill.amount * weight


class PdfReport:
    """
    Creates a pdf report of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("static/house.png", w=30, h=30)

        pdf.set_font('Arial', 'B', size=24)
        pdf.cell(w=0, h=80, txt="FlatMates Bill", border=1, align='C', ln=1)

        pdf.set_font('Arial', 'B', size=14)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font('Arial', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 1)), border=0, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 1)), border=0, ln=1)

        os.chdir("output")
        pdf.output(f'{self.filename}.pdf')
        webbrowser.open(f'{self.filename}.pdf')
