from crewai import Crew
from crew import funding_researcher, outreach_agent, research_task, email_task

def run():
    crew = Crew(
        agents=[funding_researcher, outreach_agent],
        tasks=[research_task, email_task],
        verbose=True
    )

    crew.kickoff(
        inputs={
            "startup_description": "Seed-stage climate startup building carbon accounting software for Indian MSMEs"
        }
    )

if __name__ == "__main__":
    run()
