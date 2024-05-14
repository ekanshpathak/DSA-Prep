# Print numbers from N to 1 in N lines

N = 5

def PrintDecreasing(N):             # Faith
    
    if N==1:                        # Base
        print(1)                    #
        return False                # Condition
    
    print(N)                        # Main
    return PrintDecreasing(N-1)     # Logic


PrintDecreasing(N)