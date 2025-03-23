#!/usr/bin/env python
from research_crew.crew import ResearchCrewCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    ResearchCrewCrew().crew().kickoff(inputs=inputs)