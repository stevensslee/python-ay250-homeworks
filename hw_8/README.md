# Python AY 250 Homework

Homework submissions for AY 250, Spring 2022.
Name: STEVEN LEE

## Homework 8
[Homework 8](https://github.com/stevensslee/python-ay250-homeworks/blob/main/hw_8/hw8_bayes_pymc.ipynb) was completed on Apr. 19, 2022.


Problem 1 A/C:
For part A, I considered the posterior speed in the x and y direction for the blue and red objects individually, i.e., I took the absolute difference between the x and y positions and divided by the time interval. For part C) I instead considered the posterior speed of the speed, i.e., speed = sqrt(v_x^2 + v_y^2) for the blue and red objects. For A and C) both the prior and likelihood assumed to be gaussian. The resulting posterior gaussian was sampled using pymc3 in both A and C. 

Problem 1 B:
Not sure if there is a principled way to remove the white noise from the position measurements or use samples to generate and estimate the confidence interval. 

Problem 1D:
Repeated A/C with only 100 measurements from the loaded csv file. 
