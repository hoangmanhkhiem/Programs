import numpy as np 
import matplotlib.pyplot as plt 
  
def estimate_coef(x, y): 
    n = np.size(x) 
    m_x, m_y = np.mean(x), np.mean(y) 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
    b = SS_xy / SS_xx 
    a = m_y - b*m_x 
    return(a, b) 
   
def plot_regression_line(x, y, b): 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
    y_pred = b[0] + b[1]*x 
    plt.plot(x, y_pred, color = "g") 
    plt.xlabel('x') 
    plt.ylabel('y')
    plt.show() 

def forecast(x,a,b):
    return print("Du doan gia tri Y khi X = ",x," la ",a*x+b)
 
def main(): 
    x = np.array([1, 2, 4, 6, 8]) 
    y = np.array([5, 7, 11, 15, 19])
    X = np.array([7, 11])
    b = estimate_coef(x, y) 
    # plot_regression_line(x, y, b) 
    print("Gia tri cua a = {}  \nGia tri cua b = {}".format(b[0], b[1]))
    for i in X:
        forecast(i,b[0],b[1])
 
if __name__ == "__main__": 
    main() 