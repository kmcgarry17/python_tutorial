
# Column names and column indices to read
# create a dictionary
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column (if not string)
types = {'tempout': float, 'windspeed': float, 'windchill':12}

# Initialize my data variable 
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:

    for _ in range(3):
        datafile.readline()

    # Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value = t(split_line[i])
            data[column].append(value)

# compute the wind chill temperature
# write a function!

def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v ** 16

    wci = a + (b * t) - (c * v16) + (d * t * v16)
    return wci


# use the function to compute the windchill
windchill = []
for temper, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))


# output comparison of data
print('                        ORIGINAl    COMPUTED')
print('  DATE          TIME    WINDCHILL    WINDCHILL   DIFFERENCE')
print(' --- ----- ------- -------- --------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:.6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')


