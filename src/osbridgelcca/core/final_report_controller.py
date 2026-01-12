from core.calculation_service import calculate_all_modules
from core.report_generator_tex import generate_tex_report
from db.database import Database

def generate_final_report():
    db = Database()

    # 1. Fetch all module data from DB
    energy_data = db.fetch("energy_module")
    transport_data = db.fetch("transport_module")
    material_data = db.fetch("material_module")
    waste_data = db.fetch("waste_module")

    # 2. Run existing calculations (already written in your project)
    results = calculate_all_modules(
        energy_data=energy_data,
        transport_data=transport_data,
        material_data=material_data,
        waste_data=waste_data
    )

    # 3. Generate PDF using Overleaf LaTeX + TinyTeX
    generate_tex_report(results)
