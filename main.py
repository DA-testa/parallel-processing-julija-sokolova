# python3
# Jūlija Sokolova 221RDB058
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    pav=[(i, 0) for i in range(n)]
    for i in range(m):
        pav1,lai=min(pav, key=lambda x: x[1])
        
        output.append((pav1, lai))
        pav[pav1]=(pav1, lai + data[i])
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int, input().split())
    #m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pav1, lai in result:
        print(pav1, lai)


if __name__ == "__main__":
    main()
