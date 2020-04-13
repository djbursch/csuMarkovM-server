import numpy as np

def cost(UnivGrad10, cohortgrad):
	for i=1:6
		graderror(i)=(UnivGrad10(i)-cohortgrad(i))^2/((UnivGrad10(i)+.0001)^2);
	end sumerror=sum(graderror);