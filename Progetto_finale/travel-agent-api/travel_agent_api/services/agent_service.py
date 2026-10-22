from datetime import datetime
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from travel_agent_api.tools.flights_finder import flights_finder
from travel_agent_api.tools.hotels_finder import hotels_finder
from travel_agent_api.tools.chain_historical_expert import chain_historical_expert
from travel_agent_api.tools.chain_travel_plan import chain_travel_plan

FLIGHTS_OUTPUT = """
Format: markdown
## Miglior Opzione
### Andata:
Compagnia aerea: Ryanair
Data di partenza: 2024-12-13
Ora di partenza: 10:00
Durata del volo: 1h 30m
### Ritorno:
Compagnia aerea: Ryanair
Data di ritorno: 2024-12-19
Ora di ritorno: 14:30
Durata del volo: 1h 30m
Inserisci il link di Google per la prenotazione se possibile.
#### Altri opzioni disponibili:
Compagnia aerea: Ryanair
Data di partenza: 2024-12-13
Ora di partenza: 10:00
Durata del volo: 1h 30m
"""

HOTELS_OUTPUT = """
Format: markdown
#### Hotel 1
Inserisci la foto dell'hotel se disponibile.
- Descrizione: Camere e suite eleganti, a volte con vista sulla città.
- Prezzo per notte: €260
- Prezzo totale: €2,336
- Check-in: 15:00, Check-out: 12:00
- Valutazione complessiva: 4.5 su 5
- Servizi Inclusi: Spa, Piscina, Parcheggio gratuito
"""

TRAVEL_PLAN_OUTPUT = """
Format: markdown
### Itinerario:
### Giorno 1 - 2024-12-13:
- Mattina: Descrizione dell'attività
- Pomeriggio: Descrizione dell'attività
- Sera: Descrizione dell'attività
"""

class Agent:
    def __init__(self):
        self.current_datetime = datetime.now()
        self.model = ChatOpenAI(model_name="gpt-4o")
        self.tools = [
            chain_historical_expert,
            flights_finder,
            hotels_finder,
            chain_travel_plan,
        ]
        self.agent_executor = create_react_agent(self.model, self.tools)

    def run(self, messages: list):
        SYSTEM_PROMPT = (
            "Sei un travel planner. Il tuo compito è organizzare il viaggio per l'utente.\n"
            "Aggiungi delle emojis per rendere il tuo output piu' interessante.\n"
            f"La data di oggi è {self.current_datetime}.\n"
            "Usa le seguenti istruzioni per creare un output:\n"
            f"Esempio Output Voli:\n{FLIGHTS_OUTPUT}\n"
            f"Esempio Output Hotel:\n{HOTELS_OUTPUT}\n"
            f"Esempio di Output Viaggio:\n{TRAVEL_PLAN_OUTPUT}"
        )
        
        conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
        
        response = self.agent_executor.invoke({"messages": conversation_history})
        
        print(" " * 80)
        print("chat_completion")
        print("*" * 80)
        
        last_message = response["messages"][-1]
        return last_message.content