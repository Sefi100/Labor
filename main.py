from importnb import imports
import matplotlib.pyplot as plt
import numpy as np
import os
import nbconvert
import nbformat as nbf



def pdfconvert(path, title, name):
    # exporter = nbconvert.TemplateExporter(exclude_input=True)
    #exporter = nbconvert.PDFExporter(exclude_input=True)
    #nbconvert.export(exporter, path)
    dt = nbf.read(path, nbf.NO_CONVERT)
    dt.metadata.update({'title': title})
    dt.metadata.update({'authors': [{'name': name[0]}, {'name': name[1]}]})
    nbf.write(dt, path, nbf.NO_CONVERT)
    os.system(f"jupyter nbconvert --to pdf --TemplateExporter.exclude_input=True {path}")


if __name__ == '__main__':
    # dir_path = os.getcwd() + "\\Kisfeny\\Kisfeny.ipynb"
    dir_path = "C:\\Users\\schba\\PycharmProjects\\Ellab\\Hallab2\\Hőmérsékletisugárzás\\Homsug.ipynb"
    pdfconvert(dir_path, "Hőmérsékleti Sugárzás Vizsgálata", ["Györgyfalvai Fanni", "Schäffer Bálint"])
