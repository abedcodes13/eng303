import camelot
import os

def process_multiple_pdfs(input_pdf_paths):
    for input_pdf_path in input_pdf_paths:
        # Extract directory and base filename
        directory, filename = os.path.split(input_pdf_path)
        base_filename, ext = os.path.splitext(filename)

        # Read the PDF using Camelot's stream method
        print(f"Processing {input_pdf_path}...")
        tables = camelot.read_pdf(input_pdf_path, pages='all', flavor='stream', flag_size=True)

        if len(tables) > 0:
            # Export all extracted tables to CSV
            output_csv_path = os.path.join(directory, 'tables.csv')
            tables.export(output_csv_path, f='csv')
            print(f"Tables exported to: {output_csv_path}")
        else:
            print(f"No tables found in {input_pdf_path}.")

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
    r"C:\Users\mhmda\Downloads\eng303\Integrating major ion geochemistry\Integrating major ion geochemistry.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Island groundwater resources, impacts of abstraction and a drying\Island groundwater resources, impacts of abstraction and a drying.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Lithium and strontium isotope dynamics in a carbonate island aquifer\Lithium and strontium isotope dynamics in a carbonate island aquifer.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Marine water from mid-Holocene sea level highstand\Marine water from mid-Holocene sea level highstand.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Mean transit times in headwater catchments\Mean transit times in headwater catchments.pdf",
    r"C:\Users\mhmda\Downloads\eng303\River infiltration to a subtropical alluvial\River infiltration to a subtropical alluvial.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Sources and mean transit times of intermittent streamflow in semi-arid\Sources and mean transit times of intermittent streamflow in semi-arid.pdf",
    r"C:\Users\mhmda\Downloads\eng303\The evolution of stable silicon isotopes in a coastal carbonate aquifer\The evolution of stable silicon isotopes in a coastal carbonate aquifer.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Transit times from rainfall to baseflow in headwater catchments estimated using tritium\Transit times from rainfall to baseflow.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Assessing the controls and uncertainties on mean transit times in\Assessing the controls and uncertainties on mean transit times in.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Analysis of environmental isotopes in groundwater to understand\Analysis of environmental isotopes in groundwater to understand.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using 14C and 3 H to delineate a recharge ‘window’ into the Perth Basin aquifers\Using 14C and 3 H to delineate a recharge ‘window’ into the Perth Basin aquifers.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using geochemistry to understand water sources and transit times\Using geochemistry to understand water sources and transit times.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using groundwater geochemistry and environmental isotopes to assess\Using groundwater geochemistry and environmental isotopes to assess.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using hydrogeochemistry to understand inter-aquifer mixing/Using hydrogeochemistry to understand inter-aquifer mixing.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using multiple lines of evidence to map groundwater recharge in a rapidly/Using multiple lines of evidence to map groundwater recharge in a rapidly.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using multiple methods to investigate the effects of land-use\Using multiple methods to investigate the effects of land-use.pdf",
    r"C:\Users\mhmda\Downloads\eng303\Using tritium to document the mean transit time and sources\Using tritium to document the mean transit time and sources.pdf",
    r"C:\Users\mhmda\Downloads\eng303\On the hydrology of the bauxite oases\On the hydrology of the bauxite oases.pdf",
]


# Process multiple PDFs
process_multiple_pdfs(input_pdf_paths)
