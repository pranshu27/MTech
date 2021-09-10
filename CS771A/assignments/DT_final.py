df.head()

#cleaning
df = df.replace(' ?',np.nan)
df.isna().sum()

df.fillna(df.mode().loc[0], inplace=True)
df.isna().sum()




for col in column_names:
  df[col], tmp  = pd.Series(list(df[col])).factorize()

#df.drop(['gain', 'loss'], axis = 1)

df.info()


for col in column_names:
    maxx = df[col].max()
    minn = df[col].min()
    
    
    df[col] = df[col].apply(lambda x: (x-minn)/(maxx-minn))
    
for d in ['fnlwgt', 'capital-gain', 'capital-loss', 'education-num', 'income', 'age']:
    column_names.remove(d)

#df.drop(['fnlwgt', 'capital-gain', 'capital-loss', 'education-num'], axis=1, inplace=True)

df.head()

def ent(col):
    counts = np.unique(col,return_counts=True)
    ent = 0.0
    for ix in counts[1]:
        p = ix/col.shape[0]
        ent += (-1.0*p*np.log2(p))
    return ent

def splitd(x_data,fkey,fval):
    x_right = pd.DataFrame([],columns=x_data.columns)
    x_left = pd.DataFrame([],columns=x_data.columns)
    for i in range(x_data.shape[0]):
        val = x_data[fkey].loc[i]
        if val >=fval:
            x_right = x_right.append(x_data.iloc[i])
        else:
            x_left = x_left.append(x_data.iloc[i])
    return x_right,x_left

def ig(x_data,fkey,fval):
    right,left = splitd(x_data,fkey,fval)
    
    l = float(left.shape[0])/x_data.shape[0]
    r = float(right.shape[0])/x_data.shape[0]
    if left.shape[0] == 0 or right.shape[0] == 0:
        return -99999
    i_gain = ent(x_data.income) - (l * ent(left.income) + r*ent(right.income))
    return i_gain

class DecisionTree:
    def __init__(self,depth=0,max_depth=10):
        self.left = None
        self.right = None
        self.fkey = None
        self.fval = None
        self.depth = depth
        self.max_depth = max_depth
        self.target = None
    def train(self,x_train):
        features=column_names
        info_gains = []
        for ix in features:
            i_gain = ig(x_train,ix,x_train[ix].mean())
            info_gains.append(i_gain)
        self.fkey = features[np.argmax(info_gains)]
        self.fval = x_train[self.fkey].mean()
        print("Splitting Tree",self.fkey)
        data_right,data_left = splitd(x_train,self.fkey,self.fval)
        data_right = data_right.reset_index(drop=True)
        data_left = data_left.reset_index(drop=True)
        if data_left.shape[0] == 0 or data_right.shape[0] == 0:
            if x_train.income.mean() >= 0.5:
                self.target = "Positive"
            else:
                self.target = "Negative"
            return
        if self.depth >= self.max_depth:
            if x_train.income.mean() >= 0.5:
                self.target = "Positive"
            else:
                self.target = "Negative"
            return
        self.left = DecisionTree(self.depth+1,self.max_depth)
        self.left.train(data_left)
        self.right = DecisionTree(self.depth+1,self.max_depth)
        self.right.train(data_right)
        if x_train.income.mean() >= 0.5:
            self.target = "Positive"
        else:
            self.target = "Negative"
        return
    def predict(self,test):
        if test[self.fkey] > self.fval:
            if self.right is None:
                return self.target
            return self.right.predict(test)
        if test[self.fkey] <= self.fval:
            if self.left is None:
                return self.target
            return self.left.predict(test)

split = int(0.7*df.shape[0])
train_data = df[:split]
test_data = df[split:]
test_data= test_data.reset_index(drop=True)

dt = DecisionTree()

train_data

#train_data.columns.values

#train_data.drop(['edu_num'], axis=1, inplace=True)

dt.train(train_data)

y_pred = []
for ix in range(test_data.shape[0]):
    y_pred.append(dt.predict(test_data.loc[ix]))

y_pred[:10]

for i in range(len(y_pred)):
    if y_pred[i] == "Negative":
        y_pred[i] = 0
    else:
        y_pred[i] = 1

np.mean(y_pred == test_data['income'])
