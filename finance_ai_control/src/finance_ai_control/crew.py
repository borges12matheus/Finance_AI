from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from finance_ai_control.tools import File_to_Text

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

text_extract_tool = File_to_Text()

@CrewBase
class Finance_Ai_Project():
	"""SummarizeDocsProject crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def finance_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['finance_analyst'],
			verbose=True,
			tools=[text_extract_tool],
		)

	@agent
	def trend_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['trend_researcher'],
			verbose=True
		)
  
	@agent
	def planning_consultant(self) -> Agent:
		return Agent(
			config=self.agents_config['planning_consultant'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['analysis_task'],
		)

	@task
	def context_task(self) -> Task:
		return Task(
			config=self.tasks_config['context_task'],
		)
  
	@task
	def plann_task(self) -> Task:
		return Task(
			config=self.tasks_config['plann_task'],
			output_file='analysis.md'
			)

	@crew
	def crew(self) -> Crew:
		"""Creates the SummarizeDocsProject crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
