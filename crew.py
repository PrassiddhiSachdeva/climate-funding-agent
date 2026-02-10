from crewai import Agent, Task, Crew, crew

@crew
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
        description="""
        Given a climate startup description, identify 3–5 relevant
        seed-stage funds or grant programs and explain why they fit.
        """,
        agent=funding_researcher
    )

    email_task = Task(
        description="""
        Choose one fund and draft a short personalized intro email
        requesting a funding conversation.
        """,
        agent=outreach_agent
    )

    return Crew(
        agents=[funding_researcher, outreach_agent],
        tasks=[research_task, email_task],
        verbose=True
    )
