# skygo
Overall Structure
I. Import library
II. File upload
III. Country Classification
IV. Day counts
V. Number of devices lent per
day(One day)
VI. Number of devices lent per
week(More Day)
Import library ・import streamlit as st
# Imports the Streamlit library
and renames it as 'st'
・import pandas as pd
# Imports the pandas library and
renames it as 'pd'
・import datetime
# Imports the Python datetime
module, which provides classes
for working with dates and times.
・import openpyxl
# Import library to read/write
Excel file
Import data
uploaded_file = st.file_uploader("Upload csv UTF-8",
type="csv")
dataframe = pd.read_csv(uploaded_file,
comment="#")
・Using Streamlit's file upload feature to
have the user upload a file.
・When a file is uploaded in CSV
format with UTF-8 encoding, it gets
stored in a DataFrame.
Variable
• uploadfile: Files uploaded to the
web app(xlxs file only)
• dataframe: DataFrame from the
loaded file

• dataframe_us: DataFrame
containing only entries with the
country name 'USA'.
• dataframe_jp: DataFrame
containing only entries with the
country name 'JAPAN'.
• dataframe_all: Same as dataframe
• selected_country: The selected
country name from the select box.
• dataframe_filtered: The dataset of
the selected country name from the
select box.
• start_date_column: The data
column with the name “From date’
from the loaded Excel file.
• end_date_column: The data
column with the name “To date’ from
the loaded Excel file.
• Date: Today’s date
• date_start & date_end:
Calculating dates one year before
and one year ahead from a given
date as reference
• start_date & end_date:
Converting a date type
(datetime.date) to a
datetime.datetime type.
• daily_counts: Counting the number
of data entries for each day
• d: Limit selectable dates to one year
before and one year after the current
date.
• date_input: Ask the user to enter
the date
• date_start_More &

date_end_More: Store the user-
inputted start and end dates for an

extended date range.
• date_start_More_str &
date_end_More_str: Converting
date-type to string-type data and
storing it.

• More_date: Store the subset of
data that is being extracted from the
daily counts DataFrame based on the
date range defined by
date_start_More_str and
date_end_More_str.

If sentence
if uploaded_file is not None:
→Run programs only when files are
uploaded
if selected_country == "USA":
dataframe_filtered = dataframe_us
elif selected_country == "JAPAN":
dataframe_filtered = dataframe_jp
else:
dataframe_filtered = dataframe_all
→The dataset of the country selected in
the select box determines the data that
goes into ‘dataframe_filtered’.
if date_input:
→Run programs only when user input
