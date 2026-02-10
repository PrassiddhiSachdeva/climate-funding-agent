from climate_funding_agent.crew import climate_funding_crew

def run():
    crew = climate_funding_crew()
    crew.kickoff(
        inputs={
            "startup_description": "Seed-stage climate startup"
        }
    )

if __name__ == "__main__":
    run()
