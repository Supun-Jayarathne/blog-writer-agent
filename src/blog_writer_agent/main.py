import sys
import warnings

import gradio as gr

from blog_writer_agent.crew import BlogWriterAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

topic = ''

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
    }
    
    try:
        BlogWriterAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def run_crewai_app(topic):
    topic = topic
    final_answer = BlogWriterAgent().crew().kickoff(inputs={'topic': topic})
    return final_answer

iface = gr.Interface(
    fn=run_crewai_app,
    inputs=[gr.Textbox(label="Area", placeholder="Enter the area you wish to write a blog about")],
    outputs=gr.Textbox(label="Generated Blog Content"),
    title="CrewAI blog writer agent",
    description="Write a blog by finding topic from a given area by the user."
)

iface.launch(share=True)