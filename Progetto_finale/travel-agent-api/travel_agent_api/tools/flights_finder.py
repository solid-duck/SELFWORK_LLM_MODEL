from langchain_core.tools import tool
from pydantic import BaseModel, Field
from serpapi import GoogleSearch
import os

class FlightsInputSchema(BaseModel):
    departure_airport: str = Field(description="Codice IATA dell'aeroporto di partenza (es. FCO)")
    arrival_airport: str = Field(description="Codice IATA dell'aeroporto di arrivo (es. JFK)")
    outbound_date: str = Field(description="Data di partenza nel formato YYYY-MM-DD")

@tool(args_schema=FlightsInputSchema)
def flights_finder(departure_airport: str, arrival_airport: str, outbound_date: str) -> str:
    """Cerca i voli disponibili utilizzando SerpApi in base all'aeroporto di partenza, di arrivo e alla data."""
    api_key = os.getenv("SERPAPI_API_KEY")
    params = {
        "engine": "google_flights",
        "departure_id": departure_airport,
        "arrival_id": arrival_airport,
        "outbound_date": outbound_date,
        "api_key": api_key,
        "hl": "it",
        "currency": "EUR"
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
    best_flights = results.get("best_flights", [])
    if not best_flights:
        return "Nessun volo trovato per i parametri specificati."
        
    return str(best_flights[:3])