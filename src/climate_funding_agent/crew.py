from crewai import Agent, Task, Crew

def build_crew():
    funding_researcher = Agent(
        role="Climate Funding Researcher",
        goal="Find relevant seed-stage climate funding opportunities",
        backstory="Expert in climate VC, grants, and impact investors",
        verbose=True
    )

    outreach_agent = Agent(
        role="Outreach Specialist",
        goal="Draft a compelling funding outreach email",
        backstory="Understands how investors evaluate early-stage climate startups",
        verbose=True
    )

    research_task = Task(
        description="Identify 3–5 relevant seed-stage climate funds and explain fit",
        agent=funding_researcher
    )

    email_task = Task(
        description="Draft a personalized intro email to one selected fund",
        agent=outreach_agent
    )

    return Crew(
        agents=[funding_researcher, outreach_agent],
        tasks=[research_task, email_task],
        verbose=True
    )
