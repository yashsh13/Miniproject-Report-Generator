import os
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

load_dotenv()

class LiteratureSurveyTable(BaseModel):
    sr_no: int = Field(..., description="Serial number of the paper")
    title: str = Field(..., description="Title of the research paper")
    authors: str = Field(..., description="Authors of the research paper")
    year: int = Field(..., description="Year of publication")
    summary: str = Field(..., description="Short summary of the paper in 30 words")

class Miniproject(BaseModel):
    
    title: str = Field(description="Title for the project in 2-3 words max")
    abstract: str = Field(description="Generate abstract for the mini project in 90-100 words in a single paragraph")
    introduction: List[str] = Field(description="Give 6 medium sized paragraphs for the introduction in a list")
    rows: List[LiteratureSurveyTable] = Field(description='Give 10 Literature Survey entries in a list')
    literature: List[str] = Field(description="Give a list of 10 people's contribution in research of this topic in medium size paragraphs from the literature survey")
    ps: str = Field(description="Generate Problem Statement for the mini project in 60-70 words in a single paragraph")
    objective_title: str = Field(description="Generate Objective heading for the mini project in 50-60 words in a single paragraph")
    objectives: List[str] = Field(description="List 5-6 Objectives for the project with atleast 30 words each")
    graphviz: str = Field(description="Generate detailed graphviz code to generate vertical flowchart for the implementation of this project")
    flowchartexplain: List[str] = Field(description="Give 4 medium sized paragraphs for the flowchart in a list")
    methodology: List[str] = Field(description="List 4 paragraphs explaining the methodolgy with atleast 60 words each")
    functional: str = Field(description="Give 1 paragraph explaning the functional requirements for the project in 70-80 words")
    nonfunctional: str = Field(description="Give 1 paragraph explaning the Non Functional requirements for the project in 60-70 words")
    design: List[str] = Field(description="List 2 medium sized paragraphs explaining the design model")
    implementation: List[str] = Field(description="List 2 medium sized paragraphs explaining the Implementation of the project")
    result: List[str] = Field(description="List 5 large paragraphs explaining the Result and Discussion of the project")
    conclusion: List[str] = Field(description="List 2 paragraph conclusion in 60+ words in each paragraph")
    fs: List[str] = Field(description="List 5-10 future scopes for the project")
    ref: List[str] = Field(description="List 5-10 refrences for the project")



parser = PydanticOutputParser(pydantic_object=Miniproject)

prompt = PromptTemplate(
            template="""You are a college Miniproject teacher expert in creating reports .
            Given a Miniproject idea, create a comprehensive report structure.
            
            Miniproject Idea: {idea}
            
            Please analyze this idea and create a structured report that would be compelling 
            foucs on:
            - Clear problem identification
            - Innovative solution approach
            - Technical feasibility
            - Literature Survey
            - Implementation roadmap

            DO NOT USE ANY SPECIAL CHARACTER LIKE *
            
            {format_instructions}
            
            Make sure your response is detailed, realistic, and formal for a college report.
            """,
            input_variables=["idea"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash', temperature=0.7)

chain = prompt | model | parser

def get_data(idea):

    data = chain.invoke({'idea':idea})

    return data