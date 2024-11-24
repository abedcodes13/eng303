import tabula
pdf_path = "Analysis of environmental isotopes in groundwater to understand\Analysis of environmental isotopes in groundwater to understand.pdf"

tables = tabula.read_pdf(pdf_path, pages="6" , multiple_tables=True, lattice=False, stream= True)

print (tables)
# Iterate over the tables and export them to CSV
for i, table in enumerate(tables):
    # Print the table
    print(f'Table {i}:')
    print(table)
    
    # Export the table to CSV
    table.to_csv(f'Analysis of environmental isotopes in groundwater to understand/table{i}.csv', index=False, encoding='utf-8-sig')

