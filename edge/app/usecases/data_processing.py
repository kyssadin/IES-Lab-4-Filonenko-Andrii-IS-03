from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def check_quality (value):
    if value > -50 and value <= 50: return "Good Quality"
    elif ((value > -100) and (value <= -50)) or ((value > 50) and (value <= 100)): return "Appropriate Quality"
    return "Poor Quality"

def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    road_condition = agent_data.accelerometer.y
    state = check_quality(road_condition)
         
    return ProcessedAgentData(road_state=state, agent_data=agent_data)
