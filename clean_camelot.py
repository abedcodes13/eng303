import camelot
import os
import matplotlib.pyplot as plt

def clean_table(df):
    # Empty cells that have more than or equal to 30 characters
    df = df.applymap(lambda x: '' if len(str(x)) >= 30 else x)

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

    # Delete empty rows and columns
    df = df.loc[~(df == '').all(axis=1)] 
    df = df.loc[:, ~(df == '').all(axis=0)] 
    
    # Delete table with 2 or fewer columns
    if df.shape[1] <= 2:
        return None
    
    has_number = df.applymap(lambda x: any(c.isdigit() for c in str(x))).values.any()
    
    # If no numeric character is found in the entire dataframe, return None
    if not has_number:
        return None
    
    return df

def process_multiple_pdfs(input_pdf_paths):
    for input_pdf_path in input_pdf_paths:
        # Extract directory and base filename
        directory, filename = os.path.split(input_pdf_path)
        base_filename, ext = os.path.splitext(filename)

        # Read the PDF using Camelot's stream method
        tables = camelot.read_pdf(input_pdf_path, pages='all', flavor='stream', flag_size = True)

        cleaned_tables = []
        for i in range(len(tables)):
            # camelot.plot(tables[i], kind='grid')
            # plt.show()
            print(i)
            if i == 18:

                camelot.plot(tables[i], kind='text')
                plt.show()

            df = tables[i].df
            cleaned_df = clean_table(df)  # Apply cleaning steps

            if cleaned_df is not None:
                cleaned_tables.append(cleaned_df)  # Only keep non-deleted tables

        # Export cleaned tables to CSV with automated paths
        if cleaned_tables:
            for idx, cleaned_table in enumerate(cleaned_tables):
                output_csv_path = os.path.join(directory, f'cleaned_table_{idx}.csv')
                # cleaned_table.to_csv(output_csv_path, index=False)


                print(f"Cleaned table saved to: {output_csv_path}")
        else:
            print(f"No tables left after cleaning for {input_pdf_path}.")

# Replace with full path of input file
input_pdf_paths = [
    r"C:\Users\mhmda\Downloads\eng303\Differences in groundwater and chloride residence\Differences in groundwater and chloride residence.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Distinguishing groundwater flow paths\Distinguishing groundwater flow paths.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Environmental isotopes as indicators of groundwater recharge, residence times and salinity\Environmental isotopes as indicators of groundwater recharge, residence times and salinity.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Estimating retention potential of headwater catchment using Tritium time  series\Estimating retention potential of headwater catchment using Tritium time series.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Factors affecting carbon-14 activity of unsaturated zone CO2\Factors affecting carbon-14 activity of unsaturated zone CO2.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Geochemical tracers associated with methane in aquifers\Geochemical tracers associated with methane in aquifers.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Groundwater age, mixing and flow rates in the vicinity of large\Groundwater age, mixing and flow rates in the vicinity of large.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Groundwater mean residence times of a subtropical barrier sand island\Groundwater mean residence times of a subtropical barrier sand island.pdf",
    r"C:\Users\mhmda\Downloads\eng303\How water isotopes (18O, 2 H, 3 H) within an\How water isotopes (18O, 2 H, 3 H) within an.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Identifying the contribution of regional groundwater to the basef\Identifying the contribution of regional groundwater to the basef.pdf",

]

# Process multiple PDFs
process_multiple_pdfs(input_pdf_paths)
