from crewai import Agent, Task, Crew

def climate_funding_crew():
    funding_researcher = Agent(
        role="Climate Funding Researcher",
        goal="Find relevant seed-stage climate funding opportunities",
        backstory="Expert in climate venture capital, grants, and impact investors",
        verbose=True
    )

    outreach_agent = Agent(
        role="Outreach Specialist",
        goal="Draft a clear and compelling funding outreach email",
        backstory="Understands how founders pitch and how investors evaluate deals",
        verbose=True
    )

    research_task = Task(
        description="Identify 3–5 relevant seed-stage climate funds or grants.",
        agent=funding_researcher
    )

    email_task = Task(
        description="Draft a short personalized intro email.",
        agent=outreach_agent
    )

    return Crew(
        agents=[funding_researcher, outreach_agent],
        tasks=[research_task, email_task],
        verbose=True
    )
