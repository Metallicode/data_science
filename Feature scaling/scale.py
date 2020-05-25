import csv
import matplotlib.pyplot as plt

def get_data_as_list():
    with open('fixed.csv', newline='') as csvfile:
        return list(csv.reader(csvfile))

def get_col(lst, col):
    return [float(i[col]) for i in lst]

def plot_data(data):
    x = range(0,len(data))
    plt.plot(x,data)


#this is the importent part...
def Rescaling(lst):
    min_val = min(lst)
    max_val = max(lst)
    rescaledLst = []

    for i in lst:
        rescaledLst.append( (i-min_val) / (max_val-min_val))

    return rescaledLst
    

def Rescale_to_range(lst, new_min, new_max):
    min_val = min(lst)
    max_val = max(lst)
    rescaledLst = []

    for i in lst:
        rescaledLst.append(new_min + ((i-min_val)*(new_max-new_min) / (max_val-min_val)))

    return rescaledLst

    
data = get_data_as_list()

###Problem...
##plot_data(get_col(data,0))
##plot_data(get_col(data,1))


###Rescale to 0:1 range
##plot_data(Rescaling(get_col(data,0)))
##plot_data(Rescaling(get_col(data,1)))


###Rescale to custom range
plot_data(Rescale_to_range(get_col(data,0), 50,75))
plot_data(Rescale_to_range(get_col(data,1), 50,75))


plt.show()



