#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gym
from gym import error, spaces, utils
from gym.utils import seeding
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
import pandas.util.testing as tm
from sklearn.linear_model import LogisticRegression
from scipy.stats import truncnorm
import math

#Gym environment

class DiscreteEnv(gym.Env):
  def __init__(self):
    self.size = 10
    #get initial values for theta's
    #fit logit model to data
    self.df = pd.DataFrame(dict(
            Xs=truncnorm.rvs(a=0, b= math.inf,size=self.size),
            Xa=truncnorm.rvs(a=0, b= math.inf,size=self.size),
            Y=np.random.binomial(1, 0.05, self.size)))
    self.model = LogisticRegression().fit(self.df[["Xs", "Xa"]], np.ravel(self.df[["Y"]]))

    #extract theta parameters from the fitted logistic

    self.thetas = np.array([self.model.coef_[0,0] , self.model.coef_[0,1], self.model.intercept_[0]]) #thetas[1] coef for Xs, thetas[2] coef for Xa

    #set range for obs space
    #? not all values should be equaly likely to be sampled, this is missing here
    #? can I restrict the sampling space when an episode is run?
    self.minXa1 = pd.to_numeric(min(self.df[["Xa"]].values.flatten()))
    self.minXs1 = pd.to_numeric(min(self.df[["Xs"]].values.flatten()))
    
    self.maxXa1 = pd.to_numeric(max(self.df[["Xa"]].values.flatten()))
    self.maxXs1 = pd.to_numeric(max(self.df[["Xs"]].values.flatten()))
    
    self.min_Xas=np.array([np.float32(self.minXa1), np.float32(self.minXs1)])
    self.max_Xas=np.array([np.float32(self.maxXa1), np.float32(self.maxXs1)])
    
    
   
    #set ACTION SPACE
    #discrete 0, 1
    self.action_space = spaces.Discrete(n=2)
    
    #set OBSERVATION SPACE
    #it is made of values for Xa, Xs for each observation
    self.observation_space = spaces.Box(low=self.min_Xas, 
                                   high=self.max_Xas, 
                                   dtype=np.float32)
    
    #self.Y_obs_space = spaces.Discrete(n=2)
    #combine them in a tuple - I think it doesn't work well
    #self.observation_space = spaces.Tuple([self.Xas_obs_space, self.Y_obs_space])

    #set an initial state, sample a random row from df to get 1 observation (Xs(0), Xa(0))
    #the step def will update self.state according to some value
    self.state=None    #self.df.sample(n=1, random_state=1).values.reshape(3,)

    #introduce some (short) length (time steps)
    self.horizon=20
    
    

  def seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]    


  
#take an action with the environment
#it returns the next observation, the immediate reward, whether the episode is over (done) and additional information    
#"action" argument is one value in the range of the action space (logit transform)
  def step(self, action):
    
    self.state = self.df
    
    
    data = []
    for f in self.state.itertuples(index=False):
      Xs = f[0]
      Xa = f[1]
      Y = f[2]
      Xsa=(self.thetas[0])+(self.thetas[1])*(Xs)+(self.thetas[2])*(Xa)
      rho2 = (1/(1+np.exp(-Xsa)))  #prob of Y=1
      g2 = ((Xa) + 0.5*((Xa)+math.sqrt(1+(Xa)**2)))*(1-rho2) + ((Xa) - 0.5*((Xa)+math.sqrt(1+(Xa)**2)))*rho2
      if (rho2>0.2) or (action == 1):
        Xa=g2
      else: Xa=Xa 

      data.append([Xs, Xa, Y])

    df_new = pd.DataFrame(data, columns=['Xs', 'Xa', 'Y']) 

    model1 = LogisticRegression().fit(df_new[["Xs", "Xa"]], np.ravel(df_new[["Y"]]))

    #extract theta parameters from the fitted logistic
    thetas1 = np.array([model1.coef_[0,0] , model1.coef_[0,1], model1.intercept_[0]])
    #extract theta parameter for Xa from the fitted logistic
    theta_updated = np.array([model1.coef_[0,1]]) #thetas[1] coef for Xs, thetas[2] coef for Xa


    list1= []
    for i in df_new.itertuples(index=False):
      Xss = i[0] #no change
      Xaa = i[1] #no change
      YY = i[2] #no change

      Z1 = ((thetas1[0])+(thetas1[1])*(Xss)+(thetas1[2])*(Xaa))
      Prob1 = np.exp(Z1)/(1+np.exp(Z1)) #P(Y=1)
  

      list1.append([Prob1])

    list_new = pd.DataFrame(list1, columns=['Prob1']) 
    Ynew_cumul = np.mean(list_new["Prob1"])
    #reduce the horizon
    self.horizon -= 1
    
    #depending on the value of self.state, apply a reward
    reward = self.Ynew_cumul 
    
    #check if horion is over, otherwise keep on doing
    if self.horizon <= 0:
        done = True
    else:
        done = False

    #set placeholder for infos
    info ={}        
     
    return self.state, reward, done, theta_updated , {}

#reset state and horizon    
  def reset(self):
    self.state=self.df
    self.horizon = 20
    return self.state



# In[ ]:




