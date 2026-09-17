from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active
sheet.title = "FlightSearchData"

sheet["A1"] = "From"
sheet["B1"] = "To"
sheet["C1"] = "Departure Date"

sheet["A2"] = "Hyderabad"
sheet["B2"] = "Chennai"
sheet["C2"] = "Sunday, September 13, 2026"

workbook.save("FlightSearchData.xlsx")

print("Excel file created successfully!")