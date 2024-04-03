def move_and_remove_N_elements(listOne, listtwo, N):
    # Ensure N is not greater than the length of listOne
    N = min(N, len(listOne))

    # Move the last N elements from listOne to listtwo
    elements_to_move = listOne[-N:]
    del listOne[-N:]  # Remove the last N elements from listOne
    # Insert the elements from elements_to_move into listtwo in the desired order
    listtwo.extend(elements_to_move[::-1])


# Example usage:
listOne = ['Z', 'N', 'D']
listtwo = ['U', 'I', 'C']
N = 2

move_and_remove_N_elements(listOne, listtwo, N)

print("listOne:", listOne)
print("listtwo:", listtwo)