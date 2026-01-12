"""
Final controller to generate LCCA report
Triggered from ResultsWidget
"""

from osbridgelcca.core.bridge_lcc import BridgeLCC
from osbridgelcca.core.report_generator_tex import generate_tex_report
from osbridgelcca.core.input_data import InputData


def generate_final_report():
    """
    1. Load saved input data
    2. Run Bridge LCC calculations
    3. Generate LaTeX PDF report
    """

    # -----------------------------
    # STEP 1: LOAD INPUT DATA
    # -----------------------------
    input_data = InputData()
    input_data.load()   # uses your existing persistence logic

    # -----------------------------
    # STEP 2: RUN LCCA CALCULATION
    # -----------------------------
    lcc_engine = BridgeLCC(input_data)
    results = lcc_engine.calculate_lcc()

    # -----------------------------
    # STEP 3: GENERATE LATEX REPORT
    # -----------------------------
    generate_tex_report(results)

    print("✅ Final LCCA Report generated successfully")
