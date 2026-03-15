from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context

study_planner_agent_google_search_agent = LlmAgent(
  name='Study_Planner_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
study_planner_agent_url_context_agent = LlmAgent(
  name='Study_Planner_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
study_planner_agent = LlmAgent(
  name='study_planner_agent',
  model='gemini-2.5-flash',
  description=(
      'Schedule study sessions based on assignments, exams, and user availability.'
  ),
  sub_agents=[],
  instruction='- Receive list of assignments, exams, and preferred study hours.\n- Calculate optimal study blocks avoiding conflicts.\n- Suggest study sessions with start/end times.\n- Provide reasoning logs explaining why each session is scheduled.',
  tools=[
    agent_tool.AgentTool(agent=study_planner_agent_google_search_agent),
    agent_tool.AgentTool(agent=study_planner_agent_url_context_agent)
  ],
)
entertainment_planner_agent_google_search_agent = LlmAgent(
  name='Entertainment_Planner_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
entertainment_planner_agent_url_context_agent = LlmAgent(
  name='Entertainment_Planner_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
entertainment_planner_agent = LlmAgent(
  name='entertainment_planner_agent',
  model='gemini-2.5-flash',
  description=(
      'Decide whether user should do indoor or outdoor activities and delegate to corresponding agent.'
  ),
  sub_agents=[],
  instruction='- Receive user preferences for entertainment.\n- Decide if indoor or outdoor activity is better for each time slot.\n- Delegate to Indoor Agent or Outdoor Agent accordingly.\n- Return suggested activity + reasoning logs.',
  tools=[
    agent_tool.AgentTool(agent=entertainment_planner_agent_google_search_agent),
    agent_tool.AgentTool(agent=entertainment_planner_agent_url_context_agent)
  ],
)
indoor_entertainment_agent_google_search_agent = LlmAgent(
  name='Indoor_Entertainment_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
indoor_entertainment_agent_url_context_agent = LlmAgent(
  name='Indoor_Entertainment_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
indoor_entertainment_agent = LlmAgent(
  name='indoor_entertainment_agent',
  model='gemini-2.5-flash',
  description=(
      'Suggest indoor activities like reading, gaming, or hobbies based on user preferences.'
  ),
  sub_agents=[],
  instruction='- Receive available time slots from Entertainment Planner.\n- Suggest indoor activities suitable for that slot.\n- Provide reasoning logs why each activity is suggested.',
  tools=[
    agent_tool.AgentTool(agent=indoor_entertainment_agent_google_search_agent),
    agent_tool.AgentTool(agent=indoor_entertainment_agent_url_context_agent)
  ],
)
outdoor_entertainment_agent_google_search_agent = LlmAgent(
  name='Outdoor_Entertainment_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
outdoor_entertainment_agent_url_context_agent = LlmAgent(
  name='Outdoor_Entertainment_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
outdoor_entertainment_agent = LlmAgent(
  name='outdoor_entertainment_agent',
  model='gemini-2.5-flash',
  description=(
      'Suggest outdoor activities for the user based on preferences and available time, and request detailed transport routes from the Transport Planner for each activity.'
  ),
  sub_agents=[],
  instruction='- Receive available time slots and user preferences from the Entertainment Planner.\n- Suggest suitable outdoor activity for each slot.\n- Send activity and location to Transport Planner agent.\n- Receive transport route(s) including distance, estimated time, and step-by-step directions.\n- Return the final outdoor activity block with scheduled time and transport details.\n- Include reasoning logs explaining why this activity and route were chosen.',
  tools=[
    agent_tool.AgentTool(agent=outdoor_entertainment_agent_google_search_agent),
    agent_tool.AgentTool(agent=outdoor_entertainment_agent_url_context_agent)
  ],
)
transport_planner_agent_google_search_agent = LlmAgent(
  name='Transport_Planner_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
transport_planner_agent_url_context_agent = LlmAgent(
  name='Transport_Planner_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
transport_planner_agent_2 = LlmAgent(
  name='transport_planner_agent_2',
  model='gemini-2.5-flash',
  description=(
      'Calculate the best route for outdoor activities, including distance, estimated travel time, and suggested transport mode (walking, public transport, driving, cycling). Provide clear step-by-step directions for the user.'
  ),
  sub_agents=[],
  instruction='- Receive outdoor activity and its location from the Outdoor Agent.\n- Determine the best travel options based on distance, time, and convenience.\n- Include multiple options if possible: walking, bus/train, or cycling.\n- Provide step-by-step directions (e.g., which bus to take, transfers, walking segments).\n- Return the transport schedule along with reasoning logs explaining the choice of route.',
  tools=[
    agent_tool.AgentTool(agent=transport_planner_agent_google_search_agent),
    agent_tool.AgentTool(agent=transport_planner_agent_url_context_agent)
  ],
)
coordinator_agent_google_search_agent = LlmAgent(
  name='Coordinator_Agent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
coordinator_agent_url_context_agent = LlmAgent(
  name='Coordinator_Agent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
root_agent = LlmAgent(
  name='Coordinator_Agent',
  model='gemini-2.5-flash',
  description=(
      'Orchestrate all tasks for the student, merge study plans, entertainment (indoor/outdoor), and transport schedules.'
  ),
  sub_agents=[study_planner_agent, entertainment_planner_agent, indoor_entertainment_agent, outdoor_entertainment_agent, transport_planner_agent_2],
  instruction='- Greet the user.\n- Ask for their weekly assignments, exams, and preferences.\n- Delegate study planning to the Study Planner agent.\n- Delegate entertainment planning to the Entertainment Planner agent.\n- Merge results from all sub-agents into a weekly timetable.\n- Show thinking logs for each step.',
  tools=[
    agent_tool.AgentTool(agent=coordinator_agent_google_search_agent),
    agent_tool.AgentTool(agent=coordinator_agent_url_context_agent)
  ],
)