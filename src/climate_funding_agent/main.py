from climate_funding_agent.crew import build_crew

def run():
    crew = build_crew()
    crew.kickoff(
        inputs={
            "startup_description": "Seed-stage climate startup building carbon accounting software for Indian MSMEs"
        }
    )

if __name__ == "__main__":
    run()
