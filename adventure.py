"""week 11"""

import re

import pandas as pd

def load_artifact_data(excel_filepath):
    """Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows."""
    excel_filepath = pd.read_excel(excel_filepath, sheet_name = "Main Chamber",
                  skiprows = 3)
    return excel_filepath

def load_location_notes(tsv_filepath):
    """Reads location data from a Tab-Separated Value (TSV) file."""
    tsv_filepath = pd.read_csv(tsv_filepath, sep = "\t")
    return tsv_filepath

def extract_journal_dates(journal_text):
    """Extracts all dates in MM/DD/YYYY format from the journal text."""
    journal_dates = re.findall(r"\d\d/\d\d/\d\d\d\d", journal_text)
    return journal_dates

def extract_secret_codes(journal_text):
    """Extracts all secret codes in AZMAR-XXX format from the journal text."""
    secret_codes = re.findall(r"AZMAR\-\d\d\d", journal_text)
    return secret_codes
