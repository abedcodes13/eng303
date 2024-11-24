import win32com.client
import camelot
import os

def convert_pdf_to_single_column(input_pdf_path, output_pdf_path):
    # Create an instance of Word application
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False  # Set to True if you want to see the process

    # Open the PDF file in Word
    doc = word.Documents.Open(input_pdf_path)

    # Select the entire content of the document
    doc.Content.Select()

    # Apply single-column layout (set columns to 1)
    word.Selection.PageSetup.TextColumns.SetCount(1)

    # Optionally adjust other formatting (font size, alignment, etc.)

    # Save the document as PDF
    doc.SaveAs(output_pdf_path, FileFormat=17)  # 17 is the constant for PDF format

    # Close the document and Word application
    doc.Close(SaveChanges=False)
    word.Quit()

def clean_table(df):
    # Step 1: If a cell contains more than or equal to 40 characters, make that cell empty
    df = df.map(lambda x: '' if len(str(x)) >= 30 else x)
    
    total_chars = 0
    total_numeric_chars = 0
    
    for _, row in df.iterrows():
        for cell in row:
            cell_str = str(cell)
            total_chars += len(cell_str)
            total_numeric_chars += sum(c.isdigit() for c in cell_str)
    
    if total_chars > 0:
        numeric_percentage = (total_numeric_chars / total_chars)
    else:
        numeric_percentage = 0

    if total_chars <= 150:
        return None  # Delete table by returning None
    
    # If numeric characters make up less than 7% of the dataframe, return None
    if numeric_percentage < 0.07:
        return None

    # Step 2: Delete rows and columns with all empty entries
    df = df.loc[~(df == '').all(axis=1)]  # Delete rows with all empty entries
    df = df.loc[:, ~(df == '').all(axis=0)]  # Delete columns with all empty entries
    
    # Step 3: If a table has 2 or fewer columns, delete the table
    if df.shape[1] <= 2:
        return None  # Delete table by returning None
    
    has_number = df.map(lambda x: any(c.isdigit() for c in str(x))).values.any()
    
    # If no numeric character is found in the entire dataframe, return None
    if not has_number:
        return None
    
    return df  # Return cleaned DataFrame

def extract_tables_from_pdf(pdf_path, directory):
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

    cleaned_tables = []
    for idx in range(len(tables)):
        df = tables[idx].df
        cleaned_df = clean_table(df)  # Apply cleaning steps
        if cleaned_df is not None:
            cleaned_tables.append(cleaned_df)  # Only keep non-deleted tables
    

    # Export cleaned tables to CSV
    if cleaned_tables:
        for idx, cleaned_table in enumerate(cleaned_tables):
            output_csv_path = os.path.join(directory, f'single_cleaned_table_{idx}.csv')
            cleaned_table.to_csv(output_csv_path, index=False)
            print(f"Cleaned table saved to: {output_csv_path}")
    else:
        print("No tables left after cleaning.")

def process_multiple_pdfs(input_pdf_paths):
    for input_pdf_path in input_pdf_paths:
        directory, filename = os.path.split(input_pdf_path)
        base_filename, ext = os.path.splitext(filename)
        output_pdf_path = os.path.join(directory, f'single_{base_filename}.pdf')

        # Convert the PDF to single-column layout
        convert_pdf_to_single_column(input_pdf_path, output_pdf_path)

        # Extract tables from the converted PDF
        extract_tables_from_pdf(output_pdf_path, directory)

# List of input PDF paths
input_pdf_paths = [
    # r"C:\Users\mhmda\Downloads\eng303\Differences in groundwater and chloride residence\Differences in groundwater and chloride residence.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Distinguishing groundwater flow paths\Distinguishing groundwater flow paths.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Environmental isotopes as indicators of groundwater recharge, residence times and salinity\Environmental isotopes as indicators of groundwater recharge, residence times and salinity.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Estimating retention potential of headwater catchment using Tritium time  series\Estimating retention potential of headwater catchment using Tritium time series.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Factors affecting carbon-14 activity of unsaturated zone CO2\Factors affecting carbon-14 activity of unsaturated zone CO2.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Geochemical tracers associated with methane in aquifers\Geochemical tracers associated with methane in aquifers.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Groundwater age, mixing and flow rates in the vicinity of large\Groundwater age, mixing and flow rates in the vicinity of large.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Groundwater mean residence times of a subtropical barrier sand island\Groundwater mean residence times of a subtropical barrier sand island.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\How water isotopes (18O, 2 H, 3 H) within an\How water isotopes (18O, 2 H, 3 H) within an.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Identifying the contribution of regional groundwater to the basef\Identifying the contribution of regional groundwater to the basef.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Integrating major ion geochemistry\Integrating major ion geochemistry.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Island groundwater resources, impacts of abstraction and a drying\Island groundwater resources, impacts of abstraction and a drying.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Lithium and strontium isotope dynamics in a carbonate island aquifer\Lithium and strontium isotope dynamics in a carbonate island aquifer.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Marine water from mid-Holocene sea level highstand\Marine water from mid-Holocene sea level highstand.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Mean transit times in headwater catchments\Mean transit times in headwater catchments.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\River infiltration to a subtropical alluvial\River infiltration to a subtropical alluvial.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Sources and mean transit times of intermittent streamflow in semi-arid\Sources and mean transit times of intermittent streamflow in semi-arid.pdf",
    r"C:\Users\mhmda\Downloads\eng303\The evolution of stable silicon isotopes in a coastal carbonate aquifer\The evolution of stable silicon isotopes in a coastal carbonate aquifer.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Transit times from rainfall to baseflow in headwater catchments estimated using tritium\Transit times from rainfall to baseflow.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Assessing the controls and uncertainties on mean transit times in\Assessing the controls and uncertainties on mean transit times in.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Analysis of environmental isotopes in groundwater to understand\Analysis of environmental isotopes in groundwater to understand.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using 14C and 3 H to delineate a recharge ‘window’ into the Perth Basin aquifers\Using 14C and 3 H to delineate a recharge ‘window’ into the Perth Basin aquifers.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using geochemistry to understand water sources and transit times\Using geochemistry to understand water sources and transit times.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using groundwater geochemistry and environmental isotopes to assess\Using groundwater geochemistry and environmental isotopes to assess.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using hydrogeochemistry to understand inter-aquifer mixing/Using hydrogeochemistry to understand inter-aquifer mixing.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using multiple lines of evidence to map groundwater recharge in a rapidly/Using multiple lines of evidence to map groundwater recharge in a rapidly.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using multiple methods to investigate the effects of land-use\Using multiple methods to investigate the effects of land-use.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\Using tritium to document the mean transit time and sources\Using tritium to document the mean transit time and sources.pdf",
    # r"C:\Users\mhmda\Downloads\eng303\On the hydrology of the bauxite oases\On the hydrology of the bauxite oases.pdf",
]

# Process multiple PDFs
process_multiple_pdfs(input_pdf_paths)
