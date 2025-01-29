#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
import gradio as gr

from blog_writer_agent.crew import BlogWriterAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
area = ''

def run():
    """
    Run the crew.
    """
    inputs = {
        'area': area,
    }
    
    try:
        BlogWriterAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'area': area,
    }
    try:
        BlogWriterAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogWriterAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'area': area,
    }
    try:
        BlogWriterAgent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_crewai_app(area):
    # global area
    area = area
    final_answer = BlogWriterAgent().crew().kickoff(inputs={'area': area})
    return final_answer

iface = gr.Interface(
    fn=run_crewai_app,
    inputs=[gr.Textbox(label="Area", placeholder="Enter the area you wish to write a blog about")],
    outputs=gr.Textbox(label="Generated Blog Content"),
    title="CrewAI blog writer agent",
    description="Write a blog by finding topic from a given area by the user."
)

iface.launch(share=True)