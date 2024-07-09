from langchain.tools import tool
from langchain_community.llms import Ollama
from crewai import Agent

llm = Ollama("llama3") 
class MathTools(): 
    
    @tool("Make a calculation")
    def calculate(operation): 
        """
            This tool takes in a 
            expresion and then evaluates 
            the value and returns it
        """

        try:
            return eval(operation)
        except SyntaxError: 
            return "Error : There was a SyntaxError in your expression"

class Agents(): 

    def MathAgent(): 

        return Agent(
            role="calculate math expresions",
            goal="use calculate tool inorder to calculate the value of an expression"
            backstory="You are an expert in math",
            verbose=True,
            tools=[MathTools()],
            llm=llm)
