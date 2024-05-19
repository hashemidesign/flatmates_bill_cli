import os
import webbrowser

from fpdf import FPDF


class Bill:
    """
    A class to represent a bill.

    Attributes:
    ----------
    amount : float
        The monetary amount of the bill.
    period : str
        The period for which the bill is applicable (e.g., 'January 2024').

    Methods:
    -------
    __repr__():
        Returns a string representation of the Bill instance.
    """

    def __init__(self, amount: float, period: str) -> None:
        self.amount = self._validate_amount(amount)
        self.period = self._validate_period(period)

    def __repr__(self):
        return f"Bill(amount={self.amount}, period='{self.period}')"

    @staticmethod
    def _validate_amount(amount: float) -> float:
        """
        Validates the amount of the bill.

        Parameters:
        ----------
        amount : float
            The monetary amount of the bill.

        Returns:
        -------
        float
            The validated amount.

        Raises:
        ------
        ValueError
            If the amount is not a positive number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        return amount

    @staticmethod
    def _validate_period(period: str) -> str:
        """
        Validates the period of the bill.

        Parameters:
        ----------
        period : str
            The period for which the bill is applicable.

        Returns:
        -------
        str
            The validated period.

        Raises:
        ------
        ValueError
            If the period is not a string.
        """
        if not isinstance(period, str):
            raise ValueError("Period must be a string.")
        return period


class Flatmate:
    """
    A class to represent a flatmate who lives in the flat and pays
    a share of the bill.

    Attributes:
    ----------
    name : str
        The name of the flatmate.
    days_in_house : int
        The number of days the flatmate has been in the house.

    Methods:
    -------
    pays(bill, flatmate):
        Calculates and returns the share of the bill to be paid by this flatmate.
    """

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = self._validate_name(name)
        self.days_in_house = self._validate_days_in_house(days_in_house)

    def pays(self, bill: Bill, flatmate: 'Flatmate') -> float:
        """
        Calculates and returns the share of the bill to be paid by this flatmate.

        Parameters:
        ----------
        bill : Bill
            The bill to be shared.
        flatmate : Flatmate
            The other flatmate sharing the bill.

        Returns:
        -------
        float
            The amount to be paid by this flatmate.
        """
        total_days = self.days_in_house + flatmate.days_in_house
        weight = self.days_in_house / total_days
        return bill.amount * weight

    def __repr__(self):
        return f"Flatmate(name='{self.name}', days_in_house={self.days_in_house})"

    @staticmethod
    def _validate_name(name):
        """
        Validates the name of the flatmate.

        Parameters:
        ----------
        name : str
            The name of the flatmate.

        Returns:
        -------
        str
            The validated name.

        Raises:
        ------
        ValueError
            If the name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        return name

    @staticmethod
    def _validate_days_in_house(days_in_house):
        """
        Validates the number of days in house.

        Parameters:
        ----------
        days_in_house : int
            The number of days the flatmate has been in the house.

        Returns:
        -------
        int
            The validated number of days.

        Raises:
        ------
        ValueError
            If the days_in_house is not a positive integer.
        """
        if not isinstance(days_in_house, int) or days_in_house < 0:
            raise ValueError("Days in house must be a non-negative integer.")
        return days_in_house


class PdfReport:
    """
    A class to create a PDF report of the bill.

    Attributes:
    ----------
    filename : str
        The name of the file where the PDF report will be saved.

    Methods:
    -------
    generate(flatmate1, flatmate2, bill):
        Generates a PDF report showing the bill details and the share each flatmate has to pay.
    """

    def __init__(self, filename: str) -> None:
        self.filename = self._validate_filename(filename)

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill):
        """
        Generates a PDF report showing the bill details and the share each flatmate has to pay.

        Parameters:
        ----------
        flatmate1 : Flatmate
            The first flatmate.
        flatmate2 : Flatmate
            The second flatmate.
        bill : Bill
            The bill to be shared.
        """
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("static/house.png", w=30, h=30)

        pdf.set_font('Arial', 'B', size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        pdf.set_font('Arial', 'B', size=14)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font('Arial', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 1)), border=0, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 1)), border=0, ln=1)

        if not os.path.exists("output"):
            os.makedirs("output")
        os.chdir("output")
        pdf.output(f'{self.filename}.pdf')
        webbrowser.open(f'{self.filename}.pdf')

    @staticmethod
    def _validate_filename(filename):
        """
        Validates the filename.

        Parameters:
        ----------
        filename : str
            The name of the file where the PDF report will be saved.

        Returns:
        -------
        str
            The validated filename.

        Raises:
        ------
        ValueError
            If the filename is not a string.
        """
        if not isinstance(filename, str):
            raise ValueError("Filename must be a string.")
        return filename
