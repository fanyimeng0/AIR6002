import itertools

def characteristic_function(x):
    
    v = 2*x[1] + 3*x[2] + 4*x[3] + 5*x[0]*x[2] + 7*x[1]*x[4] - 12*x[0]*x[1]*x[2]
    return v

def shapley_value(n_players):

    shapley_values = [0] * n_players
    subsets = list(itertools.permutations(range(n_players)))
    
    for subset in subsets:
        for i in range(n_players):

            new_subset = list(subset[:i]) + [n_players - 1] + list(subset[i:])

            value_with_player = characteristic_function(new_subset)

            value_without_player = characteristic_function(subset)

            marginal_contribution = value_with_player - value_without_player

            shapley_values[i] += marginal_contribution / len(subsets)
            
    return shapley_values

def main():
    players = 5
    shapley_values = shapley_value(players)
    
    print("Shapley Values:")
    for i, value in enumerate(shapley_values):
        print(f"Player {i+1}: {value}")

if __name__ == "__main__":
    main()
