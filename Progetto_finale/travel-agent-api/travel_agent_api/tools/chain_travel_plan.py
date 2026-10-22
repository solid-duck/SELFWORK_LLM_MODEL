from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser

class TravelPlanInput(BaseModel):
    start_date: str = Field(description="The start date of the trip (YYYY-MM-DD)")
    end_date: str = Field(description="The end date of the trip (YYYY-MM-DD)")
    destination: str = Field(description="The destination of the trip.")
    adults: Optional[int] = Field(1, description="The number of adults.")
    children: Optional[int] = Field(0, description="The number of children.")
    travel_style: str = Field(description="The style of travel.")
    budget: Optional[int] = Field(description="The total budget.")
    activities: str = Field(description="The preferred activities.")
    food_restriction: str = Field(description="Any food restrictions.")

class TravelPlanInputSchema(BaseModel):
    params: TravelPlanInput

class TravelDayOutput(BaseModel):
    morning: str = Field(description="The activities for the morning.")
    afternoon: str = Field(description="The activities for the afternoon.")
    evening: str = Field(description="The activities for the evening.")

class TravelPlanOutput(BaseModel):
    travel_plan: List[TravelDayOutput]

@tool(args_schema=TravelPlanInputSchema)
def chain_travel_plan(params: TravelPlanInput) -> TravelPlanOutput:
    """Genera un piano di viaggio dettagliato strutturato giorno per giorno in base alle preferenze fornite."""
    model = ChatOpenAI(model_name="gpt-4o")
    
    system_prompt = (
        f"Sei un esperto di viaggi.\n"
        f"La data di inizio è {params.start_date}.\n"
        f"La data di fine è {params.end_date}.\n"
        f"La destinazione è {params.destination}.\n"
        f"Adulti: {params.adults}, Bambini: {params.children}.\n"
        f"Stile di viaggio: {params.travel_style}.\n"
        f"Budget: {params.budget}.\n"
        f"Attività preferite: {params.activities}.\n"
        f"Restrizioni alimentari: {params.food_restriction}.\n"
        f"Usa le emoji e sii amichevole."
    )
    
    prompt = ChatPromptTemplate([("human", "{input}")])
    output_parser = PydanticOutputParser(pydantic_object=TravelPlanOutput)
    
    chain = prompt | model | output_parser
    
    result = chain.invoke({"input": system_prompt})
    
    print(" " * 80)
    print("chain_travel_plan")
    print("*" * 80)
    
    return result