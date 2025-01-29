from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BlogWriterAgent():
	"""BlogWriterAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def topic_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['topic_generator'],
			verbose=True
		)

	@agent
	def topic_selector(self) -> Agent:
		return Agent(
			config=self.agents_config['topic_selector'],
			verbose=True
		)
	
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)
	
	@agent
	def content_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['content_creator'],
			verbose=True
		)
	
	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_writer'],
			verbose=True
		)

	@task
	def topic_generator_task(self) -> Task:
		return Task(
			config=self.tasks_config['topic_generator_task'],
		)

	@task
	def topic_selector_task(self) -> Task:
		return Task(
			config=self.tasks_config['topic_selector_task'],
		)
	
	@task
	def researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['researcher_task'],
		)
	
	@task
	def content_creator_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_creator_task'],
		)
	
	@task
	def blog_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['blog_writer_task'],
			output_file='blog.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BlogWriterAgent crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # Uncomment this line to run the crew in hierarchical mode
		)
