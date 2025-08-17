from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import requests
from generate import get_data

def create_report(idea):
    doc = DocxTemplate('template.docx')

    data = get_data(idea)


    url = 'https://quickchart.io/graphviz'
    params = {
        'graph':data.graphviz,
        'format':'png'
        }

    response = requests.get(url,params=params)

    with open('/tmp/flowchart.png','wb') as f:
        f.write(response.content)

    context = {
        'Title':data.title,
        'Abstract':data.abstract,
        'Introduction':data.introduction,
        'Literature':data.literature,
        'rows':data.rows,
        'ProblemStatement':data.ps,
        'ObjectiveTitle':data.objective_title,
        'Objectives':enumerate(data.objectives,start=1),
        'Flowchart':InlineImage(doc,'/tmp/flowchart.png'),
        'Flowchartexplain':data.flowchartexplain,
        'Methodology':data.methodology,
        'Functional':data.functional,
        'NonFunctional':data.nonfunctional,
        'Design':data.design,
        'Implementation':data.implementation,
        'Result_1':data.result[0],
        'Result_2':data.result[1],
        'Result_3':data.result[2],
        'Result_4':data.result[3],
        'Result_5':data.result[4],
        'Conclusion':data.conclusion,
        'Fs':enumerate(data.fs,start=1),
        'Ref':enumerate(data.ref,start=1)
        }

    doc.render(context)

    doc.save('/tmp/generated.docx')  