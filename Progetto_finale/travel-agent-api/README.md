# Travel Agent API - Un Assistente di Viaggio Intelligente

**Travel Agent API** è un'applicazione backend sviluppata con **FastAPI**, **LangChain**, **LangGraph** e modelli di linguaggio avanzati (OpenAI GPT-4). L'applicazione fornisce un'interfaccia conversazionale intelligente capable di gestire la ricerca di voli e hotel, la generazione di itinerari su misura e l'approfondimento di informazioni storiche e culturali sulle destinazioni.

---

## 1. Caratteristiche Principali

1. **Ricerca Intelligente di Voli**: Integrazione con l'API di Google Flights tramite SerpApi per il confronto di prezzi, date e compagnie aeree.
2. **Ricerca Hotel**: Integrazione con l'API di Google Hotels tramite SerpApi per filtrare strutture ricettive per valutazione, servizi e prezzo.
3. **Pianificazione Itinerari**: Generazione di piani di viaggio personalizzati suddivisi per giornate e fasce orarie (mattina, pomeriggio, sera).
4. **Informazioni Storiche e Culturali**: Modello AI specializzato come guida e storico locale per arricchire l'esperienza di viaggio.

---

## 2. Tecnologie e Architettura

- **Python (>=3.9, <4.0)**: Linguaggio di programmazione principale.
- **FastAPI & Uvicorn**: Framework web moderno e server ASGI per la gestione delle API RESTful.
- **LangChain & LangGraph**: Orchestrazione dei modelli di linguaggio e creazione dell'agente conversazionale (architettura ReAct).
- **OpenAI GPT-4**: Modello LLM per la comprensione del testo e l'elaborazione delle risposte.
- **SerpApi**: API per la ricerca in tempo reale di voli e hotel.
- **Pydantic**: Validazione rigorosa dei dati di input/output.
- **Poetry**: Gestione delle dipendenze e dell'ambiente virtuale.

---

## 3. Struttura del Progetto

```text
travel-agent-api/
│
├── travel_agent_api/
│   ├── __init__.py
│   ├── main.py                     # Punto di ingresso dell'applicazione e configurazione CORS
│   ├── routes/
│   │   ├── __init__.py
│   │   └── chat_router.py          # Gestione delle rotte API per la chat (/chat/travel-agent)
│   ├── services/
│   │   ├── __init__.py
│   │   └── agent_service.py        # Orchestrazione dell'Agente e gestione del ReAct Agent
│   └── tools/
│       ├── __init__.py
│       ├── flights_finder.py       # Tool per la ricerca voli tramite SerpApi
│       ├── hotels_finder.py        # Tool per la ricerca hotel tramite SerpApi
│       ├── chain_travel_plan.py    # Tool per la generazione degli itinerari
│       └── chain_historical_expert.py # Tool per le informazioni storiche
│
├── .env.example                    # Template per le variabili d'ambiente
├── .gitignore                      # Esclusione file sensibili e temporanei
├── pyproject.toml                  # Configurazione delle dipendenze Poetry
├── poetry.lock                     # Lock file delle dipendenze
└── README.md                       # Documentazione del progetto
```

---

## 4. Installazione e Configurazione

### 4.1 Prerequisiti
Assicurati di avere installato Python e Poetry sul tuo sistema.

### 4.2 Clonazione e Installazione Dipendenze
1. Clona la repository ed entra nella cartella principale del progetto:
   ```bash
   cd travel-agent-api
   ```
2. Installa tutte le dipendenze necessarie utilizzando Poetry:
   ```bash
   poetry install
   ```

### 4.3 Configurazione delle Variabili d'Ambiente
1. Crea una copia del file `.env.example` denominandola `.env`:
   ```bash
   cp .env.example .env
   ```
2. Inserisci le tue chiavi API all'interno del file `.env`:
   ```env
   OPENAI_API_KEY="la_tua_openai_api_key"
   SERPAPI_API_KEY="la_tua_serpapi_api_key"
   ```

---

## 5. Avvio del Server

Per avviare il server backend di sviluppo, esegui il seguente comando:

```bash
poetry run uvicorn travel_agent_api.main:app --reload --port 8080
```

Il server sarà accessibile all'indirizzo `http://127.0.0.1:8080`.

---

## 6. Utilizzo e Test dell'API

### 6.1 Interfaccia Swagger (Documentazione Interattiva)
Apri il browser e naviga all'indirizzo:
```text
http://127.0.0.1:8080/docs
```

Da qui puoi testare direttamente l'endpoint `POST /chat/travel-agent`.

### 6.2 Esempio di Richiesta (JSON)

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Vorrei organizzare un viaggio a Parigi dal 2024-12-13 al 2024-12-19"
    }
  ]
}
```

### 6.3 Esempi di Prompt da Testare

- **Esperto Storico**: `"Raccontami la storia del Rinascimento a Firenze, in particolare il ruolo della famiglia Medici."`
- **Pianificazione Viaggio**: `"Vorrei organizzare un viaggio a Venezia dal 15 al 20 giugno 2024 per due persone con un budget di 2000€."`
- **Ricerca Voli**: `"Cerco voli da FCO a CDG per due adulti dal 13 al 19 dicembre 2024."`
- **Ricerca Hotel**: `"Cerco un hotel 4 stelle nel centro di Roma per due adulti dal 15 al 20 maggio 2024."`

---

## 7. Integrazione Client (Laravel Web Client)

L'API è predisposta con supporto **CORS** per comunicare con un'interfaccia frontend Laravel (es. `http://localhost:8000`).

Per avviare il client Laravel (dalla cartella `web_travel-agent`):
```bash
composer install
npm install
npm run dev
php artisan serve
```