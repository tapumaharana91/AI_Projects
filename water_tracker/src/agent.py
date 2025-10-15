import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(groq_api_key=groq_api_key,
             model='llama-3.3-70b-versatile',
             temperature=0.7)

class waterIntakeAgent:
    def __init__(self):
        self.history = []
    
    def analyze_intake(self, intake_ml):

        prompt = f"""
        You are a Hydration assistant. The user has consumed {intake_ml} ml of water today.
        Provide a hydration status and suggest if they need to drink more water.
        """
        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content
    
if __name__ == "__main__":
    agent = waterIntakeAgent()
    intake = 1500  # Example intake in ml
    feedback = agent.analyze_intake(intake)
    print(f"Hydration Feedback: {feedback}")