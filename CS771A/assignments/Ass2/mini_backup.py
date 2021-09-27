

def lr_mb_gd(X, Y, batch_size, learning_rate = 0.01, init_a = 0, init_b = 0, max_iter = 10000, tol = 1e-04):
    start_time = time.time()
    a = 0
    b = 0

    n = float(len(X)) 
    
    for i in range(max_iter): 
        #np.random.seed (5)
        random_index=np.random.randint(0,n-batch_size-1)
        X_mini= X[random_index:random_index+batch_size]
        Y_mini = Y[random_index:random_index+batch_size]
        
        n_tmp = len(X_mini)
        Y_pred = a*X_mini + b 

        D_a = (-2/n_tmp) * np.dot(X_mini.T,(Y_mini - Y_pred))  
        D_b = (-2/n_tmp) * sum(Y_mini - Y_pred)  

        delta_a = (-1)*learning_rate * D_a
        delta_b = (-1)*learning_rate * D_b

        if (np.all(np.abs (delta_a) <= tol) & np.all(np.abs (delta_b) <= tol)): 
            break

        a+=delta_a
        b+=delta_b

# =============================================================================
#         print(i)
# =============================================================================
    #print('It took ', str(i+1), ' iterations to arrive at the desired result')
    #print("--- %s seconds ---" % (time.time() - start_time))
    #print (round(a,2), round(b,2))
    return str(i+1), time.time() - start_time, round(a,2), round(b,2)