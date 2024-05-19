from models import Bill, Flatmate, PdfReport

if __name__ == '__main__':
    try:
        amount = float(input("Enter the bill amount in dollars: "))
        period = input("What is the period of the bill? E.g. May 2024: ")

        name1 = input("What is your name? ")
        dih1 = int(input(f"How many days did {name1} stay in the house during {period}? "))

        name2 = input("What is your flatmate's name? ")
        dih2 = int(input(f"How many days did {name2} stay in the house during {period}? "))

        flatmate1 = Flatmate(name1, dih1)
        flatmate2 = Flatmate(name2, dih2)
        bill = Bill(amount, period)

        print(f'{name1} pays: ${flatmate1.pays(bill=bill, flatmate=flatmate2):.2f}')
        print(f'{name2} pays: ${flatmate2.pays(bill=bill, flatmate=flatmate1):.2f}')

        pdf_report = PdfReport('Report')
        pdf_report.generate(flatmate1, flatmate2, bill)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

