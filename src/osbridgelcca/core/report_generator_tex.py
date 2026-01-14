import subprocess
from pathlib import Path

def generate_tex_report(results):
    latex_dir = Path("src/osbridgelcca/latex_template")

    base_tex = (latex_dir / "main.tex").read_text()

    # Inject values (example – I will map all fields properly next)
    base_tex = base_tex.replace(
        r"\newcommand{\TotalCost}{}",
        rf"\newcommand{{\TotalCost}}{{{results['total_cost']}}}"
    )

    base_tex = base_tex.replace(
        r"\newcommand{\EnergyCost}{}",
        rf"\newcommand{{\EnergyCost}}{{{results['energy_cost']}}}"
    )

    final_tex = latex_dir / "final.tex"
    final_tex.write_text(base_tex)

    subprocess.run(
        ["pdflatex", "final.tex"],
        cwd=latex_dir,
        check=True
    )
