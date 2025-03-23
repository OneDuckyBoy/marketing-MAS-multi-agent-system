from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from research_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ResearchCrewCrew():
    """ResearchCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    # marketing info 
    @agent
    def researcher(self) -> Agent:
        # Define the tools you need
        file_read_tool = FileReadTool(file_path='./Data/marketing information.txt')
        semantic_search_tool = TXTSearchTool(txt='./Data/marketing information.txt')

        return Agent(
            config=self.agents_config['researcher'],
            tools=[file_read_tool, semantic_search_tool],  # Include the tools here
            verbose=True
        )
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )
    



    # trends
    @agent
    def trend_researcher(self) -> Agent:
        web_search_tool = WebSearchTool()  # To find current trends online
        output_file_tool = OutputFileTool(file_path='./Data/research_results.txt')

        return Agent(
            config=self.agents_config['trend_researcher'],
            tools=[web_search_tool, output_file_tool],
            verbose=True
        )

    @agent
    def trend_analyst(self) -> Agent:
        file_read_tool = FileReadTool(file_path='./Data/research_results.txt')
        text_processing_tool = TextProcessingTool()  # For summarizing data

        return Agent(
            config=self.agents_config['trend_analyst'],
            tools=[file_read_tool, text_processing_tool],
            verbose=True
        )
    @task
    def trend_analys_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_analys_task'],
            agent=self.trend_researcher()  # Uses the researcher to gather data
        )
    @task
    def trend_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_analysis_task'],
            agent=self.trend_analyst()  # Uses the trend_analyst to analyze data
        )





    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            process=Process.hierarchical, # Uncomment to use hierarchical process
        )
    # @agent
    # def researcher(self) -> Agent:
    #     # Define the tools you need : )
    #     file_read_tool = FileReadTool(file_path='./Data/marketing information.txt')
    #     semantic_search_tool = TXTSearchTool(txt='./Data/marketing information.txt')

    #     return Agent(
    #         config=self.agents_config['researcher'],
    #         tools=[file_read_tool, semantic_search_tool],  # Include the tools here
    #         verbose=True
    #     )

    # @task
    # def research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['research_task'],
    #         agent=self.researcher()
    #     )
    

    # @agent
    # def trend_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['trend_analyst'],
    #         verbose=True
    #     )
    # @agent
    # def reporting_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reporting_analyst'],
    #         verbose=True
    #     )
    

    

    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reporting_task'],
    #         agent=self.reporting_analyst(),
    #         output_file='report.md'
    #     )

    