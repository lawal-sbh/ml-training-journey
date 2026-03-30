import random
rewards = [random.uniform(-1, 1) for _ in range(500)]

class RewardAnalyser:
    def __init__(self, rewards):
        self.rewards = rewards
    
    def average_reward(self):
        if not self.rewards:
            return None
        return sum(self.rewards) / len(self.rewards)
    
    def improvement_rate(self):
        if len(self.rewards)< 200:
            return ("not enough data (need minimum of 200 data points)")
        first_100 = self.rewards[:100]
        last_100 = self.rewards[-100:]

        first_average = sum(first_100)/len(first_100)
        last_average = sum(last_100)/ len(last_100)

        rate = (last_average - first_average)/ abs(first_average) * 100
        return round( rate, 2)

    def plot_summary(self):
        print("Reward progression (every 100 steps):")
        for i in range(0, len(self.rewards), 100):
            chunk = self.rewards[i:i+100]
            if len(chunk) ==0:
                break
            avg = sum(chunk)/len(chunk)
            bar = "#" * int(abs(avg) * 10)
            print(f"step {i:>5}: {avg:6.2f} |{bar}")     
analyser = RewardAnalyser(rewards)
print("Average reward:", analyser.average_reward())
print("Improvement rate:", analyser.improvement_rate(), "%")
analyser.plot_summary()    