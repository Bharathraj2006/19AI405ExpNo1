import random

class MedicinePrescribingAgent:
    def __init__(self):
        self.rooms = {"Room1": random.uniform(97, 102), 
                      "Room2": random.uniform(97, 102)}  
        self.location = "Room1"
        self.performance = 0

    def move(self):
        self.location = "Room2" if self.location == "Room1" else "Room1"
        self.performance -= 1
        print(f"Agent moved to {self.location}")

    def check_and_treat(self):
        temp = self.rooms[self.location]
        print(f"Checking patient in {self.location} with temp: {temp:.1f}°F")

        if temp > 98.5:
            print("Patient has fever. Prescribing medicine ✅")
            self.performance += 10
            self.rooms[self.location] = 98.0  
        else:
            print("Patient is healthy. No medicine needed.")

    def run(self, steps=4):
        for i in range(steps):
            print(f"\nStep {i+1}: Agent in {self.location}")
            self.check_and_treat()
            if i < steps - 1:
                self.move()
        print(f"\nFinal Performance Score: {self.performance}")

agent = MedicinePrescribingAgent()
agent.run()
