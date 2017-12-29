import subprocess
from source.Hello import run

# download https://github.com/euske/pdfminer

pdf_file = "/home/felix/paperit/pdf/test.pdf"
txt_file = "/tmp/text_pdf.txt"
subprocess.call("python /home/felix/Software/pdfminer/tools/pdf2txt.py -c 'ascii' -t text -o " + txt_file + " " + pdf_file, shell=True)

run(txt_file)