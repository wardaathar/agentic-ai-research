# agent.py
import time

class Agent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def run(self):
        print(f"[{self.name}] Task Started: {self.task}")
        time.sleep(1)
        print(f"[{self.name}] Task Completed!")

if __name__ == "__main__":
    agent = Agent("DataAgent", "Collect data from web")
    agent.run()
