# Flatmates Bill Splitter

Flatmates Bill Splitter is a Python application that calculates and generates a PDF report for splitting a bill between flatmates based on the number of days they stayed in the house during the billing period.

## Features

- Calculates the share of the bill each flatmate has to pay.
- Generates a PDF report with the details of the bill and each flatmate's share.
- Simple command-line interface for inputting bill and flatmate details.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flatmates-bill-splitter.git
    cd flatmates-bill-splitter
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Follow the prompts to enter the bill amount, billing period, and details of the flatmates (name and number of days stayed).

3. The application will display the amount each flatmate needs to pay.

4. A PDF report will be generated and automatically opened, showing the bill details and each flatmate's share.

## Example

```plaintext
Enter the bill amount in dollars: 120.50
What is the period of the bill? E.g. May 2024: May 2024
What is your name? John
How many days did John stay in the house during May 2024? 20
What is your flatmate's name? Jane
How many days did Jane stay in the house during May 2024? 10

John pays: $80.33
Jane pays: $40.17
```

## File Structure
```plaintext
flatmates-bill-splitter/
│
├── static/
│   └── house.png           # Image used in the PDF report
├── output/
│   └── Report.pdf          # Generated PDF report
├── main.py                 # Main script to run the application
├── bill.py                 # Contains the Bill class
├── flatmate.py             # Contains the Flatmate class
├── pdf_report.py           # Contains the PdfReport class
└── requirements.txt        # List of dependencies
```

## Classes
### Bill
Represents a bill with amount and period.

### Flatmate
Represents a flatmate who pays a share of the bill based on the number of days stayed in the house.

### PdfReport
Generates a PDF report of the bill.

## Dependencies
- FPDF
- webbrowser
- os

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## Contact
For any questions or suggestions, please open an issue or contact [m.hashemi.code@gmail.com](mailto:m.hashemi.code@gmail.com).

