from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from research_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import FileReadTool, TXTSearchTool, DallETool, CSVSearchTool


@CrewBase
class ResearchCrewCrew():
    """ResearchCrew crew"""
    agents_config = 'src/config/agents.yaml'
    tasks_config = 'src/config/tasks.yaml'


    # marketing info 
    @agent
    def researcher(self) -> Agent:
        # Define the tools you need
        file_read_tool = FileReadTool(file_path='./Data/marketing information.txt')
        semantic_search_tool = TXTSearchTool(txt='./Data/marketing information.txt')

        return Agent(
            # config=self.agents_config['researcher'],
            role = "Senior Data Researcher",
            goal = """
    Analyze the given data and give the needed information to the agents that need it for making the posts in different social media and emails
      The social medias are:
      X.com,
      Instagram
      Treads
      facebook
      and also
      email newsletter special other emails
""",    
            backstory="""You're a seasoned researcher with a knack for analyzing data. Known for your ability to find the most relevant
      information and present it in a clear and concise manner.""",
            tools=[file_read_tool, semantic_search_tool],  # Include the tools here
            verbose=True
        )
    @task
    def research_task(self) -> Task:
        return Task(
           # config=self.tasks_config['research_task'],
            description = "Conduct a thorough research on the given marketing data"
            "Make sure you find any interesting and relevant information that can be used to make interesting social media post or email newsletter"
            " Facebook, Instagram, X.com, Threads and email newsletters - these are the platforms that we will use for social media",
            expected_output = "Detailed information about topics that can be used as material for posts or email newsletters",
            agent=self.researcher()
        )
    



    # trends
    @agent
    def trend_researcher(self) -> Agent:
        web_search_tool = CSVSearchTool()  # To find current trends online
        output_file_tool = FileReadTool(file_path='./Data/research_results.txt')

        return Agent(
            name="Trend Researcher",
            role="Trend Researcher",
            description="Analyzes the latest social media trends to gather raw data on popular platforms like Facebook, Instagram, X.com, Threads, and email newsletters.",
            personality="Detail-oriented and curious. Always looks for the most accurate and updated information.",
            goals=[
                "Find the most relevant and recent social media trends.",
                "Identify popular tags and viral post strategies.",
                "Present findings in a structured way for further analysis."
            ],
            goal="Analyze the latest social media trends to gather raw data on popular platforms.",
            backstory="Detail-oriented and curious. Always looks for the most accurate and updated information.",

            tools=[web_search_tool, output_file_tool],
            verbose=True
        )

    @agent
    def trend_analyst(self) -> Agent:
        file_read_tool = FileReadTool(file_path='./Data/research_results.txt')

        
        return Agent(
            name="Trend Analyst",
            role="Trend Analyst",
            goal="Analyze current social media trends to provide actionable insights.",
            backstory="You are an expert in social media analytics with a deep understanding of platform dynamics and user engagement strategies.",
            description="Reviews and analyzes the collected data to produce clear and actionable reports about social media trends.",
            personality="Analytical and precise, with a strong ability to interpret data and extract key insights.",
            goals=[
                "Summarize and interpret social media trends effectively.",
                "Highlight key strategies for creating viral content on each platform.",
                "Provide actionable insights based on current trends."
            ],
            tools=[file_read_tool],
            verbose=True
        )
    @task
    def trend_analys_task(self) -> Task:
        return Task(
            name="Trend Analysis Task",
        description=(
            "Conduct a thorough research about trends in social media now. "
            "Make sure to find any important information about how to make viral posts on Facebook, Instagram, X.com, Threads, and email newsletters. "
            "Include popular tags where relevant."
        ),
        expected_output=(
            "A list of points about the different platforms with 10 bullet points of the most relevant information about the trends on the given platform."
        ),
        input_format="text",
        output_format="structured_list",
            agent=self.trend_researcher()  # Uses the researcher to gather data
        )
    @task
    def trend_analysis_task(self) -> Task:
        return Task(
            role='Trend Analyst',
            goal='Analyze current social media trends to provide actionable insights.',
            backstory='You are an expert in social media analytics with a deep understanding of platform dynamics and user engagement strategies.',
             description=(
            "Conduct a thorough research about trends in social media now. "
            "Make sure to find any important information about how to make viral posts on Facebook, "
            "Instagram, X.com, Threads, and email newsletters. Include popular tags where relevant."
            ),
            expected_output=(
                "A list of points about the different platforms with 10 bullet points of the most relevant information about the trends on the given platform."
            ),
            tools=[CSVSearchTool(), FileReadTool()],
        
            agent=self.trend_analyst()  # Uses the trend_analyst to analyze data
        )



    # Intagram agents setup
    @agent
    def instagram_supervisor_agent(self) -> Agent:
        return Agent(
            # config=self.agents_config['instagram_supervisor_agent'],
            role="You are a coordinator, managing the process of creating effective Instagram posts.",
            goal="Review trend and research data, guide the writer, editor, and image prompt agent to create high-quality Instagram content.",
            backstory="You have experience in managing creative teams and ensuring content aligns with marketing goals.",
            verbose=True
        )

    @agent
    def instagram_writer_agent(self) -> Agent:
        return Agent(
            # config=self.agents_config['instagram_writer_agent'],
            role="You are a creative writer responsible for drafting engaging Instagram posts.",
            goal="Write captivating Instagram posts based on the given research and trends. "
            "Ensure the language suits the target audience and platform.",
            backstory="You have experience in writing marketing content for social media.",
            verbose=True
        )

    @agent
    def instagram_editor_agent(self) -> Agent:
        return Agent(
            # config=self.agents_config['instagram_editor_agent'],
            role="You are a meticulous editor, reviewing content for clarity, accuracy, and adherence to the brand's voice.",
            goal="Ensure the Instagram post meets quality standards and effectively communicates the intended message.",
            backstory="You are experienced in editing social media content, optimizing it for maximum engagement.",
            verbose=True
        )

    @agent
    def instagram_image_prompt_agent(self) -> Agent:
        dalle_tool = DallETool(
            model="dall-e-3",
            size="1024x1024",
            quality="standard",
            n=1
        )   
        return Agent(
            # config=self.agents_config['instagram_image_prompt_agent'],
            role="You are a creative visual specialist who generates effective prompts for DALL-E 3.",
            goal="Create detailed, professional prompts for generating Instagram images that align with the post content.",
            backstory="You understand how to create prompts that yield visually appealing and relevant images for social media.",
            tools=[dalle_tool],
            verbose=True
        )

    # Instagram tools tasks setup
    @task
    def instagram_supervise_task(self) -> Task:
        return Task(
            # config=self.tasks_config['instagram_supervise_task'],
            description="Coordinate the process of creating an Instagram post. Review research data, guide the writer and editor, "
            "and ensure the final post is suitable for publication.",
            expected_output="An organized post-creation process with a high-quality, approved Instagram post and an image prompt for DALL-E 3.",
            agent=self.instagram_supervisor_agent()
        )

    @task
    def instagram_write_post_task(self) -> Task:
        return Task(
            # config=self.tasks_config['instagram_write_post_task'],
            description="Draft an engaging Instagram post based on the provided research and trend data.",
            expected_output="A well-written Instagram post draft that aligns with the marketing strategy.",
            agent=self.instagram_writer_agent()
        )

    @task
    def instagram_edit_post_task(self) -> Task:
        return Task(
            # config=self.tasks_config['instagram_edit_post_task'],
            description="Review the post draft for errors, brand consistency, and platform suitability."
            "Provide feedback or approve for the final stage.",
            agent=self.instagram_editor_agent()
        )

    @task
    def instagram_generate_image_prompt_task(self) -> Task:
        return Task(
            # config=self.tasks_config['instagram_generate_image_prompt_task'],
            description="Create a detailed prompt for DALL-E 3 to generate an Instagram-worthy image. "
            "Align the image prompt with the finalized post content.",
            expected_output="A prompt that generates a visually appealing, context-appropriate image (1024x1024) for Instagram.",
            agent=self.instagram_image_prompt_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            # process=Process.sequential,
            verbose=2,
            process=Process.hierarchical, # Uncomment to use hierarchical process
        )