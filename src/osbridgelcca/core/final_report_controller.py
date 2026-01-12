"""
Final controller to generate LCCA report
Triggered from ResultsWidget
"""

from osbridgelcca.core.bridge_lcc import BridgeLCC
from osbridgelcca.core.report_generator_tex import generate_tex_report
from osbridgelcca.core.input_data import Input


def generate_final_report(project_input: Input):
    """
    Generate final LCCA report.

    Parameters
    ----------
    project_input : Input
        Fully constructed Input object from module widgets
    """

    # -----------------------------
    # STEP 1: RUN LCCA CALCULATION
    # -----------------------------
    lcc_engine = BridgeLCC(project_input)
    results = lcc_engine.calculate_lcc()

    # -----------------------------
    # STEP 2: GENERATE LATEX REPORT
    # -----------------------------
    generate_tex_report(results)

    print("✅ Final LCCA Report generated successfully")
