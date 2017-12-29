import subprocess
from source.Hello import run

# download https://github.com/pkubowicz/opendetex

latex_file = "/home/felix/Thesis/Thesis/chapters/chapter2.tex"
txt_file = "/tmp/text_latex.txt"
subprocess.call("detex " + latex_file + " > " + txt_file, shell=True)

run(txt_file)