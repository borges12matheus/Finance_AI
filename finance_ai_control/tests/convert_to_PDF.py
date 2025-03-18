import pypandoc

def convert_to_pdf(md_file):
    pdf_file = pypandoc.convert_file(md_file, 'pdf', outputfile="teste.pdf")
    print(pdf_file)
    
convert_to_pdf(md_file = r"D:\Data Science\CrewAi\Finance AI Project\finance_ai_control\analysis.md")    