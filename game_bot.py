import gym
import universe
env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1) #creates a local docker container

#write game bot logic
observation_n = env.reset() #retrieve list of observations for the current environment initialized
action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
observation_n, reward_n, done_n, info = env.step(action_n)
while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    # reward_n - check if action is beneficial or not: 1/-1
    # done_n - indicates if game is over
    #info - misc info: performance, latency, etc to see and tweak performace of bot


    print "observation is "
    print observation_n
    print "reward is "
    print reward_n
    print "done is "
    print done_n
    print "info is "
    print info

env.render()
